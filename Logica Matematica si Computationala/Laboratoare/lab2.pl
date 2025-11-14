%ex1:
/* 3+5 is 8 nu merge, dar 8 is 3+5 merge
daca vr evaluat doar termenul din dreapta folosesti is*/

distance((XA, YA), (XB, YB), X):-
    X is ((XA-XB)**2 + (YA-YB)**2)**0.5.

distance((XA, YA), (XB, YB), X):-
    X = ((XA-XB)**2 + (YA-YB)**2)**0.5.

/*  7 ?- distance((0,0), (3,4), X).
X = 5.0 ; - cu is
X = ((0-3)**2+(0-4)**2)**0.5. - cu = */



%ex2:

fib(0, 1).
fib(1, 1).
fib(N, X) :- 2 =< N, M is N-1, fib(M, Y),
            P is N-2, fib(P, Z), X is Y + Z.
         
%daca e doar atat e f redundant
fibo(0, 0, 1).
fibo(1, 1, 1).
fibo(N, Z, X) :- 2 =< N, M is N-1, fibo(M, Y, Z),
    X is Y + Z.
fibg(N, X) :- fibo(N, _, X).

%ex3:

line(0, _).
line(X, C):- X>0, Y is X-1, write(C), line(Y, C).
rectangle(0, _, _):-n1.
rectangle(X, Z, C):- X>0, line(Z, C), n1, Y is X-1,
rectangle(Y, Z, C).
square(X, C) :- rectangle(X, X, C).
square2(X, C):- Y is X+4, rectangle(X, Y, C).