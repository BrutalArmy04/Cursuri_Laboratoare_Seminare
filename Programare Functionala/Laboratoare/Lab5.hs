--foldr si foldl
-- l = [1,2,3]
--f x y = x + y
-- foldr f 0 ( elem de start) l (lista noastra)
-- va lua ultimul element si 0 si le va aduna si merge in spate pe lista => (((0+3)+2)+1)
-- foldl f 0 l => (((0+1)+2)+3)

--1

ex1 l = foldr (+) 0 (map(^2) l) 

--2

ex2 l = foldr (&&) True l

--3

allVerifies :: (a -> Bool) -> [a] -> Bool
allVerifies p xs = foldr (&&) True (map p xs)

--4 

anyVerifies :: (a -> Bool) -> [a] -> Bool
anyVerifies p xs = foldr (||) True (map p xs)

--5


mapFoldr :: Foldable t1 => (t2 -> a) -> t1 t2 -> [a]
mapFoldr f = foldr (\x acc -> f x : acc) []

filterFoldr :: Foldable t => (a -> Bool) -> t a -> [a]
filterFoldr p = foldr (\x acc -> if p x then x : acc else acc) []

--6
-- listToInt [2,3,4,5] = 2345
listToInt :: (Foldable t, Num b) => t b -> b
listToInt l = foldl (\acc x -> acc*10 + x) 0 l

--7

rmChar :: Eq a => a -> [a] -> [a]
rmChar c s = filter (/= c) s

rmCharsRec :: Eq a => [a] -> [a] -> [a]
rmCharsRec _ [] = []
rmCharsRec [] str = str
rmCharsRec (c:cs) str = rmCharsRec cs (rmChar c str)

rmCharsFold :: (Foldable t, Eq a) => t a -> [a] -> [a]
rmCharsFold chars str = foldr rmChar str chars

--8

myReverse :: Foldable t => t a -> [a]
myReverse l = foldl(\acc x -> x : acc) [] l


--9


myElem :: (Foldable t, Eq a) => a -> t a -> Bool
myElem x = foldr (\y acc -> x == y || acc) False

--10

myUnzip :: [(a, b)] -> ([a], [b])
myUnzip = foldr (\(x, y) (xs, ys) -> (x:xs, y:ys)) ([], [])

--11


union :: (Foldable t, Eq a) => t a -> [a] -> [a]
union xs ys = foldr (\x acc -> if x `elem` acc then acc else x : acc) ys xs

--12

intersect :: (Foldable t1, Foldable t2, Eq a) => t1 a -> t2 a -> [a]
intersect xs ys = foldr (\x acc -> if x `elem` ys then x: acc else acc) [] xs

--13

permutations :: Eq a => [a] -> [[a]]
permutations [] = [[]]
permutations xs = foldr (\x acc -> acc ++ [x:perm | perm <- permutations (filter (/= x) xs)]) [] xs


--Prim

infinity :: Int
infinity = 999999

type Node = Int



prim :: (Ord a1, Eq a2) => [a2] -> (a2 -> a2 -> a1) -> [(a2, a2)]
prim [] _ = []
prim (start:nodes) graph = go [(n, graph start n, start) | n <- nodes] [start] []
  where
    go [] _ mst = reverse mst
    go candidates inMST mst =
        let (minNode, minDist, fromNode) = 
                foldl1 (\(n1,d1,f1) (n2,d2,f2) -> if d1 < d2 then (n1,d1,f1) else (n2,d2,f2)) candidates
            newCandidates = [(n, min (graph minNode n) dist, if graph minNode n < dist then minNode else from) 
                           | (n, dist, from) <- candidates, n /= minNode]
        in go newCandidates (minNode:inMST) ((fromNode, minNode):mst)

-- Test
testGraph :: (Eq a1, Eq a2, Num a1, Num a2, Num a3) => a1 -> a2 -> a3
testGraph 1 2 = 1
testGraph 2 1 = 1  
testGraph 2 3 = 1
testGraph 3 2 = 1
testGraph 1 3 = 2
testGraph 3 1 = 2
testGraph _ _ = 0

