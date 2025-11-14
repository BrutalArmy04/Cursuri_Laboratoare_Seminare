% P01 (*): Find the last element of a list

% my_last(X,L) :- X is the last element of the list L
%    (element,list) (?,?)

% Note: last(?Elem, ?List) is predefined

my_last(X,[X]).
my_last(X,[_|L]) :- my_last(X,L).

% P02 (*): Find the last but one element of a list

% last_but_one(X,L) :- X is the last but one element of the list L
%    (element,list) (?,?)

last_but_one(X,[X,_]).
last_but_one(X,[_,Y|Ys]) :- last_but_one(X,[Y|Ys]).

% P03 (*): Find the K'th element of a list.
% The first element in the list is number 1.

% element_at(X,L,K) :- X is the K'th element of the list L
%    (element,list,integer) (?,?,+)

% Note: nth1(?Index, ?List, ?Elem) is predefined

element_at(X,[X|_],1).
element_at(X,[_|L],K) :- K > 1, K1 is K - 1, element_at(X,L,K1).

% P04 (*): Find the number of elements of a list.

% my_length(L,N) :- the list L contains N elements
%    (list,integer) (+,?) 

% Note: length(?List, ?Int) is predefined

my_length([],0).
my_length([_|L],N) :- my_length(L,N1), N is N1 + 1.

% P05 (*): Reverse a list.

% my_reverse(L1,L2) :- L2 is the list obtained from L1 by reversing 
%    the order of the elements.
%    (list,list) (?,?)

% Note: reverse(+List1, -List2) is predefined

my_reverse(L1,L2) :- my_rev(L1,L2,[]).

my_rev([],L2,L2) :- !.
my_rev([X|Xs],L2,Acc) :- my_rev(Xs,L2,[X|Acc]).

% P06 (*): Find out whether a list is a palindrome
% A palindrome can be read forward or backward; e.g. [x,a,m,a,x]

% is_palindrome(L) :- L is a palindrome list
%    (list) (?)

is_palindrome(L) :- reverse(L,L).

% P07 (**): Flatten a nested list structure.

% my_flatten(L1,L2) :- the list L2 is obtained from the list L1 by
%    flattening; i.e. if an element of L1 is a list then it is replaced
%    by its elements, recursively. 
%    (list,list) (+,?)

% Note: flatten(+List1, -List2) is a predefined predicate

my_flatten(X,[X]) :- \+ is_list(X).
my_flatten([],[]).
my_flatten([X|Xs],Zs) :- my_flatten(X,Y), my_flatten(Xs,Ys), append(Y,Ys,Zs).

% P08 (**): Eliminate consecutive duplicates of list elements.

% compress(L1,L2) :- the list L2 is obtained from the list L1 by
%    compressing repeated occurrences of elements into a single copy
%    of the element.
%    (list,list) (+,?)

compress([],[]).
compress([X],[X]).
compress([X,X|Xs],Zs) :- compress([X|Xs],Zs).
compress([X,Y|Ys],[X|Zs]) :- X \= Y, compress([Y|Ys],Zs).

% P09 (**):  Pack consecutive duplicates of list elements into sublists.

% pack(L1,L2) :- the list L2 is obtained from the list L1 by packing
%    repeated occurrences of elements into separate sublists.
%    (list,list) (+,?)

pack([],[]).
pack([X|Xs],[Z|Zs]) :- transfer(X,Xs,Ys,Z), pack(Ys,Zs).

% transfer(X,Xs,Ys,Z) Ys is the list that remains from the list Xs
%    when all leading copies of X are removed and transfered to Z

transfer(X,[],[],[X]).
transfer(X,[Y|Ys],[Y|Ys],[X]) :- X \= Y.
transfer(X,[X|Xs],Ys,[X|Zs]) :- transfer(X,Xs,Ys,Zs).

% P10 (*):  Run-length encoding of a list

% encode(L1,L2) :- the list L2 is obtained from the list L1 by run-length
%    encoding. Consecutive duplicates of elements are encoded as terms [N,E],
%    where N is the number of duplicates of the element E.
%    (list,list) (+,?)

:- ensure_loaded(p09).

encode(L1,L2) :- pack(L1,L), transform(L,L2).

transform([],[]).
transform([[X|Xs]|Ys],[[N,X]|Zs]) :- length([X|Xs],N), transform(Ys,Zs).

% P11 (*):  Modified run-length encoding

% encode_modified(L1,L2) :- the list L2 is obtained from the list L1 by 
%    run-length encoding. Consecutive duplicates of elements are encoded 
%    as terms [N,E], where N is the number of duplicates of the element E.
%    However, if N equals 1 then the element is simply copied into the 
%    output list.
%    (list,list) (+,?)

