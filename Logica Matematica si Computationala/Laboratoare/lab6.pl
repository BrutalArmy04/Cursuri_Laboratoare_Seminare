%ex1

vars(V, [V]) :- atom(V).
vars(non(F), L) :- vars(F, L).
vars(and(F1, F2), L) :- vars(F1, L1), vars(F2, L2), union(L1, L2, L).
vars(or(F1, F2), L) :- vars(F1, L1), vars(F2, L2), union(L1, L2, L).
vars(imp(F1, F2), L) :- vars(F1, L1), vars(F2, L2), union(L1, L2, L).

%ex2


var(V, [(V, Val)|_], Val).
var(V, [_|T], Val) :- var(V, T, Val).

%ex3

bsi(1, 0, 0).
bsi(1, 1, 1).
bsi(0, 0, 0).
bsi(0, 1, 0).

bsau(1, 0, 1).
bsau(1, 1, 1).
bsau(0, 0, 0).
bsau(0, 1, 1).

bimp(1, 0, 0).
bimp(1, 1, 1).
bimp(0, 0, 1).
bimp(0, 1, 1).


%ex4


eval(V, E, B):- atom(V), var(V, E, B).
eval(non(F), E, B):- eval(F, E, B1), bnon(B1, B).
eval(and(F1, F2), E, B):- eval(F1, E, B1), eval(F2, E, B2), band(B1, B2, B).
eval(or(F1, F2), E, B):- eval(F1, E, B1), eval(F2, E, B2), bor(B1, B2, B).
eval(imp(F1, F2), E, B):- eval(F1, E, B1), eval(F2, E, B2), bimp(B1, B2, B).

%ex5

evals(_, [], []).
evals(E, [H|T], As):- eval(E, H, B), evals(E, T, As1), append([B], As1, As).



