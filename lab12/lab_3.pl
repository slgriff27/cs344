lookslikewitch(booth)
dressedlikewitch(booth)
weighssameduc(booth)
madeofwood(booth)

witch(X) :- lookslikewitch(X)
If she looks like a witch, then she is a witch.

witch(X) :- dressedlikewitch(X)
If she is dressed like a witch, then she is a witch.

madeofwood(X) :- weighssameduck(X)
If she weighs the same as a duck, then she's made of wood.

shouldbeburned(X) :- madeofwood(X)
If she’s made of wood, then she should be burned.


