--1

data List a = Nil
            | Cons a (List a)
        deriving (Eq, Show)

-- Funcție ajutătoare pentru concatenarea a două liste de tipul nostru Custom
append :: List a -> List a -> List a
append Nil ys = ys
append (Cons x xs) ys = Cons x (append xs ys)

instance Functor List where
    fmap _ Nil = Nil
    fmap f (Cons x xs) = Cons (f x) (fmap f xs)

instance Applicative List where

    pure x = Cons x Nil    
    Nil <*> _ = Nil
    (Cons f fs) <*> xs = append (fmap f xs) (fs <*> xs)



f = Cons (+1) (Cons (*2) Nil)
v = Cons 1 (Cons 2 Nil)
test1 = (f <*> v) == Cons 2 (Cons 3 (Cons 2 (Cons 4 Nil)))

--2

--a

data Dog = Dog {
        name :: String
        , age :: Int
        , weight :: Int
        } deriving (Eq, Show)

noEmpty :: String -> Maybe String
noEmpty "" = Nothing
noEmpty str = Just str

noNegative :: Int -> Maybe Int
noNegative n
  | n < 0     = Nothing
  | otherwise = Just n

test21 = noEmpty "abc" == Just "abc"
test22 = noNegative (-5) == Nothing 
test23 = noNegative 5 == Just 5 

--b

dogFromString :: String -> Int -> Int -> Maybe Dog
dogFromString n a w = do
    validName <- noEmpty n
    validAge <- noNegative a
    validWeight <- noNegative w
    return (Dog validName validAge validWeight)

test24 = dogFromString "Toto" 5 11 == Just (Dog {name = "Toto", age = 5, 
                                                   weight = 11})

--c

dogFromStringApplicative :: String -> Int -> Int -> Maybe Dog
dogFromStringApplicative n a w = Dog <$> noEmpty n <*> noNegative a <*> noNegative w

--3

--a

newtype Name = Name String deriving (Eq, Show)
newtype Address = Address String deriving (Eq, Show)
data Person = Person Name Address deriving (Eq, Show)

validateLength :: Int -> String -> Maybe String
validateLength maxLen str
    | length str < maxLen = Just str
    | otherwise           = Nothing

test31 = validateLength 5 "abc" == Just "abc"

--b

mkName :: String -> Maybe Name
mkName s = fmap Name (validateLength 25 s)

mkAddress :: String -> Maybe Address
mkAddress s = fmap Address (validateLength 100 s)

test32 = mkName "Popescu" ==  Just (Name "Popescu")
test33 = mkAddress "Str Academiei" ==  Just (Address "Str Academiei")

--c

mkPerson :: String -> String -> Maybe Person
mkPerson n a = do
    validName <- mkName n
    validAddr <- mkAddress a
    return (Person validName validAddr)

test34 = mkPerson "Popescu" "Str Academiei" == Just (Person (Name "Popescu")
                                                    (Address "Str Academiei"))

--d


mkPersonApplicative :: String -> String -> Maybe Person
mkPersonApplicative n a = Person <$> mkName n <*> mkAddress a