:- ensure_loaded(p10).

encode_modified(L1,L2) :- encode(L1,L), strip(L,L2).

strip([],[]).
strip([[1,X]|Ys],[X|Zs]) :- strip(Ys,Zs).
strip([[N,X]|Ys],[[N,X]|Zs]) :- N > 1, strip(Ys,Zs).

% P12 (**): Decode a run-length compressed list.

% decode(L1,L2) :- L2 is the uncompressed version of the run-length
%    encoded list L1.
%    (list,list) (+,?)

decode([],[]).
decode([X|Ys],[X|Zs]) :- \+ is_list(X), decode(Ys,Zs).
decode([[1,X]|Ys],[X|Zs]) :- decode(Ys,Zs).
decode([[N,X]|Ys],[X|Zs]) :- N > 1, N1 is N - 1, decode([[N1,X]|Ys],Zs).

% P13 (**): Run-length encoding of a list (direct solution) 

% encode_direct(L1,L2) :- the list L2 is obtained from the list L1 by 
%    run-length encoding. Consecutive duplicates of elements are encoded 
%    as terms [N,E], where N is the number of duplicates of the element E.
%    However, if N equals 1 then the element is simply copied into the 
%    output list.
%    (list,list) (+,?)

encode_direct([],[]).
encode_direct([X|Xs],[Z|Zs]) :- count(X,Xs,Ys,1,Z), encode_direct(Ys,Zs).

% count(X,Xs,Ys,K,T) Ys is the list that remains from the list Xs
%    when all leading copies of X are removed. T is the term [N,X],
%    where N is K plus the number of X's that can be removed from Xs.
%    In the case of N=1, T is X, instead of the term [1,X].

count(X,[],[],1,X).
count(X,[],[],N,[N,X]) :- N > 1.
count(X,[Y|Ys],[Y|Ys],1,X) :- X \= Y.
count(X,[Y|Ys],[Y|Ys],N,[N,X]) :- N > 1, X \= Y.
count(X,[X|Xs],Ys,K,T) :- K1 is K + 1, count(X,Xs,Ys,K1,T).

% P14 (*): Duplicate the elements of a list

% dupli(L1,L2) :- L2 is obtained from L1 by duplicating all elements.
%    (list,list) (?,?)

dupli([],[]).
dupli([X|Xs],[X,X|Ys]) :- dupli(Xs,Ys).

% P15 (**): Duplicate the elements of a list agiven number of times

% dupli(L1,N,L2) :- L2 is obtained from L1 by duplicating all elements
%    N times.
%    (list,integer,list) (?,+,?)

dupli(L1,N,L2) :- dupli(L1,N,L2,N).

% dupli(L1,N,L2,K) :- L2 is obtained from L1 by duplicating its leading
%    element K times, all other elements N times.
%    (list,integer,list,integer) (?,+,?,+)

dupli([],_,[],_).
dupli([_|Xs],N,Ys,0) :- dupli(Xs,N,Ys,N).
dupli([X|Xs],N,[X|Ys],K) :- K > 0, K1 is K - 1, dupli([X|Xs],N,Ys,K1).

% P16 (**):  Drop every N'th element from a list

% drop(L1,N,L2) :- L2 is obtained from L1 by dropping every N'th element.
%    (list,integer,list) (?,+,?)

drop(L1,N,L2) :- drop(L1,N,L2,N).

% drop(L1,N,L2,K) :- L2 is obtained from L1 by first copying K-1 elements
%    and then dropping an element and, from then on, dropping every
%    N'th element.
%    (list,integer,list,integer) (?,+,?,+)

drop([],_,[],_).
drop([_|Xs],N,Ys,1) :- drop(Xs,N,Ys,N).
drop([X|Xs],N,[X|Ys],K) :- K > 1, K1 is K - 1, drop(Xs,N,Ys,K1).

% P17 (*): Split a list into two parts

% split(L,N,L1,L2) :- the list L1 contains the first N elements
%    of the list L, the list L2 contains the remaining elements.
%    (list,integer,list,list) (?,+,?,?)

split(L,0,[],L).
split([X|Xs],N,[X|Ys],Zs) :- N > 0, N1 is N - 1, split(Xs,N1,Ys,Zs).

% P18 (**):  Extract a slice from a list

% slice(L1,I,K,L2) :- L2 is the list of the elements of L1 between
%    index I and index K (both included).
%    (list,integer,integer,list) (?,+,+,?)

