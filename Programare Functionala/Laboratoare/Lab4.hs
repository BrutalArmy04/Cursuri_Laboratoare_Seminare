{-
# Laborator 4 - Liste, map, filter

## Liste (Exercițiul 1)
Evaluarea expresiilor date:
[ x^2 |x <- [1..10], x `rem` 3 == 2 ]
=> [4, 25, 64] (x este 2, 5, 8)

[ (x,y) | x <- [1..5], y <- [x..(x+2)] ]
=> [(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(4,5),(4,6),(5,5),(5,6),(5,7)]

[ (x,y) | x <- [1..3], let k = x^2, y <- [1..k] ]
=> [(1,1), (2,1),(2,2),(2,3),(2,4), (3,1)..(3,9)]

[ x | x <- "Facultatea de Matematica si Informatica", elem x ['A'..'Z'] ]
=> "FMI"

[ [x..y] | x <- [1..5], y <- [1..5], x < y ]
=> [[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
-}

-- 2. Funcția factori (divizori pozitivi)
factori :: Int -> [Int]
factori a = [x | x <- [1..abs a], abs a `rem` x == 0]

-- 3. Predicatul prim
prim :: Int -> Bool
prim a = length (factori a) == 2

-- 4. Lista numerelor prime până la n
numerePrime :: Int -> [Int]
numerePrime n = [x | x <- [2..n], prim x]

{-
## Funcția zip (Exercițiul 5)
-}

-- 5. myzip3
myzip3 :: [a] -> [b] -> [c] -> [(a,b,c)]
myzip3 [] _ _ = []
myzip3 _ [] _ = []
myzip3 _ _ [] = []
myzip3 (x:xs) (y:ys) (z:zs) = (x,y,z) : myzip3 xs ys zs

{-
## Map și Filter (Exercițiile 6-12)
-}

-- 6. firstEl - Lista primelor elemente din perechi
firstEl :: [(a, b)] -> [a]
firstEl l = map fst l

-- 7. sumList - Lista sumelor listelor interne
sumList :: [[Int]] -> [Int]
sumList l = map sum l

-- 8. prel2 - Pare înjumătățite, impare dublate
-- (Corectat din pre12 în prel2 conform cerinței)
prel2 :: [Int] -> [Int]
prel2 l = map (\x -> if even x then x `div` 2 else x * 2) l

-- 9. Șirurile care conțin un anumit caracter
-- Funcția elem verifică apartenența, filter păstrează doar șirurile care satisfac condiția
filterByChar :: Char -> [String] -> [String]
filterByChar chr strings = filter (elem chr) strings

-- 10. Lista pătratelor numerelor impare
-- Corecție: Cerința implică filtrarea numerelor impare și apoi ridicarea la pătrat.
-- Varianta ta anterioară păstra și numerele pare (neschimbate).
puteriLaNrImp :: [Int] -> [Int]
puteriLaNrImp l = map (^2) (filter odd l)

-- 11. Pătratele elementelor de pe poziții impare
-- Considerăm pozițiile începând de la 1 (1, 3, 5...)
patratePozImp :: [Int] -> [Int]
patratePozImp l = map (^2) (map snd (filter (odd . fst) (zip [1..] l)))

-- 12. Eliminarea consoanelor (păstrarea vocalelor)
numaiVocale :: [String] -> [String]
numaiVocale strings = map (filter (`elem` "aeiouAEIOU")) strings

{-
## Funcții Recursive (Exercițiul 13)
-}

-- 13a. mymap
mymap :: (a -> b) -> [a] -> [b]
mymap _ [] = []
mymap f (x:xs) = f x : mymap f xs

-- 13b. myfilter
myfilter :: (a -> Bool) -> [a] -> [a]
myfilter _ [] = []
myfilter p (x:xs)
    | p x       = x : myfilter p xs
    | otherwise = myfilter p xs

{-
## EXTRA - Jocul X și 0
Implementare completă
-}

-- 1. Funcția step - generează toate mutările posibile
step :: Char -> [Maybe Char] -> [[Maybe Char]]
step p config = [placeMark config i p | i <- [0..8], config !! i == Nothing]
  where
    placeMark board pos mark = 
        take pos board ++ [Just mark] ++ drop (pos + 1) board

-- 2. Funcția next - aplică step pe toate configurațiile
next :: Char -> [[Maybe Char]] -> [[Maybe Char]]
next p configs = concat [step p config | config <- configs]

-- 3. Verifică dacă un jucător a câștigat
isWinner :: Char -> [Maybe Char] -> Bool
isWinner p board = 
    any checkLine 
      [ [0,1,2], [3,4,5], [6,7,8]  -- Linii
      , [0,3,6], [1,4,7], [2,5,8]  -- Coloane
      , [0,4,8], [2,4,6]           -- Diagonale
      ]
  where
    checkLine indices = all (\i -> board !! i == Just p) indices

-- 4. Funcția win - filtrează configurațiile câștigătoare
win :: Char -> [[Maybe Char]] -> [[Maybe Char]]
win p configs = filter (isWinner p) configs

-- 5. Verifică dacă tabla este plină
isBoardFull :: [Maybe Char] -> Bool
isBoardFull board = Nothing `notElem` board

-- 6. Schimbă jucătorul
nextPlayer :: Char -> Char
nextPlayer 'X' = '0'
nextPlayer '0' = 'X'

-- 7. Simularea jocului complet
playGame :: [[Maybe Char]] -> Char -> [[[Maybe Char]]]
playGame configs player
  | null configs = []
  | otherwise = 
      let winning = win player configs
          remaining = [config | config <- configs, not (isBoardFull config) && not (isWinner player config)]
          nextConfigs = next player remaining
      in winning : playGame nextConfigs (nextPlayer player)

-- 8. Configurație inițială (tablă goală)
initialConfig :: [Maybe Char]
initialConfig = replicate 9 Nothing

-- 9. Afișare tabla
showBoard :: [Maybe Char] -> String
showBoard board = 
    "\n" ++
    " " ++ c 0 ++ " | " ++ c 1 ++ " | " ++ c 2 ++ " \n" ++
    "-----------\n" ++
    " " ++ c 3 ++ " | " ++ c 4 ++ " | " ++ c 5 ++ " \n" ++
    "-----------\n" ++
    " " ++ c 6 ++ " | " ++ c 7 ++ " | " ++ c 8 ++ " \n"
  where
    c i = case board !! i of
            Nothing -> " "
            Just val -> [val]

-- 10. Teste
main :: IO ()
main = do
    putStrLn "--- Test Step ---"
    let moves = step 'X' initialConfig
    putStrLn $ "Mutări posibile din start: " ++ show (length moves)
    putStrLn $ showBoard (head moves)

    putStrLn "--- Test Win ---"
    let winningBoard = [Just 'X', Just 'X', Just 'X', Nothing, Nothing, Nothing, Nothing, Nothing, Nothing]
    putStrLn $ "Este X câștigător? " ++ show (isWinner 'X' winningBoard)

    putStrLn "--- Simulare Joc (Primele 3 runde) ---"
    let game = playGame [initialConfig] 'X'
    putStrLn $ "Configurații câștigătoare X (Runda 1): " ++ show (length (game !! 0)) -- Ar trebui să fie 0
    -- Nota: Acest joc generează arborele complet, care este imens.
    -- Nu printați tot arborele în consolă!