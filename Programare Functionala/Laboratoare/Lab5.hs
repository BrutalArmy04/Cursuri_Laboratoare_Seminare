{-
# Laborator 5 - Fold

## Fold
Funcțiile `foldr` și `foldl` sunt folosite pentru agregarea unei colecții de elemente.

foldr :: (a -> b -> b) -> b -> [a] -> b
foldr op unit [a1, a2, ... , an] = a1 `op` (a2 `op` (... `op` (an `op` unit)))

foldl :: (b -> a -> b) -> b -> [a] -> b
foldl op unit [a1, a2, ... , an] = (...((unit `op` a1) `op` a2) ...) `op` an
-}

import Data.List (minimumBy)
import Data.Ord (comparing)

-- 1. Calculați suma pătratelor elementelor impare dintr-o listă dată ca parametru.
-- Corecție: Trebuie filtrate elementele impare înainte de mapare/fold.
ex1 :: [Int] -> Int
ex1 l = foldr (+) 0 (map (^2) (filter odd l))

-- 2. Scrieți o funcție care verifică că toate elementele dintr-o listă sunt `True`.
ex2 :: [Bool] -> Bool
ex2 l = foldr (&&) True l

-- 3. Scrieți o funcție care verifică dacă toate elementele satisfac o proprietate.
allVerifies :: (a -> Bool) -> [a] -> Bool
allVerifies p xs = foldr (&&) True (map p xs)

-- 4. Scrieți o funcție care verifică dacă există elemente care satisfac o proprietate.
-- Corecție: Elementul neutru pentru (||) trebuie să fie False.
anyVerifies :: (a -> Bool) -> [a] -> Bool
anyVerifies p xs = foldr (||) False (map p xs)

-- 5. Redefiniți map și filter folosind foldr.
mapFoldr :: (a -> b) -> [a] -> [b]
mapFoldr f = foldr (\x acc -> f x : acc) []

filterFoldr :: (a -> Bool) -> [a] -> [a]
filterFoldr p = foldr (\x acc -> if p x then x : acc else acc) []

-- 6. listToInt folosind foldl (transformă [2,3,4,5] în 2345).
listToInt :: [Integer] -> Integer
listToInt l = foldl (\acc x -> acc * 10 + x) 0 l

-- 7. Eliminarea caracterelor
-- (a) Elimină toate aparițiile unui caracter.
rmChar :: Char -> String -> String
rmChar c s = filter (/= c) s

-- (b) Recursiv: elimină caracterele din primul argument găsite în al doilea.
rmCharsRec :: String -> String -> String
rmCharsRec [] str = str
rmCharsRec (c:cs) str = rmCharsRec cs (rmChar c str)

-- (c) Folosind foldr pentru a face același lucru.
rmCharsFold :: String -> String -> String
rmCharsFold chars str = foldr rmChar str chars

-- 8. myReverse folosind foldl.
myReverse :: [a] -> [a]
myReverse l = foldl (\acc x -> x : acc) [] l

-- 9. myElem folosind foldr.
myElem :: Eq a => a -> [a] -> Bool
myElem x = foldr (\y acc -> x == y || acc) False

-- 10. myUnzip folosind foldr.
myUnzip :: [(a, b)] -> ([a], [b])
myUnzip = foldr (\(x, y) (xs, ys) -> (x:xs, y:ys)) ([], [])

-- 11. Union (reuniunea a două liste) folosind foldr.
union :: Eq a => [a] -> [a] -> [a]
union xs ys = foldr (\x acc -> if x `elem` acc then acc else x : acc) ys xs

-- 12. Intersect (intersecția) folosind foldr.
intersect :: Eq a => [a] -> [a] -> [a]
intersect xs ys = foldr (\x acc -> if x `elem` ys then x : acc else acc) [] xs

-- 13. Permutations folosind foldr.
-- Metoda "funcțională pură" cu fold: inserăm elementul curent în toate pozițiile posibile
-- pentru fiecare permutare a restului listei.
permutations :: [a] -> [[a]]
permutations = foldr (\x acc -> concatMap (insertAll x) acc) [[]]
  where
    insertAll :: a -> [a] -> [[a]]
    insertAll e [] = [[e]]
    insertAll e (y:ys) = (e:y:ys) : map (y:) (insertAll e ys)

{-
## Extra - Algoritmul lui Prim
14. Implementați algoritmul lui Prim folosind fold.
-}

infinity :: Int
infinity = 999999

-- Definim tipul grafului ca o funcție de cost între două noduri
type Graph = Int -> Int -> Int
type Node = Int
type Edge = (Node, Node) -- (From, To)

-- Funcția prim: primește lista de noduri și funcția de cost.
-- Returnează lista de muchii care formează MST.
prim :: [Node] -> Graph -> [Edge]
prim [] _ = []
prim (start:nodes) graph = 
    let 
        -- Starea inițială: (Muchii MST, Lista costurilor minime către nodurile nevizitate)
        -- Lista costurilor: [(Node, Cost, FromNode)]
        initialCosts = map (\n -> (n, graph start n, start)) nodes
    in 
        -- Folosim foldl pentru a itera de (n-1) ori (numărul de noduri rămase de adăugat)
        -- Lista peste care facem fold este irelevantă, contează doar lungimea ei (nodes e restul nodurilor)
        fst $ foldl step ([], initialCosts) nodes
  where
    step :: ([Edge], [(Node, Int, Node)]) -> Node -> ([Edge], [(Node, Int, Node)])
    step (mst, costs) _ =
        let 
            -- 1. Găsim nodul cu costul minim din lista de candidați
            (minNode, minCost, fromNode) = minimumBy (comparing (\(_, c, _) -> c)) costs
            
            -- 2. Îl eliminăm din lista de candidați (a devenit vizitat)
            remainingCandidates = filter (\(n, _, _) -> n /= minNode) costs
            
            -- 3. Actualizăm costurile pentru nodurile rămase
            updatedCosts = map (\(n, currentCost, currentFrom) ->
                let distToNewNode = graph minNode n
                in if distToNewNode < currentCost 
                   then (n, distToNewNode, minNode) -- Am găsit o cale mai scurtă prin minNode
                   else (n, currentCost, currentFrom) -- Păstrăm vechiul cost
                ) remainingCandidates
        in 
            -- Adăugăm muchia în MST și trecem la pasul următor cu noile costuri
            ((fromNode, minNode) : mst, updatedCosts)

-- Exemplu de graf pentru testare
-- Noduri: 1, 2, 3
-- 1-2 cost 10
-- 2-3 cost 1
-- 1-3 cost 5
testGraph :: Graph
testGraph 1 2 = 10
testGraph 2 1 = 10
testGraph 2 3 = 1
testGraph 3 2 = 1
testGraph 1 3 = 5
testGraph 3 1 = 5
testGraph _ _ = infinity

-- Testare: prim [1,2,3] testGraph
-- Ar trebui să returneze muchiile [(1,3), (3,2)] (sau invers) cu cost total 6.