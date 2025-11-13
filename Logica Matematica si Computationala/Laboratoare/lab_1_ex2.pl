female(mary).
female(sandra).
female(juliet).
female(lisa).
male(peter).
male(paul).
male(dony).
male(bob).
male(harry).
parent(bob, lisa).
parent(bob, paul).
parent(bob, mary).
parent(juliet, lisa).
parent(juliet, paul).
parent(juliet, mary).
parent(peter, harry).
parent(lisa, harry).
parent(mary, dony).
parent(mary, sandra).
father_of(F, C):- parent(F, C), male(F).
mother_of(M, C):- parent(M, C), female(M).
grandfather_of(GF, C):- parent(GF, P), parent(P, C), male(GF).
grandmother_of(GM, C):- parent(GM, P), parent(P, C), female(GM).
/*grandfather_of(GF, C):- father_of(GF, P), parent(P, C).*/
sister_of(S, Pe):- parent(Pa, S), parent(Pa, Pe), female(S), S\=Pe.
brother_of(S, Pe):- parent(Pa, S), parent(Pa, Pe), male(S), S\=Pe.
aunt_of(A, Pe):- sister_of(A, Pa), parent(Pa, Pe).
uncle_of(U, Pe):- brother_of(U, Pa), parent(Pa, Pe).
/*not_parent(X, Y):- \+parent(X, Y). - not good*/
not_parent(X, Y) :- (male(X); female(X)),
        (male(Y);  female(Y)),
        X\=Y, not(parent(X, Y)).

/* ca sa nu ia o pereche de 2 ori trb sa facem 
o chestie suplimentara pe care nu am
invatat-o inca*/

/*26 ?- [lab_1_ex2].
true.

27 ?- grandfather_of(X, sandra).
X = juliet .

28 ?- [lab_1_ex2].
true.

29 ?- sister_of(X, Y).     
X = lisa,
Y = paul .

30 ?- sister_of(X, Y).     
X = lisa,
Y = paul .

30 ?-




e
.
ERROR: Unknown procedure: e/0 (DWIM could not correct goal)
^  Exception: (4) setup_call_cleanup('$toplevel':notrace(call_repl_loop_hook(begin, 0)), '$toplevel':'$query_loop'(0), '$toplevel':notrace(call_repl_loop_hook(end, 0))) ? creep
31 ?- [lab_1_ex2].
true.

32 ?- aunt_of(X, Y).
X = lisa,
Y = dony ;
X = lisa,
Y = sandra ;
X = mary,
Y = harry ;
X = lisa,
Y = dony ;
X = lisa,
Y = sandra ;
X = mary,
Y = harry ;
false.

33 ?- uncle_of(X, Y).
X = paul,
Y = harry ;
X = paul,
Y = dony ;
X = paul,
Y = sandra ;
X = paul,
Y = harry ;
X = paul,
Y = dony ;
X = paul,
Y = sandra ;
false.

34 ?- [lab_1_ex2].
true.

35 ?- not_parent(bob, juliet).     
true.

36 ?- not_parent(X, juliet).
true.

37 ?- [lab_1_ex2].
true.

38 ?- not_parent(X, juliet). 
X = peter ;
X = paul ;
X = dony ;
X = bob ;
X = harry.

39 ?-   [lab_1_ex2].
true.

40 ?- not_parent(X, juliet).
X = peter ;
X = paul ;
X = dony ;
X = bob ;
X = harry.

41 ?- [lab_1_ex2].
true.

42 ?- not_parent(X, juliet).
false.

43 ?- [lab_1_ex2].
true.

44 ?- not_parent(X, juliet).
X = peter ;
X = paul ;
X = dony ;
X = bob ;
X = harry ;
X = mary ;
X = sandra ;
X = lisa.

45 ?-*/