
head este primul element, tail este o lista din elementele ramase

1 ?- [1, 2, 3, 4, 5] = [Head | Tail].
Head = 1,
Tail = [2, 3, 4, 5].

2 ?- [2,3] = [Head | Tail].
Head = 2,
Tail = [3].

3 ?- [2] = [Head | Tail].
Head = 2,
Tail = [].

4 ?- [1, 2, 3, 4, 5] = [_, X | _].
X = 2.
headul tailului

element_of(X,[X|_]).
element_of(X,[_|T]) :- element_of(X,T).

?- element_of(a,[a,b,c]).
true 
?- element_of(X, [a, b, c]).
X = a ;
X = b ;
X = c ;

cu variabilele parcurgem lista

concat_lists([Elem | List1], List2, [Elem | List3])
 :- concat_lists(List1, List2, List3).


 all_a([]).
 all_a([a | T]) :- all_a(T).

 trans_a_b([], []).
 trans_a_b([a | T1], [b | T2]):- trans_a_b(T1, T2).

scalar_mult(_, [], []).
scalar_mult(N, [H|T], [H1|T1]) 
:- H1 is N * H, scalar_mult(N, T, T1).

dot([], [], 0).
dot([H|T], [H1|T1], R)
:- dot(T, T1, R1), R is R1 + H * H1.