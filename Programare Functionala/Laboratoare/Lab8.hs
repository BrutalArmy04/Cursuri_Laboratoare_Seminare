{-# OPTIONS_GHC -Wno-tabs #-}
import Prelude hiding (lookup)
-- vb de clase
-- show (show), eq (defineam op de egalitate si de neegalitate), ord(<, >, <=, >=) - clase pe care le-am mai vazut

--declararea unei clase

-- class Collention c where
    --dupa se pun titulatitatile functiilor


-- data MyType =        -> cum am facut pana acum
    -- deriving ...
    -- instance MyClass MyType where
        -- functiile din MyClass

-- 1

class Collection c where
  empty :: c key value
  singleton :: key -> value -> c key value
  insert
      :: Ord key
      => key -> value -> c key value -> c key value
  lookup :: Ord key => key -> c key value -> Maybe value
  delete :: Ord key => key -> c key value -> c key value
  keys :: c key value -> [key]
  values :: c key value -> [value]
  toList :: c key value -> [(key, value)]
  fromList :: Ord key => [(key,value)] -> c key value

  keys = map fst . toList
  values = map snd . toList
  fromList = foldr (\(k,v) acc -> insert k v acc) empty

-- curry: f(a,b) => f a b   => functie cu 1 param care devine o functie cu 2 param
-- uncurry: f a b => f(a,b) => functie cu 2 param care devine o functie cu 1 param


--2

newtype PairList k v = PairList { getPairList :: [(k, v)] }

instance Collection PairList where
  empty = PairList []
  singleton k v = PairList [(k, v)]
  insert k v (PairList pairs) = 
    PairList $ (k, v) : filter ((/= k) . fst) pairs
  lookup k (PairList pairs) = 
    case filter ((== k) . fst) pairs of
      [] -> Nothing
      ((_, v):_) -> Just v
  delete k (PairList pairs) = 
    PairList $ filter ((/= k) . fst) pairs
  toList = getPairList

--3

data SearchTree key value
  = Empty
  | BNode
      (SearchTree key value) -- elemente cu cheia mai mica
      key                    -- cheia elementului
      (Maybe value)          -- valoarea elementului
      (SearchTree key value) -- elemente cu cheia mai mare

instance Collection SearchTree where
    empty = Empty
    singleton k v = BNode Empty k (Just v) Empty
    insert key val Empty = BNode Empty key (Just val) Empty
    insert key val (BNode left k v right)
      | key == k = BNode left k (Just val) right
      | key < k  = BNode (insert key val left) k v right
      | otherwise = BNode left k v (insert key val right)
    lookup _ Empty = Nothing
    lookup k (BNode l key val r)
        | k < key   = lookup k l
        | k > key   = lookup k r
        | otherwise = val
    delete _ Empty = Empty
    delete key (BNode left k v right)
      | key == k = BNode left k Nothing right
      | key < k  = BNode (delete key left) k v right
      | otherwise = BNode left k v (delete key right)
    toList Empty = []
    toList (BNode left k v right) =
      toList left ++ maybe [] (\val -> [(k, val)]) v ++ toList right
    
data Punct = Pt [Int]

data Arb = Vid | F Int | N Arb Arb
          deriving Show

class ToFromArb a where
 	toArb :: a -> Arb
	fromArb :: Arb -> a

--4 

instance Show Punct where
  show (Pt []) = "()"
  show (Pt xs) = "(" ++ intercalate ", " (map show xs) ++ ")"
    where intercalate :: [a] -> [[a]] -> [a]
          intercalate _ [] = []
          intercalate sep (x:xs) = x ++ concatMap (sep ++) xs

--5

instance ToFromArb Punct where
  toArb (Pt []) = Vid
  toArb (Pt [x]) = F x
  toArb (Pt (x:xs)) = N (F x) (toArb (Pt xs))

  fromArb Vid = Pt []
  fromArb (F x) = Pt [x]
  fromArb (N left right) = 
    let Pt leftList = fromArb left
        Pt rightList = fromArb right
    in Pt (leftList ++ rightList)


--6

data Geo a = Square a | Rectangle a a | Circle a
    deriving Show

class GeoOps g where
     perimeter :: (Floating a) => g a -> a
     area :: (Floating a) =>  g a -> a

instance GeoOps Geo where
    perimeter (Square l) = 4 * l
    perimeter (Rectangle lung lat) = 2 * (lung + lat)
    perimeter (Circle r) = 2 * pi * r

    area (Square l) = l * l
    area (Rectangle lung lat) = lung * lat
    area (Circle r) = pi * r * r

--7

instance (Floating a, Eq a) => Eq (Geo a) where
  x == y = perimeter x == perimeter y