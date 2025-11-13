%lab 3 ultimul ex

max([], 0).
max([H|T], Y) :- max(T, Y), Y>=H.
max([H|T], H) :- max(T, Y), H>Y.
% luat de la coada la cap, recursiv, nu merge normal

%ex1

reverse([], []).
reverse([H|T], R) :- reverse(T, R1), append(R1, [H], R).
palindrome(L) :- reverse(L, L).

%ex2

remove_duplicates([], []).
remove_duplicates([H|T], [H|D]) :- remove_duplicates(T, D), not(member(H, D)).
remove_duplicates([H|T], D) :- remove_duplicates(T, D), member(H, D).

%ex3

atimes(_, [], 0).
atimes(X, [X|T], Y) :- atimes(X, T, C), Y is C+1.
atimes(X, [H|T], Y) :- atimes(X, T, Y), X\=H.

%ex4

insert(X, [], [X]).
insert(X, [H|T], [X, H|T] /*sau [X||[H\T]]*/) :- X=<H.
insert(X, [H|T], [H|T1]) :- X>H, insert(X, T, T1).
%  [X|T] este o lista deja sortata, [H|T1] este lista sortata cu X adaugat

%ex5

quicksort([],[]).
quicksort([H|T],L) :- split(H,T,A,B), quicksort(A,M), quicksort(B,N),
append(M,[H|N],L).
split(_,[],[],[]).
split(H,[X|T],[X|A],B) :- X=<H, split(H,T,A,B).
split(H,[X|T],A,[X|B]) :- X>H, split(H,T,A,B).

