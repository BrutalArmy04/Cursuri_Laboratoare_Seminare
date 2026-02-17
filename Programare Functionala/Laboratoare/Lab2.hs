{-
# Laborator 2 - Elemente de limbaj. Funcții

## Elemente de limbaj
Există numeroase biblioteci utile de Haskell. Puteți găsi informații despre ele în Hoogle.
Bibliotecile se includ în fișiere sursă folosind comanda `import`.
-}

import Data.List

{-
1. Permutări
Folosim `permutations` din Data.List.
Exemplu apel: permutations [1, 2, 3]
-}

-- Variabila globală din Lab 1
myInt :: Integer
myInt = 31415926535897932384626433832795028841971693993751058209749445923

{-
## Indentare și Funcții simple
-}

-- 3. Modificați indentarea funcției double (atenție la aliniere!)
double :: Integer -> Integer
double x = x + x

-- 4. Definiți funcția maxim
maxim :: Integer -> Integer -> Integer
maxim x y = 
    if (x > y)
        then x
        else y

-- Varianta maxim3 cu if/else imbricat
maxim3 :: Integer -> Integer -> Integer -> Integer
maxim3 x y z =
    if (x > y)
        then if (x > z)
            then x
            else z
        else if (y > z)
            then y
            else z

-- Varianta maxim3 folosind let...in
-- (User implementation preserved)
max3Let :: Integer -> Integer -> Integer -> Integer
max3Let x y z = 
    let
        u = maxim x y
    in 
        maxim u z

-- Funcția maxim4 folosind let..in și indentări
maxim4 :: Integer -> Integer -> Integer -> Integer -> Integer
maxim4 a b c d = 
    let 
        e = maxim a b
    in 
        let
            f = maxim e c
        in
            maxim f d

-- Testare maxim4
test_max4 :: Integer -> Integer -> Integer -> Integer -> Bool
test_max4 a b c d =
    let e = maxim4 a b c d
    in (e >= a) && (e >= b) && (e >= c) && (e >= d)

{- 
NOTA REFERITOARE LA EROAREA GHC-39999:
Eroarea "No instance for Show (Integer -> ... -> Bool)" apare dacă scrii în consolă doar:
> test_max4
GHCi încearcă să afișeze (să printeze) funcția însăși, ceea ce nu e posibil.
Trebuie să o apelezi cu argumente:
> test_max4 1 5 2 3
True
-}

{-
## Tipuri de date și Funcții (Exercițiul 6)
-}

-- Funcție ajutătoare pentru pătrat
patrat :: Integer -> Integer
patrat x = x * x

-- 6a) Suma pătratelor
sum_pat :: Integer -> Integer -> Integer
sum_pat a b = patrat a + patrat b

-- 6b) Paritate
paritate :: Integer -> String
paritate a = 
    if (a `mod` 2 == 0)
        then "par"
        else "impar"
        
{- 
RĂSPUNS: "Cum fac sa nu imi apara ghilimele cand afisez?"
În GHCi, când o funcție întoarce un String, interpretorul îl afișează folosind `show`, deci cu ghilimele ("par").
Pentru a vedea textul curat, trebuie să folosești funcția de IO `putStrLn`:
> putStrLn (paritate 4)
par
-}

-- 6c) Factorial
fact :: Integer -> Integer
fact a 
    | a < 1     = 1
    | otherwise = a * fact (a-1)

-- 6d) Verificare dublu
verif_dublu :: Integer -> Integer -> String
verif_dublu a b = 
    if (a > double b)
        then "a > 2*b" -- am modificat stringul pt claritate
        else "nu"

-- 6e) Maximul unei liste
-- Varianta recursivă standard (fără acumulator, mai simplă pentru început):
max_list :: [Integer] -> Integer
max_list [] = error "Lista vida nu are maxim"
max_list [x] = x
max_list (h:t) = maxim h (max_list t)

-- Varianta ta cu acumulator (reparată):
-- Trebuie să apelezi: max_list_acc [1,2,3] 0 (sau un minim foarte mic)
max_list_acc :: [Integer] -> Integer -> Integer
max_list_acc [] maximCurent = maximCurent
max_list_acc (h:t) maximCurent = 
    if h > maximCurent
        then max_list_acc t h
        else max_list_acc t maximCurent

{-
7. Funcția Poly
Cerința specifică tipul Double. Deoarece `patrat` de mai sus era pe Integer,
aici scriem calculul direct sau folosim operatorul `^` sau `**`.
-}
poly :: Double -> Double -> Double -> Double -> Double
poly a b c x = a * x * x + b * x + c

{-
8. Eeny Meeny
-}
eeny :: Integer -> String
eeny a = 
    if (paritate a == "par")
        then "eeny"
        else "meeny"

{-
9. FizzBuzz
-}
fizzbuzz :: Integer -> String
fizzbuzz a = 
    if (a `mod` 3 == 0 && a `mod` 5 == 0)
        then "FizzBuzz"
        else 
            if (a `mod` 3 == 0)
                then "Fizz"
                else if (a `mod` 5 == 0)
                    then "Buzz"
                    else ""

-- Varianta FizzBuzz cu gărzi (cerută în exercițiu)
fizzbuzzGuards :: Integer -> String
fizzbuzzGuards a
    | a `mod` 15 == 0 = "FizzBuzz"
    | a `mod` 3 == 0  = "Fizz"
    | a `mod` 5 == 0  = "Buzz"
    | otherwise       = ""

{-
## Recursivitate
-}

-- Fibonacci Cazuri
fibonacciCazuri :: Integer -> Integer
fibonacciCazuri n
    | n < 2     = n
    | otherwise = fibonacciCazuri (n - 1) + fibonacciCazuri (n - 2)
    
-- Fibonacci Ecuațional
fibonacciEcuational :: Integer -> Integer
fibonacciEcuational 0 = 0
fibonacciEcuational 1 = 1
fibonacciEcuational n =
    fibonacciEcuational (n - 1) + fibonacciEcuational (n - 2)

{-
10. Tribonacci
-}

-- Varianta cu Gărzi (scrisă de tine)
tribonacci :: Integer -> Integer
tribonacci n
    | n == 1    = 1
    | n == 2    = 1
    | n == 3    = 2
    | otherwise = tribonacci (n - 1) + tribonacci (n - 2) + tribonacci (n - 3)

-- Varianta Ecuațională (Pattern Matching) - Cerută suplimentar
tribonacciEq :: Integer -> Integer
tribonacciEq 1 = 1
tribonacciEq 2 = 1
tribonacciEq 3 = 2
tribonacciEq n = tribonacciEq (n - 1) + tribonacciEq (n - 2) + tribonacciEq (n - 3)

{-
11. Binomial
-}
binomial :: Integer -> Integer -> Integer
binomial n k 
    | k == 0    = 1
    | n == 0    = 0
    | otherwise = binomial (n - 1) k + binomial (n - 1) (k - 1)