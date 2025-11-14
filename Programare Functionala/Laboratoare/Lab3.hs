import Text.XHtml (base)
import Data.IntMap
import Data.Char (ord, isDigit, digitToInt)
-- Ex 1

--a
verifL :: [Int] -> Bool
verifL l = 
    if ((length l `mod` 2) == 0)
        then True
        else False

--b

takefinal :: [Int] -> Int -> [Int]
takefinal l n = 
    if (length l < n)
        then l
        else drop((length l) - n) l

--c

remove :: [Int] -> Int -> [Int]
remove l n = take (n-1) l ++ drop n l -- concatenare

--Ex 2

--a

myreplicate :: Int -> Int -> [Int]
myreplicate n v = [v | x<-[1, n]]

--b

sumImp :: [Int] -> Int
sumImp [] = 0
sumImp (h:t) = 
    if (h `mod` 2 == 0)
        then sumImp t
    else h + sumImp t

--c

totalLen :: [String] -> Int
totalLen [] = 0
totalLen ((h1:t1):t) = 
    if (h1 == 'A')
        then length (h1:t1) + totalLen t
        else totalLen t

-- Ex 3


vocale :: String -> Int
vocale [] = 0
vocale (h:t) = 
    if (('a' `elem` [h])||('i' `elem` [h])||('e' `elem` [h])||('o' `elem` [h])||('u' `elem` [h]))
        then 1 + vocale t
        else vocale t


-- nrVocale ["sos", "civic", "palton", "desen", "aerisirea"] == 9
nrVocale :: [String] -> Int
nrVocale (h:t) = 
    if (h == reverse h)
        then vocale h + nrVocale t
        else nrVocale t


--Ex 4

f :: Int -> [Int] -> [Int]
f n [] = []
f a (h:t) = h : (a : f (a) t) 

    

--Ex 5

-- divizori 4 == [1,2,4]

divizori :: Int -> [Int]
divizori a = [x | x <-take a [1..], a `mod` x == 0]

--Ex 6

listadiv :: [Int] -> [Int]
listadiv [] = []
listadiv (h:t) = 
    let b = divizori h
    in b++listadiv(t)


--Ex 7

inInterval :: Int -> Int -> [Int] -> [Int]
inInterval a b l = [x | x<-l, x>=a && x<=b]

--Ex 8

--a
pozitiveRec :: (Ord a1, Num a2, Num a1) => [a1] -> a2
pozitiveRec []=0
pozitiveRec (h:t) =
    if h>0
        then 1+ pozitiveRec t
        else pozitiveRec t

--b
pozitiveComp :: (Ord a, Num a) => [a] -> Int
pozitiveComp l =  length [x | x <- l, x > 0]

--9
--a
pozitiiImpare :: (Integral a, Num t) => [a] -> [t]
pozitiiImpare l = pozitiiImpareAux l 0
  where
    pozitiiImpareAux [] _ = []
    pozitiiImpareAux (h:t) i =
      if odd h
        then i : pozitiiImpareAux t (i + 1)
        else pozitiiImpareAux t (i + 1)

--b
pozitiiImpareC :: (Integral a1, Num a2, Enum a2) => (([a3] -> [b] -> [(a3, b)]) -> [a2] -> [(a1, a4)]) -> [a4]
pozitiiImpareC l = [i | (x, i) <- l zip [0..], odd x]

--10
--a
multiDigitsRec :: Num a => [Char] -> a
multiDigitsRec []=1
multiDigitsRec (h:t)
    | h == '2' = 2 * multiDigitsRec t
    | h == '3' = 3 * multiDigitsRec t
    | h == '4' = 4 * multiDigitsRec t
    | h == '5' = 5 * multiDigitsRec t
    | h == '6' = 6 * multiDigitsRec t
    | h == '7' = 7 * multiDigitsRec t
    | h == '8' = 8 * multiDigitsRec t
    | h == '9' = 9 * multiDigitsRec t
    | h == '0' = 0
    | otherwise = multiDigitsRec t

--b


multDigitsComp :: String -> Int
multDigitsComp s = product [digitToInt c | c <- s, isDigit c]

--11
permutari :: Eq a => [a] -> [[a]]
permutari [] = [[]]
permutari xs = [x : ps | x <- xs, ps <- permutari (delete x xs)]
    where
        delete _ [] = []
        delete x (y:ys)
            |   x == y = ys
            |   otherwise = y : delete x ys

--12
combinari :: [a] -> Int -> [[a]]
combinari l k = [take k (drop i l) | i<-[0..((length l)-k)]]

--13
aranjamente :: Eq a => [a] -> Int -> [[a]]
aranjamente l k = concat [permutari x | x<-combinari l k]

--14
merge :: (Foldable t, Eq a, Num a) => (a, a) -> t (a, a) -> Bool
merge (l, c) regine = all (\(la, ca) -> l /= la && c /= ca && abs (l - la) /= abs (c - ca)) regine

nReg :: (Num t, Num p, Enum p, Eq t, Eq p) => p -> t -> [[(p, p)]]
nReg n k = add k []
  where
    add 0 regine = [regine]
    add num regine = concat [ add (num - 1) ((l, c) : regine) | l <- [1..n], c <- [1..n], merge (l, c) regine ]

