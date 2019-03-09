'''
This module implements a spam filter.

@author: slg27
@date: March 8, 2019
'''

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

spamMessageCount = 0
hamMessageCount = 0
spamList = [] # list of all words in the spam corpus
hamList = [] # list of all words in the ham corpus
spamCount = {} # dictionary of spam word and their number of occurances
hamCount = {} # dictionary of ham words and their number of occurances

# put all of the spam words into one list
for i in spam_corpus:
    spamMessageCount += 1
    for j in i:
        spamList.append(j.lower())

# count the number of occurances for each spam word and add each to a dictionary
for i in spamList:
    spamCount[i] = spamList.count(i)

# put all of the ham words into one list
for i in ham_corpus:
    hamMessageCount += 1
    for j in i:
        hamList.append(j.lower())

# count the number of occurances for each ham word and add each to a dictionary
for i in hamList:
    hamCount[i] = hamList.count(i)

# calculate probabilities of words
def spamFilter(list1, list2):
    calculatedWords = [] # a list of all the previously calculated words so that you don't calculate the same word twice
    for i in [list1, list2]:
        for j in i:
            if (j not in calculatedWords):
                # set bad number
                if (j in spamCount):
                    bad = spamCount[j]
                    calculatedWords.append(j)
                else:
                    bad = 0

                # set good number
                if (j in hamCount):
                    good = 2 * hamCount[j]
                    calculatedWords.append(j)
                else:
                    good = 0

                # print results
                if ((good + bad) > 1):
                    print(j + ": " + str(max(0.01, min(0.99, min(1.0, bad / spamMessageCount) / (min(1.0, good / hamMessageCount) + min(1.0, bad / spamMessageCount))))))
                else:
                    print(j + ": 0")
    print("\n")

# call the filter function on the lists
spamFilter(hamList, spamList)