slice([X|_],1,1,[X]).
slice([X|Xs],1,K,[X|Ys]) :- K > 1, 
   K1 is K - 1, slice(Xs,1,K1,Ys).
slice([_|Xs],I,K,Ys) :- I > 1, 
   I1 is I - 1, K1 is K - 1, slice(Xs,I1,K1,Ys).

% P19 (**): Rotate a list N places to the left 

% rotate(L1,N,L2) :- the list L2 is obtained from the list L1 by 
%    rotating the elements of L1 N places to the left.
%    Examples: 
%    rotate([a,b,c,d,e,f,g,h],3,[d,e,f,g,h,a,b,c])
%    rotate([a,b,c,d,e,f,g,h],-2,[g,h,a,b,c,d,e,f])
%    (list,integer,list) (+,+,?)

:- ensure_loaded(p17).

rotate(L1,N,L2) :- N >= 0, 
   length(L1,NL1), N1 is N mod NL1, rotate_left(L1,N1,L2).
rotate(L1,N,L2) :- N < 0,
   length(L1,NL1), N1 is NL1 + (N mod NL1), rotate_left(L1,N1,L2).

rotate_left(L,0,L).
rotate_left(L1,N,L2) :- N > 0, split(L1,N,S1,S2), append(S2,S1,L2).

% P20 (*): Remove the K'th element from a list.
% The first element in the list is number 1.

% remove_at(X,L,K,R) :- X is the K'th element of the list L; R is the
%    list that remains when the K'th element is removed from L.
%    (element,list,integer,list) (?,?,+,?)

remove_at(X,[X|Xs],1,Xs).
remove_at(X,[Y|Xs],K,[Y|Ys]) :- K > 1, 
   K1 is K - 1, remove_at(X,Xs,K1,Ys).

% P21 (*): Insert an element at a given position into a list
% The first element in the list is number 1.

% insert_at(X,L,K,R) :- X is inserted into the list L such that it
%    occupies position K. The result is the list R.
%    (element,list,integer,list) (?,?,+,?)

:- ensure_loaded(p20).

insert_at(X,L,K,R) :- remove_at(X,R,K,L).

% P22 (*):  Create a list containing all integers within a given range.

% range(I,K,L) :- I <= K, and L is the list containing all 
%    consecutive integers from I to K.
%    (integer,integer,list) (+,+,?)

range(I,I,[I]).
range(I,K,[I|L]) :- I < K, I1 is I + 1, range(I1,K,L).

% P23 (**): Extract a given number of randomly selected elements 
%    from a list.

% rnd_select(L,N,R) :- the list R contains N randomly selected 
%    items taken from the list L.
%    (list,integer,list) (+,+,-)

:- ensure_loaded(p20).

rnd_select(_,0,[]).
rnd_select(Xs,N,[X|Zs]) :- N > 0,
    length(Xs,L),
    I is random(L) + 1,
    remove_at(X,Xs,I,Ys),
    N1 is N - 1,
    rnd_select(Ys,N1,Zs).

% P24 (*): Lotto: Draw N different random numbers from the set 1..M

% lotto(N,M,L) :- the list L contains N randomly selected distinct
%    integer numbers from the interval 1..M
%    (integer,integer,number-list) (+,+,-)

:- ensure_loaded(p22).
:- ensure_loaded(p23).

lotto(N,M,L) :- range(1,M,R), rnd_select(R,N,L).

% P25 (*):  Generate a random permutation of the elements of a list

% rnd_permu(L1,L2) :- the list L2 is a random permutation of the
%    elements of the list L1.
%    (list,list) (+,-)

:- ensure_loaded(p23).

rnd_permu(L1,L2) :- length(L1,N), rnd_select(L1,N,L2).

% P26 (**):  Generate the combinations of k distinct objects
%            chosen from the n elements of a list.

% combination(K,L,C) :- C is a list of K distinct elements 
%    chosen from the list L

combination(0,_,[]).
combination(K,L,[X|Xs]) :- K > 0,
   el(X,L,R), K1 is K-1, combination(K1,R,Xs).

% Find out what the following predicate el/3 exactly does.

el(X,[X|L],L).
el(X,[_|L],R) :- el(X,L,R).

% P27 (**) Group the elements of a set into disjoint subsets.

% Problem a)

% group3(G,G1,G2,G3) :- distribute the 9 elements of G into G1, G2, and G3,
%    such that G1, G2 and G3 contain 2,3 and 4 elements respectively

group3(G,G1,G2,G3) :- 
   selectN(2,G,G1),
   subtract(G,G1,R1),
   selectN(3,R1,G2),
   subtract(R1,G2,R2),
   selectN(4,R2,G3),
   subtract(R2,G3,[]).

