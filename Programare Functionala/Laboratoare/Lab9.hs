{-
# Laborator 9 - ADT. Clase de tipuri
-}

-- ============================================================================
-- 1. ARBORI
-- ============================================================================

{-
Se dă următorul tip de date reprezentând arbori ternari cu informația de tip întreg în rădăcină.
-}

data Tree = Empty  -- arbore vid
          | Node Int Tree Tree Tree -- arbore cu valoare (Int) si 3 fii
          deriving Show

-- Exemplul din cerință
extree :: Tree
extree = Node 4 (Node 5 Empty Empty Empty) 
                (Node 3 Empty Empty (Node 1 Empty Empty Empty)) Empty

{-
1. Instanțiați clasa ArbInfo pentru tipul Tree.
   - level: înălțimea arborelui (0 pt vid)
   - sumval: suma valorilor
   - nrFrunze: numărul de frunze
-}

class ArbInfo t where
  level :: t -> Int 
  sumval :: t -> Int
  nrFrunze :: t -> Int

instance ArbInfo Tree where
  -- Level: 1 + maximul dintre înălțimile fiilor
  level Empty = 0
  level (Node _ left middle right) = 
    1 + max (level left) (max (level middle) (level right))
  
  -- Sumval: valoarea curentă + suma valorilor din subarbori
  sumval Empty = 0
  sumval (Node val left middle right) = 
    val + sumval left + sumval middle + sumval right
  
  -- NrFrunze: 1 dacă e frunză, altfel suma frunzelor fiilor
  nrFrunze Empty = 0
  nrFrunze (Node _ Empty Empty Empty) = 1
  nrFrunze (Node _ left middle right) = 
    nrFrunze left + nrFrunze middle + nrFrunze right

-- ============================================================================
-- 2. VECTORI - SCALARI
-- ============================================================================

{-
Vom implementa spații vectoriale. Mai întâi definim clasa scalarilor.
-}

class Scalar a where
  zero :: a 
  one :: a 
  adds :: a -> a -> a 
  mult :: a -> a -> a
  negates :: a -> a
  recips :: a -> a

-- 2. Instanța pentru Int
-- Notă: Int nu este corp comutativ (nu are invers multiplicativ real), 
-- dar implementăm interfața conform cerinței tehnice.
instance Scalar Int where
  zero = 0
  one = 1
  adds = (+)
  mult = (*)
  negates = negate
  recips _ = 1 -- Int nu suportă 1/x, returnăm dummy value sau 0/1

-- Instanța pentru Float
instance Scalar Float where
  zero = 0.0
  one = 1.0
  adds = (+)
  mult = (*)
  negates = negate
  recips x = 1.0 / x

-- Instanța pentru Double
instance Scalar Double where
  zero = 0.0
  one = 1.0
  adds = (+)
  mult = (*)
  negates = negate
  recips x = 1.0 / x

-- ============================================================================
-- 3. VECTORI - VECTORI
-- ============================================================================

{-
Clasa Vector care depinde de clasa Scalar.
-}

class (Scalar a) => Vector v a where
  zerov :: v a
  onev :: v a
  addv :: v a -> v a -> v a -- adunare vector
  smult :: a -> v a -> v a  -- inmultire cu scalar
  negatev :: v a -> v a     -- negare vector

-- 3a. Vectori 2D
data Vec2D a = V2 a a 
    deriving (Eq, Show)

instance Scalar a => Vector Vec2D a where
  zerov = V2 zero zero
  onev = V2 one one
  addv (V2 x1 y1) (V2 x2 y2) = V2 (x1 `adds` x2) (y1 `adds` y2)
  smult s (V2 x y) = V2 (s `mult` x) (s `mult` y)
  negatev (V2 x y) = V2 (negates x) (negates y)

-- 3b. Vectori 3D
data Vec3D a = V3 a a a 
    deriving (Eq, Show)

instance Scalar a => Vector Vec3D a where
  zerov = V3 zero zero zero
  onev = V3 one one one
  addv (V3 x1 y1 z1) (V3 x2 y2 z2) = 
    V3 (x1 `adds` x2) (y1 `adds` y2) (z1 `adds` z2)
  smult s (V3 x y z) = V3 (s `mult` x) (s `mult` y) (s `mult` z)
  negatev (V3 x y z) = V3 (negates x) (negates y) (negates z)

-- ============================================================================
-- TESTE
-- ============================================================================

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

main :: IO ()
main = do
    putStrLn $ "Test Tree: " ++ show testTree
    putStrLn $ "Test Scalar Int: " ++ show testScalarInt
    putStrLn $ "Test Vec2D Int: " ++ show testVec2DInt
    putStrLn $ "Test Vec3D Float: " ++ show testVec3DFloat

{-
## Extra: Corespondența Curry-Howard
Se recomandă vizionarea prezentării 'Propositions as Types' de Philip Wadler.
-}