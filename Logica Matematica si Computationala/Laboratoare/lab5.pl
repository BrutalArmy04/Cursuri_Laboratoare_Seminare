%ex1
listaNelem(_,0, []).
listaNelem(L, N, [H|T]) :- N>0, member(H, L), P is N-1, listaNelem(L, P, T).

%ex2

word(abalone,a,b,a,l,o,n,e).
word(abandon,a,b,a,n,d,o,n).
word(anagram,a,n,a,g,r,a,m).
word(connect,c,o,n,n,e,c,t).
word(elegant,e,l,e,g,a,n,t).
word(enhance,e,n,h,a,n,c,e).
crosswd(V1, V2, V3, H1, H2, H3) :-
    word(V1, _, A, _, B, _, C, _),
    word(V2, _, D, _, E, _, F, _),
    word(V3, _, G, _, H, _, I, _),
    word(H1, _, A, _, D, _, G, _),
    word(H2, _, B, _, E, _, H, _),
    word(H3, _, C, _, F, _, I, _).
       
%ex3

connected(1,2).
connected(3,4).
connected(5,6).
connected(7,8).
connected(9,10).
connected(12,13).
connected(13,14).
connected(15,16).
connected(17,18).
connected(19,20).
connected(4,1).
connected(6,3).
connected(4,7).
connected(6,11).
connected(14,9).
connected(11,15).
connected(16,12).
connected(14,17).
connected(16,19).

path(X, X, []).
path(X, Y, [Z|T]):-connected(X, Z), path(Z, Y, T).

pathc(X, Y):- path(X, Y, _).

%ex4

word_letters(Atom, Charlist) :-
    atom_chars(Atom, Charlist).

eliminate_letter([H|T], H, T).
eliminate_letter([H|T], L, [H|R]) :- H \= L, eliminate_letter(T, L, R).

cover([], _).
cover([H|T], L) :- eliminate_letter(L, H, R), cover(T, R).

solution(List, Word, Len):- word(Word), 
word_letters(Word, Charlist), 
cover(Charlist, List), length(Charlist, Len).

solution_le(_, 'nu exista solutie', 0).
solution_le(L, Word, X):- X>0, solution(L, Word, X).
solution_le(L, Word, X):- X>0, not(solution(L, Word, X)), M is X-1, solution_le(L, Word, M).

top_word(L, Word):- length(L, N), solution_le(L, Word, N).