% selectN(N,L,S) :- select N elements of the list L and put them in 
%    the set S. Via backtracking return all posssible selections, but
%    avoid permutations; i.e. after generating S = [a,b,c] do not return
%    S = [b,a,c], etc.

selectN(0,_,[]) :- !.
selectN(N,L,[X|S]) :- N > 0, 
   el(X,L,R), 
   N1 is N-1,
   selectN(N1,R,S).

el(X,[X|L],L).
el(X,[_|L],R) :- el(X,L,R).

% subtract/3 is predefined

% Problem b): Generalization

% group(G,Ns,Gs) :- distribute the elements of G into the groups Gs.
%    The group sizes are given in the list Ns.

group([],[],[]).
group(G,[N1|Ns],[G1|Gs]) :- 
   selectN(N1,G,G1),
   subtract(G,G1,R),
   group(R,Ns,Gs).

% P28 (**) Sorting a list of lists according to length
%
% a) length sort
%
% lsort(InList,OutList) :- it is supposed that the elements of InList 
% are lists themselves. Then OutList is obtained from InList by sorting 
% its elements according to their length. lsort/2 sorts ascendingly,
% lsort/3 allows for ascending or descending sorts.
% (list_of_lists,list_of_lists), (+,?)

lsort(InList,OutList) :- lsort(InList,OutList,asc).

% sorting direction Dir is either asc or desc

lsort(InList,OutList,Dir) :-
   add_key(InList,KList,Dir),
   keysort(KList,SKList),
   rem_key(SKList,OutList).

add_key([],[],_).
add_key([X|Xs],[L-p(X)|Ys],asc) :- !, 
	length(X,L), add_key(Xs,Ys,asc).
add_key([X|Xs],[L-p(X)|Ys],desc) :- 
	length(X,L1), L is -L1, add_key(Xs,Ys,desc).

rem_key([],[]).
rem_key([_-p(X)|Xs],[X|Ys]) :- rem_key(Xs,Ys).

