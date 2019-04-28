a. From LPN!

i. Exercise 1.4

1. Butch is a killer.
killer(butch).
This is a fact with the attribute of a killer, and that is applied to whoever is named in the parentheses, in this case, Butch.
2. Mia and Marsellus are married.
married(mia,marsellus).
married(marsellus,mia).
The attribute married is applied to both Mia and Marsellus, but I wanted to make sure that it went both ways, which is why I put both ordered pairs down.
3. Zed is dead.
dead(zed).
This is a fact with the attribute of someone being dead, and that is applied to whoever is named in the parentheses, in this case, Zed.
4. Marsellus kills everyone who gives Mia a footmassage.
kill(marsellus,X):- footmassage(X,mia).
This one contains a variable, X, which is person who Marsellus may kill. It is a conditional statement saying if X gives mia a foot massage, then Marsellus will kill X.
5. Mia loves everyone who is a good dancer.
love(mia,X):- good_dancer(X).
This one also contains a variable, X, which is person who Mia may love. It is a conditional statement saying if X is a good dancer, then Mia will love X.
6. Jules eats anything that is nutritious or tasty. 
eat(jules,X):-
	nutritious(X);
	tasty(X).
This one is a conditional statement with an “or” designated by the semi-colon. It says if X is nutritious or if X is tasty, then Jules will eat X.

ii. Exercise 1.5

1. wizard(ron).
	yes
	There is a fact in the knowledge base that is exactly the same.
2. witch(ron).
	no
	There is no such fact or rule that includes “witch” in the knowledge base.
3. wizard(hermione).
	no
There is no such name hermione in this knowledge base, and wizard references back to hasBroom, which references back to quidditchPlayer with the name Harry in its fact, and hasWand, which also has the name Harry in its fact.
4. witch(hermione).
	no
There is no such name hermione in this knowledge base, and wizard references back to hasBroom, which references back to quidditchPlayer with the name Harry in its fact, and hasWand, which also has the name Harry in its fact.
5. wizard(harry).
	yes
Wizard references back to hasBroom, which references back to quidditchPlayer with the name Harry in its fact, and hasWand, which also has the name Harry in its fact.
6. wizard(Y).
	Y = ron
It finds the first instance of a wizard in the knowledge base and prints that out, which in this case is Ron.
7. witch(Y).
	no
There is no such fact or rule that includes “witch” in the knowledge base, so it prints out “no” to show it doesn’t have any results that match the query.

b. Prolog does implement modus ponens quite easily in the form of “head :- body.” The head is what will be true if the body is true (if body then head). For instance, stomachache(sarah) :- eattoomuch(sarah). means if Sarah eats too much, she will get a stomach ache.

c. Horn clauses provide a more efficient representation than propositional logic does in Prolog, however, they horn clauses only have one or zero true statements whereas propositional logic can have more. Horn clauses can only imply one statement, but propositional logic can imply more than one. Also, propositional logic cannot use variables, but horn clauses can.

d. Telling means that you are commanding an object to do something rather than asking it and then acting on the response. Prolog uses “tell” when it declares facts (it has no choice but to create those facts), and it uses “ask” when queries are used to find out information about the knowledge base.
