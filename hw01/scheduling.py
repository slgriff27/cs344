"""
This implements a course scheduling domain using the AIMA constraint satisfaction framework.
I solved this problem based on the logic from the zebra problem. Both define variables, which,
in this case, are the classes. Then I set the domain for each of the classes, which is every
combination of professors, times, and classrooms a class could have. Lastly, I created a
dictionary of every possible class that could be taught at the same time as another class to
create the neighbors. After all of that was finished, I used min_conflicts to solve the problem.
This was all based on the general setup of the zebra problem that is laid out in csp.py.

@author: Sarah Griffioen (slg27)
@date: 2/23/2019
"""

from tools.aima.csp import CSP, min_conflicts

#finds all possible pairs of times and rooms
def time_room_pairs(times, rooms):
    timeRoomList = []
    for i in range(len(times)):
        for j in range(len(rooms)):
            timeRoomList.append(times[i] + ',' + rooms[j])
    return timeRoomList

#finds all possibilities of profs, times, and rooms for each class
def course_assignment_pairs(assignments, timeRoomList):
    courseAssignmentDict = {}
    for key, value in assignments.items():
        permutations = []
        for i in range(len(timeRoomList)):
            permutations.append(value + ',' + timeRoomList[i])
        courseAssignmentDict[key] = permutations
    return courseAssignmentDict

#finds all possible course pairs
def create_neighbors(courses):
    neighborDict = {}
    for i in range(len(courses)):
        validCoursesList = []
        for j in range(len(courses)):
            if(courses[j] != courses[i]):
                validCoursesList.append(courses[j])
        neighborDict[courses[i]] = validCoursesList
    return neighborDict

#apply constraints
def faculty_constraint(course1, slot1, course2, slot2):
    detailsList1 = slot1.split(',')
    detailsList2 = slot2.split(',')

    #assign variables to time, room, and faculty
    prof1 = detailsList1[0]
    prof2 = detailsList2[0]
    time1 = detailsList1[1]
    time2 = detailsList2[1]
    place1 = detailsList1[2]
    place2 = detailsList2[2]

    #return true only if there are no time/faculty or time/place conflicts
    return ((time1 != time2) or (prof1 != prof2) and (time1 != time2) or (place1 != place2))

#define variables and set domains and neighbors
courses = ['cs108', 'cs112', 'cs212', 'cs214', 'cs232', 'cs262', 'cs342']
assignments = {'cs108': 'schuurman', 'cs112': 'adams', 'cs212': 'plantinga', 'cs214': 'schuurman', 'cs232': 'adams', 'cs262': 'bailey', 'cs342': 'bailey'}
classtimes = ['mwf0900', 'mwf1030', 'mwf1130', 'mwf1230']
classrooms = ['nh253', 'sb382']
domains = course_assignment_pairs(assignments, time_room_pairs(classtimes, classrooms))
neighbors = create_neighbors(courses)

#calculate and print out results
print('\nVariables: ' + '\n' + str(courses))
print('Domains: ' + '\n' + str(domains))
print('Neighbors: ' + '\n' + str(neighbors))
solution = min_conflicts(CSP(courses, domains, neighbors, faculty_constraint))
if solution is None:
    print('no solution')
else:
    print('\nSolution:\n\nClass\tProfessor\tTime\t\tClassroom\n-----------------------------------------')
    for key, value in solution.items():
        detailsList = value.split(',')
        if (detailsList[0] == 'adams' or detailsList[0] == 'bailey'):
            detailsList[0] += '\t'
        print(key + '\t' + detailsList[0] + '\t' + detailsList[1] + '\t\t' + detailsList[2])
