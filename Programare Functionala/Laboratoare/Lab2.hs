import Data.List
myInt = 31415926535897932384626433832795028841971693993751058209749445923

double :: Integer -> Integer
double x = x+x

maxim :: Integer -> Integer -> Integer
maxim x y = if (x > y)
               then x
          else y

max3 x y z = let
             u = maxim x y
             in (maxim  u z)

maxim3 :: Integer -> Integer -> Integer -> Integer
maxim3 x y z=
    if (x>y)
        then if (x>z)
            then x
            else z
        else if(y>z)
            then y
            else z
maxim4 :: Integer -> Integer -> Integer -> Integer -> Integer
maxim4 a b c d = 
    let 
        e = maxim a b
    in 
        let
            f = maxim e c
        in
            maxim f d

test_max4 :: Integer -> Integer -> Integer -> Integer -> Bool
test_max4 a b c d =
    let e = maxim4 a b c d
    in (e>=a) && (e>=b) && (e>=c) && (e>=d)

--ghci> test_max4
--
 -- <interactive>:38:1: error: --[GHC-39999]
--    * No instance for `Show
  --                       (Integer -> Integer -> Integer -> Integer -> Bool)'
    --    arising from a use of `print'
        --(maybe you haven't applied a --function to enough arguments?)
   -- * In a stmt of an interactive GHCi command: print it

patrat :: Integer -> Integer
patrat x = x*x

sum_pat :: Integer -> Integer -> Integer
sum_pat a b = patrat a + patrat b

paritate :: Integer -> String
paritate a = 
    if ((a `mod` 2) == 0)
        then "par"
        else "impar"
-- cum fac sa nu imi apara ghilimele cand afisez

fact :: Integer -> Integer
fact a 
    | a < 1     = 1
    | otherwise = a * fact (a-1)


verif_dublu :: Integer -> Integer -> String
verif_dublu a b= 
    if (a>(double b))
        then "a"
        else "b"

max_list :: [Integer] -> Integer -> Integer
--max_list (h:t) = max_list (h:t) 0 
max_list [] maxim = maxim
max_list (h:t) maxim = 
    if maxim > h
        then max_list t h
        else max_list t maxim
    

--nu merge

poly :: Integer -> Integer -> Integer -> Integer -> Integer
poly a b c x = a * patrat x + b * x + c


eeny :: Integer -> String
eeny a = 
    if (paritate a == "par")
        then "eeny"
        else "meeny"

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

fibonacciCazuri :: Integer -> Integer
fibonacciCazuri n
    | n < 2     = n
    | otherwise = fibonacciCazuri (n - 1) + fibonacciCazuri (n - 2)
    
fibonacciEcuational :: Integer -> Integer
fibonacciEcuational 0 = 0
fibonacciEcuational 1 = 1
fibonacciEcuational n =
    fibonacciEcuational (n - 1) + fibonacciEcuational (n - 2)
    
tribonacci :: Integer -> Integer
tribonacci n
    | n == 1    = 1
    | n == 2    = 1
    | n == 3    = 2
    | otherwise = tribonacci (n - 1) + tribonacci (n - 2) + tribonacci (n - 3)

binomial :: Integer -> Integer -> Integer
binomial n k 
    | k == 0    = 1
    | n == 0    = 0
    | otherwise = binomial (n - 1) k + binomial (n - 1) (k - 1)
    