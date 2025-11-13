%Varianta 2, Grupa 134, Rotaru Ștefan
% am dat pe post de marire, avand prezente la seminar

%1


count_elements([],[]).
count_elements([X|Xs],[Z|Zs]) :- count(X,Xs,Ys,1,Z), count_elements(Ys,Zs).
count(X,[],[],1,X).
count(X,[],[],N,[N,X]) :- N > 1.
count(X,[Y|Ys],[Y|Ys],1,X) :- X \= Y.
count(X,[Y|Ys],[Y|Ys],N,[N,X]) :- N > 1, X \= Y.
count(X,[X|Xs],Ys,K,T) :- K1 is K + 1, count(X,Xs,Ys,K1,T).


%2

dec_concat([]).
dec_concat(R) :- check(R, N).
check(R, N) :- check([H|T], N):- check([H1|T1], N), H > H1, M is N+1, check ([T], M), M /== 2.

%3 a)

subformula(_, _).
subformula(Phi, Psi) :- subformula(vars(vars(Phi), vars(Psi))).

% b)

proper_subformula(_, _).
proper_subformula(Phi, Psi):- subformula(Phi, Psi), Phi /== Psi.