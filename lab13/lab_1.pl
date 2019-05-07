%Exercise 13.1

%a. Do these exercises from LPN!.

%i. Exercise 3.2

directlyIn(katarina,olga).
directlyIn(olga,natasha).
directlyIn(natasha,irina).

in(X,Y)  :-  directlyIn(X,Y).
in(X,Y)  :-  directlyIn(X,Z),
             in(Z,Y).

%i. Exercise 4.5

listtran([],[]).
listtran([X|Xs],[Y|Ys])  :-  trans(X,Y),
                             listtran(Xs,Ys).

%b.

%Yes. It implements a generalized version of modus ponens because it allows for variables and instantiation. For instance, “loves(X,Y)  :-  father(X,Y).” is an example of a statement with variables. This statement means that if X is the father of Y, then X loves Y. Anything could be unified or instantiated with these two variables to make this statement true as long as both X’s are the same and both Y’s are the same.
