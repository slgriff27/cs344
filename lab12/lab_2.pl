a. From LPN!

i. Exercise 2.1 (questions 1, 2, 8, 9, 14)

1. bread  =  bread
	yes
2. ’Bread’  =  bread
	yes
	The capital letter signifies a variable, and all variables can unify with other terms.
8. food(X)  =  food(bread)
	X = bread
	yes
9. food(bread,X)  =  food(Y,sausage)
	X = sausage
	Y = bread
	yes
14. meal(food(bread),X)  =  meal(X,drink(beer)) 
	no
In this case, X is trying to be assigned to both food(bread) and drink(beer), which are not the same and therefore do not unify.

ii. Exercise 2.2

1. ?-  magic(house_elf).
	no
The body of the three magic statements contain house_elf, wizard, and witch. The house_elf one would not work because it is recursive. The witch one would not work since it is a variable pointing to one of the three facts including “witch” in them, none of which evaluate to “dobby” in the end like house_elf does. The wizard one might have worked because house_elf can act as a variable pointing to “dobby.”
2. ?-  wizard(harry).
	yes
	This is a simple instantiation since X was just being replaced by “harry.”
3. ?-  magic(wizard).
	no
The body of the three magic statements contain house_elf, wizard, and witch. The house_elf one and the witch ones would not work because the values do not match up with the values in the facts themselves. The wizard one would not work because it is recursive.
4. ?-  magic(’McGonagall’).
	X = McGonagall
Yes
Even when McGonagall is seen as a variable because of its capital letter at the beginning, two variables can always be unified with other terms.
5. ?-  magic(Hermione).
	yes
This one works since the conditional statement with the witch, which has “hermione” in it, is a fact.

b. Inference does not really use unification since it uses if statements that turn into conclusions. It is not setting anything equal to anything else. It is just drawing conclusions from statements. It could be argued that through different rules in a knowledge base that are linked, unification is used. If one rule is the input to another rule with a variable, then the two are unified. However, within an inference statement, there is no unification.

c. Yes it does. Resolution is when a single valid inference rule produces a new clause implied by two clauses containing complementary literals. This happens every time there is a “head :- body” rule stated in Prolog.
