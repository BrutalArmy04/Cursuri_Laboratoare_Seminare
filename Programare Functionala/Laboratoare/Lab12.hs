{-
# Laborator 12 - Functori, Applicative

Amintiți-vă clasele `Functor` și `Applicative`.

class Functor f where
    fmap :: (a -> b) -> f a -> f b

class Functor f => Applicative f where
    pure :: a -> f a
    (<*>) :: f (a -> b) -> f a -> f b

Exemple (de rulat în consolă):
-- Just length <*> Just "world"
-- Just (++" world") <*> Just "hello,"
-- pure (+) <*> Just 3 <*> Just 5
-- pure (+) <*> Just 3 <*> Nothing
-- (++) <$> ["ha","heh"] <*> ["?","!"]
-}

-- ============================================================================
-- 1. LIST TYPE
-- ============================================================================

{-
Se dă tipul de date List. Scrieți instanțe ale claselor Functor și Applicative.
-}

data List a = Nil
            | Cons a (List a)
        deriving (Eq, Show)

-- Funcție ajutătoare pentru concatenarea a două liste de tipul nostru Custom
-- Necesară pentru implementarea Applicative
append :: List a -> List a -> List a
append Nil ys = ys
append (Cons x xs) ys = Cons x (append xs ys)

instance Functor List where
    fmap _ Nil = Nil
    fmap f (Cons x xs) = Cons (f x) (fmap f xs)

instance Applicative List where
    -- pure creează o listă cu un singur element
    pure x = Cons x Nil    
    
    -- Applicative pentru liste funcționează ca produs cartezian
    Nil <*> _ = Nil
    (Cons f fs) <*> xs = append (fmap f xs) (fs <*> xs)

-- Test Exemplu
f :: List (Int -> Int)
f = Cons (+1) (Cons (*2) Nil)

v :: List Int
v = Cons 1 (Cons 2 Nil)

test1 :: Bool
test1 = (f <*> v) == Cons 2 (Cons 3 (Cons 2 (Cons 4 Nil)))

-- ============================================================================
-- 2. DOG TYPE
-- ============================================================================

{-
Se dă tipul de date Dog.
-}

data Dog = Dog {
        name :: String
        , age :: Int
        , weight :: Int
        } deriving (Eq, Show)

-- a) Scrieți funcțiile noEmpty și noNegative

noEmpty :: String -> Maybe String
noEmpty "" = Nothing
noEmpty str = Just str

noNegative :: Int -> Maybe Int
noNegative n
  | n < 0     = Nothing
  | otherwise = Just n

test21, test22, test23 :: Bool
test21 = noEmpty "abc" == Just "abc"
test22 = noNegative (-5) == Nothing 
test23 = noNegative 5 == Just 5 

-- b) dogFromString folosind do-notation (Monad style)

dogFromString :: String -> Int -> Int -> Maybe Dog
dogFromString n a w = do
    validName <- noEmpty n
    validAge <- noNegative a
    validWeight <- noNegative w
    return (Dog validName validAge validWeight)

test24 :: Bool
test24 = dogFromString "Toto" 5 11 == Just (Dog {name = "Toto", age = 5, weight = 11})

-- c) dogFromString folosind Applicative style (<$>, <*>)

dogFromStringApplicative :: String -> Int -> Int -> Maybe Dog
dogFromStringApplicative n a w = Dog <$> noEmpty n <*> noNegative a <*> noNegative w

-- ============================================================================
-- 3. PERSON TYPE
-- ============================================================================

{-
Se dau tipurile Name, Address, Person.
-}

newtype Name = Name String deriving (Eq, Show)
newtype Address = Address String deriving (Eq, Show)
data Person = Person Name Address deriving (Eq, Show)

-- a) validateLength

validateLength :: Int -> String -> Maybe String
validateLength maxLen str
    | length str < maxLen = Just str
    | otherwise           = Nothing

test31 :: Bool
test31 = validateLength 5 "abc" == Just "abc"

-- b) mkName și mkAddress folosind fmap

mkName :: String -> Maybe Name
mkName s = fmap Name (validateLength 25 s)

mkAddress :: String -> Maybe Address
mkAddress s = fmap Address (validateLength 100 s)

test32, test33 :: Bool
test32 = mkName "Popescu" ==  Just (Name "Popescu")
test33 = mkAddress "Str Academiei" ==  Just (Address "Str Academiei")

-- c) mkPerson (varianta standard/do-notation)

mkPerson :: String -> String -> Maybe Person
mkPerson n a = do
    validName <- mkName n
    validAddr <- mkAddress a
    return (Person validName validAddr)

test34 :: Bool
test34 = mkPerson "Popescu" "Str Academiei" == Just (Person (Name "Popescu") (Address "Str Academiei"))

-- d) mkPerson folosind Applicative style

mkPersonApplicative :: String -> String -> Maybe Person
mkPersonApplicative n a = Person <$> mkName n <*> mkAddress a