% b) length frequency sort
%
% lfsort (InList,OutList) :- it is supposed that the elements of InList
% are lists themselves. Then OutList is obtained from InList by sorting
% its elements according to their length frequency; i.e. in the default,
% where sorting is done ascendingly, lists with rare lengths are placed
% first, other with more frequent lengths come later.
%
% Example:
% ?- lfsort([[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],L).
% L = [[i, j, k, l], [o], [a, b, c], [f, g, h], [d, e], [d, e], [m, n]]
%
% Note that the first two lists in the Result have length 4 and 1, both
% length appear just once. The third and forth list have length 3 which
% appears, there are two list of this length. And finally, the last
% three lists have length 2. This is the most frequent length.

lfsort(InList,OutList) :- lfsort(InList,OutList,asc).

% sorting direction Dir is either asc or desc

lfsort(InList,OutList,Dir) :-
	add_key(InList,KList,desc),
   keysort(KList,SKList),
   pack(SKList,PKList),
   lsort(PKList,SPKList,Dir),
   flatten(SPKList,FKList),
   rem_key(FKList,OutList).
   
pack([],[]).
pack([L-X|Xs],[[L-X|Z]|Zs]) :- transf(L-X,Xs,Ys,Z), pack(Ys,Zs).

% transf(L-X,Xs,Ys,Z) Ys is the list that remains from the list Xs
%    when all leading copies of length L are removed and transfed to Z

transf(_,[],[],[]).
transf(L-_,[K-Y|Ys],[K-Y|Ys],[]) :- L \= K.
transf(L-_,[L-X|Xs],Ys,[L-X|Zs]) :- transf(L-X,Xs,Ys,Zs).

test :-
   L = [[a,b,c],[d,e],[f,g,h],[d,e],[i,j,k,l],[m,n],[o]],
   write('L = '), write(L), nl,
   lsort(L,LS),
   write('LS = '), write(LS), nl,
   lsort(L,LSD,desc),
   write('LSD = '), write(LSD), nl,
   lfsort(L,LFS),
   write('LFS = '), write(LFS), nl.

% P31 (**) Determine whether a given integer number is prime. 

% is_prime(P) :- P is a prime number
%    (integer) (+)

is_prime(2).
is_prime(3).
is_prime(P) :- integer(P), P > 3, P mod 2 =\= 0, \+ has_factor(P,3).  

% has_factor(N,L) :- N has an odd factor F >= L.
%    (integer, integer) (+,+)

has_factor(N,L) :- N mod L =:= 0.
has_factor(N,L) :- L * L < N, L2 is L + 2, has_factor(N,L2).

% P32 (**) Determine the greatest common divisor of two positive integers.

% gcd(X,Y,G) :- G is the greatest common divisor of X and Y
%    (integer, integer, integer) (+,+,?)


gcd(X,0,X) :- X > 0.
gcd(X,Y,G) :- Y > 0, Z is X mod Y, gcd(Y,Z,G).


% Declare gcd as an arithmetic function; so you can use it
% like this:  ?- G is gcd(36,63).

:- arithmetic_function(gcd/2).

% P33 (*) Determine whether two positive integer numbers are coprime. 
%     Two numbers are coprime if their greatest common divisor equals 1.

% coprime(X,Y) :- X and Y are coprime.
%    (integer, integer) (+,+)

:- ensure_loaded(p32).

coprime(X,Y) :- gcd(X,Y,1).

% P34 (**) Calculate Euler's totient function phi(m). 
%    Euler's so-called totient function phi(m) is defined as the number 
%    of positive integers r (1 <= r < m) that are coprime to m. 
%    Example: m = 10: r = 1,3,7,9; thus phi(m) = 4. Note: phi(1) = 1.

% totient_phi(M,Phi) :- Phi is the value of the Euler's totient function
%    phi for the argument M.
%    (integer, integer) (+,-)

:- ensure_loaded(p33).
:- arithmetic_function(totient_phi/1).

totient_phi(1,1) :- !.
totient_phi(M,Phi) :- t_phi(M,Phi,1,0).

% t_phi(M,Phi,K,C) :- Phi = C + N, where N is the number of integers R
%    such that K <= R < M and R is coprime to M.
%    (integer,integer,integer,integer) (+,-,+,+)

t_phi(M,Phi,M,Phi) :- !.
t_phi(M,Phi,K,C) :- 
   K < M, coprime(K,M), !, 
   C1 is C + 1, K1 is K + 1,
   t_phi(M,Phi,K1,C1).
t_phi(M,Phi,K,C) :- 
   K < M, K1 is K + 1,
   t_phi(M,Phi,K1,C).

% P35 (**) Determine the prime factors of a given positive integer. 

% prime_factors(N, L) :- N is the list of prime factors of N.
%    (integer,list) (+,?)

prime_factors(N,L) :- N > 0,  prime_factors(N,L,2).

% prime_factors(N,L,K) :- L is the list of prime factors of N. It is 
% known that N does not have any prime factors less than K.

prime_factors(1,[],_) :- !.
prime_factors(N,[F|L],F) :-                           % N is multiple of F
   R is N // F, N =:= R * F, !, prime_factors(R,L,F).
prime_factors(N,L,F) :- 
   next_factor(N,F,NF), prime_factors(N,L,NF).        % N is not multiple of F
   

% next_factor(N,F,NF) :- when calculating the prime factors of N
%    and if F does not divide N then NF is the next larger candidate to
%    be a factor of N.

next_factor(_,2,3) :- !.
next_factor(N,F,NF) :- F * F < N, !, NF is F + 2.
next_factor(N,_,N).                                 % F > sqrt(N)

% P36 (**) Determine the prime factors of a given positive integer (2). 
% Construct a list containing the prime factors and their multiplicity.
% Example: 
% ?- prime_factors_mult(315, L).
% L = [[3,2],[5,1],[7,1]]

:- ensure_loaded(p35).  % make sure next_factor/3 is loaded

% prime_factors_mult(N, L) :- L is the list of prime factors of N. It is
%    composed of terms [F,M] where F is a prime factor and M its multiplicity.
%    (integer,list) (+,?)

prime_factors_mult(N,L) :- N > 0, prime_factors_mult(N,L,2).

% prime_factors_mult(N,L,K) :- L is the list of prime factors of N. It is 
% known that N does not have any prime factors less than K.

prime_factors_mult(1,[],_) :- !.
prime_factors_mult(N,[[F,M]|L],F) :- divide(N,F,M,R), !, % F divides N
   next_factor(R,F,NF), prime_factors_mult(R,L,NF).
prime_factors_mult(N,L,F) :- !,                          % F does not divide N
   next_factor(N,F,NF), prime_factors_mult(N,L,NF).

% divide(N,F,M,R) :- N = R * F**M, M >= 1, and F is not a factor of R. 
%    (integer,integer,integer,integer) (+,+,-,-)

divide(N,F,M,R) :- divi(N,F,M,R,0), M > 0.

divi(N,F,M,R,K) :- S is N // F, N =:= S * F, !,          % F divides N
   K1 is K + 1, divi(S,F,M,R,K1).
divi(N,_,M,N,M).

% P37 (**) Calculate Euler's totient function phi(m) (improved). 
% See problem P34 for the definition of Euler's totient function. 
% If the list of the prime factors of a number m is known in the 
% form of problem P36 then the function phi(m) can be efficiently
% calculated as follows: 
%
% Let [[p1,m1],[p2,m2],[p3,m3],...] be the list of prime factors (and their
% multiplicities) of a given number m. Then phi(m) can be calculated 
% with the following formula:
%
% phi(m) = (p1 - 1) * p1 ** (m1 - 1) * (p2 - 1) * p2 ** (m2 - 1) * 
%          (p3 - 1) * p3 ** (m3 - 1) * ...
%
% Note that a ** b stands for the b'th power of a.

:- ensure_loaded(p36).

% totient_phi_2(N,Phi) :- Phi is the value of Euler's totient function
%    for the argument N.
%    (integer,integer) (+,?)

totient_phi_2(N,Phi) :- prime_factors_mult(N,L), to_phi(L,Phi).

to_phi([],1).
to_phi([[F,1]|L],Phi) :- !,
   to_phi(L,Phi1), Phi is Phi1 * (F - 1).
to_phi([[F,M]|L],Phi) :- M > 1,
   M1 is M - 1, to_phi([[F,M1]|L],Phi1), Phi is Phi1 * F.

% P38 (*) Compare the two methods of calculating Euler's totient function. 
% Use the solutions of problems P34 and P37 to compare the algorithms. 
% Take the number of logical inferences as a measure for efficiency.

:- ensure_loaded(p34).
:- ensure_loaded(p37).

totient_test(N) :-
   write('totient_phi (P34):'),
   time(totient_phi(N,Phi1)),
   write('result = '), write(Phi1), nl,
   write('totient_phi_2 (P37):'),
   time(totient_phi_2(N,Phi2)),
   write('result = '), write(Phi2), nl.

% P39 (*) A list of prime numbers. 
% Given a range of integers by its lower and upper limit, construct a 
% list of all prime numbers in that range.

:- ensure_loaded(p31).   % make sure is_prime/1 is loaded

% prime_list(A,B,L) :- L is the list of prime number P with A <= P <= B

prime_list(A,B,L) :- A =< 2, !, p_list(2,B,L).
prime_list(A,B,L) :- A1 is (A // 2) * 2 + 1, p_list(A1,B,L).

p_list(A,B,[]) :- A > B, !.
p_list(A,B,[A|L]) :- is_prime(A), !, 
   next(A,A1), p_list(A1,B,L). 
p_list(A,B,L) :- 
   next(A,A1), p_list(A1,B,L).

next(2,3) :- !.
next(A,A1) :- A1 is A + 2.

% P40 (**) Goldbach's conjecture. 
% Goldbach's conjecture says that every positive even number greater 
% than 2 is the sum of two prime numbers. Example: 28 = 5 + 23.

:- ensure_loaded(p31).

% goldbach(N,L) :- L is the list of the two prime numbers that
%    sum up to the given N (which must be even).
%    (integer,integer) (+,-)

goldbach(4,[2,2]) :- !.
goldbach(N,L) :- N mod 2 =:= 0, N > 4, goldbach(N,L,3).

goldbach(N,[P,Q],P) :- Q is N - P, is_prime(Q), !.
goldbach(N,L,P) :- P < N, next_prime(P,P1), goldbach(N,L,P1).

next_prime(P,P1) :- P1 is P + 2, is_prime(P1), !.
next_prime(P,P1) :- P2 is P + 2, next_prime(P2,P1).

% P41 (*) A list of Goldbach compositions. 
% Given a range of integers by its lower and upper limit, 
% print a list of all even numbers and their Goldbach composition.

:- ensure_loaded(p40).

% goldbach_list(A,B) :- print a list of the Goldbach composition
%    of all even numbers N in the range A <= N <= B
%    (integer,integer) (+,+)

goldbach_list(A,B) :- goldbach_list(A,B,2).

% goldbach_list(A,B,L) :- perform goldbach_list(A,B), but suppress
% all output when the first prime number is less than the limit L.

goldbach_list(A,B,L) :- A =< 4, !, g_list(4,B,L).
goldbach_list(A,B,L) :- A1 is ((A+1) // 2) * 2, g_list(A1,B,L).

g_list(A,B,_) :- A > B, !.
g_list(A,B,L) :- 
   goldbach(A,[P,Q]),
   print_goldbach(A,P,Q,L),
   A2 is A + 2,
   g_list(A2,B,L).

print_goldbach(A,P,Q,L) :- P >= L, !,
   writef('%t = %t + %t',[A,P,Q]), nl.
print_goldbach(_,_,_,_).

% P46 (**) Truth tables for logical expressions.
% Define predicates and/2, or/2, nand/2, nor/2, xor/2, impl/2 
% and equ/2 (for logical equivalence) which succeed or
% fail according to the result of their respective operations; e.g.
% and(A,B) will succeed, if and only if both A and B succeed.
% Note that A and B can be Prolog goals (not only the constants
% true and fail).
% A logical expression in two variables can then be written in 
% prefix notation, as in the following example: and(or(A,B),nand(A,B)).
%
% Now, write a predicate table/3 which prints the truth table of a
% given logical expression in two variables.
%
% Example:
% ?- table(A,B,and(A,or(A,B))).
% true  true  true
% true  fail  true
% fail  true  fail
% fail  fail  fail
    
and(A,B) :- A, B.

or(A,_) :- A.
or(_,B) :- B.

equ(A,B) :- or(and(A,B), and(not(A),not(B))).

xor(A,B) :- not(equ(A,B)).

nor(A,B) :- not(or(A,B)).

nand(A,B) :- not(and(A,B)).

impl(A,B) :- or(not(A),B).

% bind(X) :- instantiate X to be true and false successively

bind(true).
bind(fail).

table(A,B,Expr) :- bind(A), bind(B), do(A,B,Expr), fail.

do(A,B,_) :- write(A), write('  '), write(B), write('  '), fail.
do(_,_,Expr) :- Expr, !, write(true), nl.
do(_,_,_) :- write(fail), nl.

% P47 (*) Truth tables for logical expressions (2).
% Continue problem P46 by defining and/2, or/2, etc as being
% operators. This allows to write the logical expression in the
% more natural way, as in the example: A and (A or not B).
% Define operator precedence as usual; i.e. as in Java.
%
% Example:
% ?- table(A,B, A and (A or not B)).
% true  true  true
% true  fail  true
% fail  true  fail
% fail  fail  fail
    
:- ensure_loaded(p46).

:- op(900, fy,not).
:- op(910, yfx, and).
:- op(910, yfx, nand).
:- op(920, yfx, or).
:- op(920, yfx, nor).
:- op(930, yfx, impl).
:- op(930, yfx, equ).
:- op(930, yfx, xor).

% I.e. not binds stronger than (and, nand), which bind stronger than
% (or,nor) which in turn bind stronger than implication, equivalence
% and xor.

% P48 (**) Truth tables for logical expressions (3).
% Generalize problem P47 in such a way that the logical
% expression may contain any number of logical variables.
%
% Example:
% ?- table([A,B,C], A and (B or C) equ A and B or A and C).
% true  true  true  true
% true  true  fail  true
% true  fail  true  true
% true  fail  fail  true
% fail  true  true  true
% fail  true  fail  true
% fail  fail  true  true
% fail  fail  fail  true

:- ensure_loaded(p47).    

% table(List,Expr) :- print the truth table for the expression Expr,
%   which contains the logical variables enumerated in List.

table(VarList,Expr) :- bindList(VarList), do(VarList,Expr), fail.

bindList([]).
bindList([V|Vs]) :- bind(V), bindList(Vs).

do(VarList,Expr) :- writeVarList(VarList), writeExpr(Expr), nl.

writeVarList([]).
writeVarList([V|Vs]) :- write(V), write('  '), writeVarList(Vs).

writeExpr(Expr) :- Expr, !, write(true).
writeExpr(_) :- write(fail).

% (**) P49 Gray codes

% gray(N,C) :- C is the N-bit Gray code

gray(1,['0','1']).
gray(N,C) :- N > 1, N1 is N-1,
   gray(N1,C1), reverse(C1,C2),
   prepend('0',C1,C1P),
   prepend('1',C2,C2P),
   append(C1P,C2P,C).

prepend(_,[],[]) :- !.
prepend(X,[C|Cs],[CP|CPs]) :- atom_concat(X,C,CP), prepend(X,Cs,CPs).


% This gives a nice example for the result caching technique:

:- dynamic gray_c/2.

gray_c(1,['0','1']) :- !.
gray_c(N,C) :- N > 1, N1 is N-1, 
   gray_c(N1,C1), reverse(C1,C2),
   prepend('0',C1,C1P),
   prepend('1',C2,C2P),
   append(C1P,C2P,C),
   asserta((gray_c(N,C) :- !)).

% Try the following goal sequence and see what happens:

% ?- [p49]. 
% ?- listing(gray_c/2).
% ?- gray_c(5,C).
% ?- listing(gray_c/2).


% There is an alternative definition for the gray code construction:

gray_alt(1,['0','1']).
gray_alt(N,C) :- N > 1, N1 is N-1,
   gray_alt(N1,C1), 
   postpend(['0','1'],C1,C).   

postpend(_,[],[]).
postpend(P,[C|Cs],[C1P,C2P|CsP]) :- P = [P1,P2],
   atom_concat(C,P1,C1P), 
   atom_concat(C,P2,C2P),
   reverse(P,PR),
   postpend(PR,Cs,CsP).

% (***) P50 Huffman code

% We suppose a set of symbols with their frequencies, given as a list 
% of fr(S,F) terms. 
% Example: [fr(a,45),fr(b,13),fr(c,12),fr(d,16),fr(e,9),fr(f,5)]. 
% Our objective is to construct a list hc(S,C) terms, where C is the Huffman
% code word for the symbol S. In our example the result could be 
% [hc(a, '0'), hc(b, '101'), hc(c, '100'), hc(d, '111'), hc(e, '1101'), 
% hc(f, '1100')]  

% The task shall be performed by the predicate huffman/2 defined as follows: 
 
% huffman(Fs,Hs) :- Hs is the Huffman code table for the frequency table Fs
% (list-of-fr/2-terms, list-of-hc/2-terms)  (+,-).

% During the construction process, we need nodes n(F,S) where, at the 
% beginning, F is a frequency and S a symbol. During the process, as n(F,S)
% becomes an internal node, S becomes a term s(L,R) with L and R being 
% again n(F,S) terms. A list of n(F,S) terms, called Ns, is maintained 
% as a sort of priority queue.

huffman(Fs,Cs) :-
   initialize(Fs,Ns),
   make_tree(Ns,T),
   traverse_tree(T,Cs).

initialize(Fs,Ns) :- init(Fs,NsU), sort(NsU,Ns).

init([],[]).
init([fr(S,F)|Fs],[n(F,S)|Ns]) :- init(Fs,Ns).

make_tree([T],T).
make_tree([n(F1,X1),n(F2,X2)|Ns],T) :- 
   F is F1+F2,
   insert(n(F,s(n(F1,X1),n(F2,X2))),Ns,NsR),
   make_tree(NsR,T).

% insert(n(F,X),Ns,NsR) :- insert the node n(F,X) into Ns such that the
%    resulting list NsR is again sorted with respect to the frequency F.

insert(N,[],[N]) :- !.
insert(n(F,X),[n(F0,Y)|Ns],[n(F,X),n(F0,Y)|Ns]) :- F < F0, !.
insert(n(F,X),[n(F0,Y)|Ns],[n(F0,Y)|Ns1]) :- F >= F0, insert(n(F,X),Ns,Ns1).

% traverse_tree(T,Cs) :- traverse the tree T and construct the Huffman 
%    code table Cs,

traverse_tree(T,Cs) :- traverse_tree(T,'',Cs1-[]), sort(Cs1,Cs).

traverse_tree(n(_,A),Code,[hc(A,Code)|Cs]-Cs) :- atom(A). % leaf node
traverse_tree(n(_,s(Left,Right)),Code,Cs1-Cs3) :-         % internal node
   atom_concat(Code,'0',CodeLeft), 
   atom_concat(Code,'1',CodeRight),
   traverse_tree(Left,CodeLeft,Cs1-Cs2),
   traverse_tree(Right,CodeRight,Cs2-Cs3).


% The following predicate gives some statistical information.

huffman(Fs) :- huffman(Fs,Hs) , nl, report(Hs,5), stats(Fs,Hs).

report([],_) :- !, nl, nl.
report(Hs,0) :- !, nl, report(Hs,5).
report([hc(S,C)|Hs],N) :- N > 0, N1 is N-1, 
   writef('%w %8l  ',[S,C]), report(Hs,N1).

stats(Fs,Cs) :- sort(Fs,FsS), sort(Cs,CsS), stats(FsS,CsS,0,0).

stats([],[],FreqCodeSum,FreqSum) :- Avg is FreqCodeSum/FreqSum,
   writef('Average code length (weighted) = %w\n',[Avg]). 
stats([fr(S,F)|Fs],[hc(S,C)|Hs],FCS,FS) :- 
   atom_chars(C,CharList), length(CharList,N),
   FCS1 is FCS + F*N, FS1 is FS + F,
   stats(Fs,Hs,FCS1,FS1). 
   
