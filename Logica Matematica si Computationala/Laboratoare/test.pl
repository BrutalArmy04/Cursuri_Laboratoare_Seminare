pack([],[]).
pack([X|Xs],[Z|Zs]) :- transfer(X,Xs,Ys,Z), pack(Ys,Zs).
transfer(X,[],[],[X]).
transfer(X,[Y|Ys],[Y|Ys],[X]) :- X \= Y.
transfer(X,[X|Xs],Ys,[X|Zs]) :- transfer(X,Xs,Ys,Zs).
encode(L1,L2) :- pack(L1,L), transform(L,L2).
transform([],[]).
transform([[X|Xs]|Ys],[[N,X]|Zs]) :- length([X|Xs],N), transform(Ys,Zs).
encode_modified(L1,L2) :- encode(L1,L), strip(L,L2).
strip([],[]).
strip([[1,X]|Ys],[X|Zs]) :- strip(Ys,Zs).
strip([[N,X]|Ys],[[N,X]|Zs]) :- N > 1, strip(Ys,Zs).

dec_concat([]).
dec_concat(R) :- check(R, N).
check(R, N) :- check([H|T], N):- check([H1|T1], N), H > H1, M is N+1, check ([T], M), M /== 2.




vars(V, [V]) :- atom(V).
vars(non(F), L) :- vars(F, L).
vars(si(F1, F2), L) :- vars(F1, L1), vars(F2, L2), union(L1, L2, L).
vars(sau(F1, F2), L) :- vars(F1, L1), vars(F2, L2), union(L1, L2, L).
vars(imp(F1, F2), L) :- vars(F1, L1), vars(F2, L2), union(L1, L2, L).

subformula(_, _).
subformula(Phi, Psi) :- subformula(vars(vars(Phi), vars(Psi))).

proper_subformula(_, _).
proper_subformula(Phi, Psi):- subformula(Phi, Psi), Phi /== Psi.