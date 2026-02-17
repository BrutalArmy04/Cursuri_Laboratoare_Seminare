{-
# Laborator 3 - Liste

## Elemente de limbaj și Importuri
-}
import Data.Char (isDigit, digitToInt)
import Data.List (delete) 
-- Am eliminat importurile Text.XHtml și Data.IntMap deoarece nu sunt necesare 
-- pentru acest laborator și pot cauza erori dacă bibliotecile nu sunt instalate.

{-
1. Implementați următoarele funcții folosind liste:

a) `verifL` - verifică dacă lungimea unei liste date ca parametru este pară.
-}
verifL :: [Int] -> Bool
verifL l = 
    if (length l `mod` 2 == 0)
        then True
        else False

{-
b) `takefinal` - pentru o listă `l` și un număr `n`, întoarce ultimele `n` elemente.
-}
takefinal :: [a] -> Int -> [a]
takefinal l n = 
    if length l < n
        then l
        else drop (length l - n) l

{-
c) `remove` - șterge elementul de pe poziția `n`.
-}
remove :: [Int] -> Int -> [Int]
remove l n = take (n-1) l ++ drop n l 

{-
2. Recursivitate și liste

a) `myreplicate` - întoarce lista ce conține `n` elemente egale cu `v`.
-}
myreplicate :: Int -> Int -> [Int]
-- Corecție: [1, n] creează o listă cu 2 elemente. Corect este [1..n]
myreplicate n v = [v | _ <- [1..n]]

{-
b) `sumImp` - suma elementelor impare.
-}
sumImp :: [Int] -> Int
sumImp [] = 0
sumImp (h:t) = 
    if h `mod` 2 == 0
        then sumImp t
        else h + sumImp t

{-
c) `totalLen` - suma lungimilor șirurilor care încep cu 'A'.
-}
totalLen :: [String] -> Int
totalLen [] = 0
totalLen (h:t) = 
    if head h == 'A'
        then length h + totalLen t
        else totalLen t

{-
3. `nrVocale` - numărul total de vocale din șirurile palindrom.
-}
vocale :: String -> Int
vocale [] = 0
vocale (h:t) = 
    if h `elem` "aeiouAEIOU"
        then 1 + vocale t
        else vocale t

nrVocale :: [String] -> Int
nrVocale [] = 0
nrVocale (h:t) = 
    if h == reverse h
        then vocale h + nrVocale t
        else nrVocale t

{-
4. Funcție care adaugă numărul dat după fiecare element *par* din listă.
Corecție: Codul inițial adăuga după orice element. Am adăugat condiția `even`.
-}
f :: Int -> [Int] -> [Int]
f _ [] = []
f n (h:t) = 
    if even h 
        then h : n : f n t 
        else h : f n t

{-
5. `divizori` - lista divizorilor unui număr.
-}
divizori :: Int -> [Int]
divizori a = [x | x <- [1..a], a `mod` x == 0]

{-
6. `listadiv` - lista listelor de divizori.
Corecție: Codul inițial concatena totul într-o singură listă. 
Cerința cere [[Int]], deci folosim `:` (cons) în loc de `++`.
-}
listadiv :: [Int] -> [[Int]]
listadiv [] = []
listadiv (h:t) = divizori h : listadiv t

{-
7. `inInterval` - numerele din listă ce aparțin intervalului [a, b].
-}

-- a) Varianta Recursivă
inIntervalRec :: Int -> Int -> [Int] -> [Int]
inIntervalRec _ _ [] = []
inIntervalRec a b (h:t)
    | h >= a && h <= b = h : inIntervalRec a b t
    | otherwise        = inIntervalRec a b t

-- b) Varianta List Comprehension (Comp)
inIntervalComp :: Int -> Int -> [Int] -> [Int]
inIntervalComp a b l = [x | x <- l, x >= a && x <= b]

{-
8. `pozitive` - numără câte numere strict pozitive sunt într-o listă.
-}

-- a) Varianta Recursivă
pozitiveRec :: (Ord a, Num a) => [a] -> Int
pozitiveRec [] = 0
pozitiveRec (h:t) =
    if h > 0
        then 1 + pozitiveRec t
        else pozitiveRec t

-- b) Varianta List Comprehension
pozitiveComp :: (Ord a, Num a) => [a] -> Int
pozitiveComp l = length [x | x <- l, x > 0]

{-
9. `pozitiiImpare` - lista pozițiilor elementelor impare.
-}

-- a) Varianta Recursivă
pozitiiImpareRec :: [Int] -> [Int]
pozitiiImpareRec l = pozitiiImpareAux l 0
  where
    pozitiiImpareAux [] _ = []
    pozitiiImpareAux (h:t) i =
      if odd h
        then i : pozitiiImpareAux t (i + 1)
        else pozitiiImpareAux t (i + 1)

-- b) Varianta List Comprehension
-- Corecție: Sintaxa `l zip ...` era greșită. Corect: `zip l [0..]`
pozitiiImpareComp :: [Int] -> [Int]
pozitiiImpareComp l = [i | (x, i) <- zip l [0..], odd x]

{-
10. `multDigits` - produsul cifrelor dintr-un șir.
-}

-- a) Varianta Recursivă
-- Corecție: Folosim isDigit și digitToInt pentru a evita hardcodarea cazurilor '0'..'9'.
multiDigitsRec :: String -> Int
multiDigitsRec [] = 1
multiDigitsRec (h:t)
    | isDigit h = digitToInt h * multiDigitsRec t
    | otherwise = multiDigitsRec t

-- b) Varianta List Comprehension
multDigitsComp :: String -> Int
multDigitsComp s = product [digitToInt c | c <- s, isDigit c]

{-
## Extra (11-14)
-}

-- 11. Permutări
permutari :: Eq a => [a] -> [[a]]
permutari [] = [[]]
permutari xs = [x : ps | x <- xs, ps <- permutari (delete x xs)]

-- 12. Combinări
combinari :: [a] -> Int -> [[a]]
combinari _ 0 = [[]]
combinari [] _ = []
combinari (x:xs) k = 
    [x : ys | ys <- combinari xs (k-1)] ++ combinari xs k

-- 13. Aranjamente
aranjamente :: Eq a => [a] -> Int -> [[a]]
aranjamente l k = concat [permutari x | x <- combinari l k]

-- 14. N-Regine (Backtracking)
merge :: (Int, Int) -> [(Int, Int)] -> Bool
merge (l, c) regine = all (\(la, ca) -> l /= la && c /= ca && abs (l - la) /= abs (c - ca)) regine

nReg :: Int -> Int -> [[(Int, Int)]]
nReg n k = add k []
  where
    add 0 regine = [regine]
    add num regine = concat [ add (num - 1) ((l, c) : regine) | l <- [1..n], c <- [1..n], merge (l, c) regine ]