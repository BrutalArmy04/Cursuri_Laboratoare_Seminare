module Lab9 where

data Tree = Empty
  | Node Int Tree Tree Tree

extree :: Tree
extree = Node 4 (Node 5 Empty Empty Empty) 
                (Node 3 Empty Empty (Node 1 Empty Empty Empty)) Empty

class ArbInfo t where
  level :: t -> Int
  sumval :: t -> Int
  nrFrunze :: t -> Int

instance ArbInfo Tree where
  level Empty = 0
  level (Node _ left middle right) = 
    1 + max (level left) (max (level middle) (level right))
  
  sumval Empty = 0
  sumval (Node val left middle right) = 
    val + sumval left + sumval middle + sumval right
  
  nrFrunze Empty = 0
  nrFrunze (Node _ Empty Empty Empty) = 1
  nrFrunze (Node _ left middle right) = 
    nrFrunze left + nrFrunze middle + nrFrunze right

class Scalar a where
  zero :: a 
  one :: a 
  adds :: a -> a -> a
  mult :: a -> a -> a
  negates :: a -> a
  recips :: a -> a

instance Scalar Int where
  zero = 0
  one = 1
  adds = (+)
  mult = (*)
  negates = negate
  recips x = 1

instance Scalar Float where
  zero = 0.0
  one = 1.0
  adds = (+)
  mult = (*)
  negates = negate
  recips x = 1 / x

instance Scalar Double where
  zero = 0.0
  one = 1.0
  adds = (+)
  mult = (*)
  negates = negate
  recips x = 1 / x

class (Scalar a) => Vector v a where
  zerov :: v a
  onev :: v a
  addv :: v a -> v a -> v a
  smult :: a -> v a -> v a
  negatev :: v a -> v a

data Vec2D a = V2 a a deriving (Eq, Show)

instance Scalar a => Vector Vec2D a where
  zerov = V2 zero zero
  onev = V2 one one
  addv (V2 x1 y1) (V2 x2 y2) = V2 (x1 `adds` x2) (y1 `adds` y2)
  smult s (V2 x y) = V2 (s `mult` x) (s `mult` y)
  negatev (V2 x y) = V2 (negates x) (negates y)

data Vec3D a = V3 a a a deriving (Eq, Show)

instance Scalar a => Vector Vec3D a where
  zerov = V3 zero zero zero
  onev = V3 one one one
  addv (V3 x1 y1 z1) (V3 x2 y2 z2) = 
    V3 (x1 `adds` x2) (y1 `adds` y2) (z1 `adds` z2)
  smult s (V3 x y z) = V3 (s `mult` x) (s `mult` y) (s `mult` z)
  negatev (V3 x y z) = V3 (negates x) (negates y) (negates z)

--teste

testTree :: Bool
testTree =
  level extree == 3 &&
  sumval extree == 13 &&
  nrFrunze extree == 2

testScalarInt :: Bool
testScalarInt =
  zero == (0 :: Int) &&
  one == (1 :: Int) &&
  adds 3 5 == (8 :: Int) &&
  mult 4 6 == (24 :: Int) &&
  negates 7 == (-7 :: Int)

testVec2DInt :: Bool
testVec2DInt =
  let v1 = V2 (3 :: Int) 5
      v2 = V2 (2 :: Int) 7
      v3 = V2 (5 :: Int) 12
      v4 = V2 (6 :: Int) 10
      zeroVec = zerov :: Vec2D Int
      oneVec = onev :: Vec2D Int
  in addv v1 v2 == v3 &&
     smult 2 v1 == v4 &&
     zeroVec == V2 0 0 &&
     oneVec == V2 1 1 &&
     negatev v1 == V2 (-3) (-5)

testVec3DFloat :: Bool
testVec3DFloat =
  let v1 = V3 (1.0 :: Float) 2.0 3.0
      v2 = V3 (4.0 :: Float) 5.0 6.0
      v3 = V3 (5.0 :: Float) 7.0 9.0
      v4 = V3 (2.0 :: Float) 4.0 6.0
      zeroVec = zerov :: Vec3D Float
      oneVec = onev :: Vec3D Float
  in addv v1 v2 == v3 &&
     smult 2.0 v1 == v4 &&
     zeroVec == V3 0.0 0.0 0.0 &&
     oneVec == V3 1.0 1.0 1.0 &&
     negatev v1 == V3 (-1.0) (-2.0) (-3.0)