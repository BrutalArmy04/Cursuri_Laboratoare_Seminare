{-# OPTIONS_GHC -Wno-tabs #-}
module Lab8 where

import Prelude hiding (lookup)
import qualified Data.List as List

-- 1. Clasa Collection
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

  -- Implementările implicite
  keys c = map fst (toList c)
  values c = map snd (toList c)
  fromList list = foldr (\(k,v) acc -> insert k v acc) empty list

-- 2. Instanța pentru PairList
newtype PairList k v = PairList { getPairList :: [(k, v)] }
  deriving Show

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

-- 3. Instanța pentru SearchTree
data SearchTree key value
  = Empty
  | BNode
      (SearchTree key value) -- elemente cu cheia mai mica
      key                    -- cheia elementului
      (Maybe value)          -- valoarea elementului (Nothing daca e sters)
      (SearchTree key value) -- elemente cu cheia mai mare
  deriving Show

instance Collection SearchTree where
    empty = Empty
    
    singleton k v = BNode Empty k (Just v) Empty
    
    insert key val Empty = BNode Empty key (Just val) Empty
    insert key val (BNode left nodeKey nodeVal right)
      | key == nodeKey = BNode left nodeKey (Just val) right
      | key < nodeKey  = BNode (insert key val left) nodeKey nodeVal right
      | otherwise      = BNode left nodeKey nodeVal (insert key val right)
    
    lookup _ Empty = Nothing
    lookup k (BNode left nodeKey nodeVal right)
        | k < nodeKey = lookup k left
        | k > nodeKey = lookup k right
        | otherwise   = nodeVal -- returnează Maybe value direct
        
    delete _ Empty = Empty
    delete key (BNode left nodeKey nodeVal right)
      | key == nodeKey = BNode left nodeKey Nothing right -- Soft delete
      | key < nodeKey  = BNode (delete key left) nodeKey nodeVal right
      | otherwise      = BNode left nodeKey nodeVal (delete key right)
      
    toList Empty = []
    toList (BNode left nodeKey nodeVal right) =
      toList left ++ maybe [] (\v -> [(nodeKey, v)]) nodeVal ++ toList right

-- Definiții pentru exercițiile 4 și 5
data Punct = Pt [Int]

data Arb = Vid | F Int | N Arb Arb
          deriving Show

class ToFromArb a where
    toArb :: a -> Arb
    fromArb :: Arb -> a

-- 4. Instanța Show pentru Punct
instance Show Punct where
  show (Pt []) = "()"
  show (Pt xs) = "(" ++ intercalate ", " (map show xs) ++ ")"
    where 
      -- Definiție locală sau putem folosi Data.List.intercalate
      intercalate :: [a] -> [[a]] -> [a]
      intercalate _ [] = []
      intercalate _ [y] = y
      intercalate sep (y:ys) = y ++ sep ++ intercalate sep ys

-- 5. Instanța ToFromArb pentru Punct
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

-- 6. Figuri Geometrice
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

-- 7. Instanța Eq pentru Geo (bazată pe perimetru)
instance (Floating a, Eq a) => Eq (Geo a) where
  g1 == g2 = perimeter g1 == perimeter g2