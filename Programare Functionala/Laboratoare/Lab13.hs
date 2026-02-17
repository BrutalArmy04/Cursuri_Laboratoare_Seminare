{-
# Laborator 13 - Monade (Maybe, IO, Writer, Reader)
-}

module Lab13 where

import Prelude hiding (lookup)

-- ============================================================================
-- 1. MAYBE MONAD
-- ============================================================================

pos :: Int -> Bool
pos x = if (x>=0) then True else False

-- Funcția inițială cu >>=
-- fct :: Maybe Int -> Maybe Bool
-- fct mx = mx >>= (\x -> Just (pos x))

-- 1. Rescriere fct folosind do notation
fct :: Maybe Int -> Maybe Bool
fct mx = do
    x <- mx
    return (pos x)

-- 2. Adunarea a două valori Maybe Int

-- a) Folosind pattern matching (sau șabloane)
addM_pattern :: Maybe Int -> Maybe Int -> Maybe Int
addM_pattern (Just x) (Just y) = Just (x + y)
addM_pattern _ _ = Nothing

-- b) Folosind do notation
addM :: Maybe Int -> Maybe Int -> Maybe Int
addM mx my = do
    x <- mx
    y <- my
    return (x + y)

-- ============================================================================
-- 3. RESCRIERE CU DO NOTATION
-- ============================================================================

cartesian_product :: [a] -> [b] -> [(a, b)]
cartesian_product xs ys = do
    x <- xs
    y <- ys
    return (x, y)

prod :: (a -> b -> c) -> [a] -> [b] -> [c]
prod f xs ys = do
    x <- xs
    y <- ys
    return (f x y)

myGetLine :: IO String
myGetLine = do
    x <- getChar
    if x == '\n'
        then return []
        else do
            xs <- myGetLine
            return (x:xs)

-- ============================================================================
-- 4. RESCRIERE CU SECVENȚIERE (>>=)
-- ============================================================================

prelNo :: Floating a => a -> a
prelNo noin = sqrt noin

-- Funcția inițială cu do notation:
{-
ioNumber = do
     noin <- readLn :: IO Float
     putStrLn $ "Intrare\n" ++ (show noin)
     let noout = prelNo noin
     putStrLn $ "Iesire"
     print noout
-}

-- Rescriere cu >>= (bind) și >> (sequence)
ioNumber :: IO ()
ioNumber = 
    (readLn :: IO Float) >>= \noin ->
    putStrLn ("Intrare\n" ++ show noin) >>
    let noout = prelNo noin in
    putStrLn "Iesire" >>
    print noout

-- ============================================================================
-- 5. WRITER MONAD
-- ============================================================================

-- A. Writer cu String (concatenare text)
newtype WriterS a = Writer { runWriter :: (a, String) } 

instance Functor WriterS where
    fmap f (Writer (x, log)) = Writer (f x, log)

instance Applicative WriterS where
    pure x = Writer (x, "")
    (Writer (f, log1)) <*> (Writer (x, log2)) = Writer (f x, log1 ++ log2)

instance Monad WriterS where
    return = pure
    (Writer (x, log1)) >>= k = 
        let (y, log2) = runWriter (k x)
        in Writer (y, log1 ++ log2)

tell :: String -> WriterS ()
tell log = Writer ((), log)

-- 5.a) logIncrement
logIncrement :: Int -> WriterS Int
logIncrement x = do
    tell ("increment:" ++ show x ++ "\n")
    return (x + 1)

logIncrement2 :: Int -> WriterS Int
logIncrement2 x = do
    y <- logIncrement x
    logIncrement y

-- 5.b) logIncrementN
-- Generalizare: aplică increment de n ori
logIncrementN :: Int -> Int -> WriterS Int
logIncrementN x 0 = return x
logIncrementN x n = do
    y <- logIncrement x
    logIncrementN y (n - 1)

-- B. Writer cu Listă de String-uri (WriterLS)
-- 5.c) Modificare pentru a produce lista mesajelor
newtype WriterLS a = WriterLS { runWriterLS :: (a, [String]) }

instance Functor WriterLS where
    fmap f (WriterLS (x, log)) = WriterLS (f x, log)

instance Applicative WriterLS where
    pure x = WriterLS (x, [])
    (WriterLS (f, log1)) <*> (WriterLS (x, log2)) = WriterLS (f x, log1 ++ log2)

instance Monad WriterLS where
    return = pure
    (WriterLS (x, log1)) >>= k = 
        let (y, log2) = runWriterLS (k x)
        in WriterLS (y, log1 ++ log2)

tellLS :: String -> WriterLS ()
tellLS msg = WriterLS ((), [msg])

logIncrementLS :: Int -> WriterLS Int
logIncrementLS x = do
    tellLS ("increment:" ++ show x)
    return (x + 1)

logIncrementNLS :: Int -> Int -> WriterLS Int
logIncrementNLS x 0 = return x
logIncrementNLS x n = do
    y <- logIncrementLS x
    logIncrementNLS y (n - 1)

-- ============================================================================
-- 6. READER MONAD
-- ============================================================================

data Person = Person { name :: String, age :: Int }
    deriving Show

-- 6.a) Funcții simple de afișare
showPersonN :: Person -> String
showPersonN p = "NAME: " ++ name p

showPersonA :: Person -> String
showPersonA p = "AGE: " ++ show (age p)

-- 6.b) Combinarea funcțiilor
showPerson :: Person -> String
showPerson p = "(" ++ showPersonN p ++ ", " ++ showPersonA p ++ ")"

-- Definirea Monadei Reader (manual, pentru a nu depinde de biblioteca mtl)
newtype Reader env a = Reader { runReader :: env -> a }

instance Functor (Reader env) where
    fmap f (Reader g) = Reader (\e -> f (g e))

instance Applicative (Reader env) where
    pure x = Reader (\_ -> x)
    (Reader f) <*> (Reader g) = Reader (\e -> (f e) (g e))

instance Monad (Reader env) where
    return = pure
    (Reader g) >>= f = Reader (\e -> runReader (f (g e)) e)

ask :: Reader env env
ask = Reader id

-- 6.c) Variante monadice folosind Reader

mshowPersonN :: Reader Person String
mshowPersonN = do
    p <- ask
    return ("NAME:" ++ name p)

mshowPersonA :: Reader Person String
mshowPersonA = do
    p <- ask
    return ("AGE:" ++ show (age p))

mshowPerson :: Reader Person String
mshowPerson = do
    n <- mshowPersonN
    a <- mshowPersonA
    return ("(" ++ n ++ "," ++ a ++ ")")

-- ============================================================================
-- TESTE
-- ============================================================================

main :: IO ()
main = do
    putStrLn "--- Teste Lab 13 ---"
    
    putStrLn "\n1. Fct Maybe:"
    print $ fct (Just 10)
    print $ fct (Just (-5))
    
    putStrLn "\n2. AddM:"
    print $ addM (Just 4) (Just 3)
    print $ addM Nothing (Just 3)

    putStrLn "\n5.b WriterS (String):"
    let (val, log) = runWriter $ logIncrementN 2 4
    putStrLn $ "Valoare: " ++ show val
    putStrLn "Log:"
    putStr log

    putStrLn "\n5.c WriterLS (Lista):"
    let (valL, logL) = runWriterLS $ logIncrementNLS 2 4
    putStrLn $ "Valoare: " ++ show valL
    putStrLn $ "Log List: " ++ show logL

    putStrLn "\n6. Reader Person:"
    let p = Person "ada" 20
    putStrLn $ runReader mshowPersonN p
    putStrLn $ runReader mshowPersonA p
    putStrLn $ runReader mshowPerson p