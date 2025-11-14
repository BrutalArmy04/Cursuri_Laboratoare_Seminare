--1

{-
[ x^2 |x <- [1..10], x `rem` 3 == 2 ]   = > 0   - m-am uitat prost
[ (x,y) | x <- [1..5], y <- [x..(x+2)] ]    => 1,3 2,4 3,5  - exista puncte
[ (x,y) | x <- [1..3], let k = x^2, y <- [1..k] ]   => 1 1 2 4 3 9
[ x | x <- "Facultatea de Matematica si Informatica", elem x ['A'..'Z'] ]   => FMI
[ [x..y] | x <- [1..5], y <- [1..5], x < y ]    => 1 2 1 3 1 4 1 5 2 3 2 4 2 5 3 4 3 5 4 5
-}

--2

factori :: Integral a => a -> [a]
factori a = [x | x <- [1..a], a `rem` x == 0]

--3

prim :: Integral a => a -> Bool
prim a = length (factori a) == 2

--4

numerePrime n = [x | x<-[2..n], prim x == True]

{-
sectiuni
dr4 = drop 4
dr 4 [1..100] = [5..100]
*, `rem`, `elem`
(*4) 5 <=> 20

lambda expresii
\x y -> x + y
aplica2 f x = f (f x)
aplica2 f = f . f   => compunerea din mate
aplica2 = \f x -> f (f x)
aplica2 f = \x -> f (f x)

map => aplica o functie pentru toate elementele listei
l = [1, -2, 3]
map(+2) l => [3, 0, 5]
map(negate.abs) l => [-1,-2,-3]

filter -> filtreaza elem care respecta o conditie (care sa returneze bool)
-}

--5

myzip3 :: [a] -> [b] -> [c] -> [(a,b,c)]
myzip3 [] _ _ = []
myzip3 _ [] _ = []
myzip3 _ _ [] = []
myzip3 (x:xs) (y:ys) (z:zs) = (x,y,z) : myzip3 xs ys zs

--6

firstEl :: [(b1, b2)] -> [b1]
firstEl l = map fst l

--7

sumList :: (Foldable t, Num b) => [t b] -> [b]
sumList l = map sum l

--8
pre12 :: Integral b => [b] -> [b]
pre12 l = map(\x -> if even x then div x 2 else x*2) l

--9

isLetterinCuv :: (Foldable t, Eq a) => a -> [t a] -> [t a]
isLetterinCuv lit cuv = filter (elem lit) cuv

--10

puteriLaNrImp :: Integral b => [b] -> [b]
puteriLaNrImp l = map(\x -> if odd x then x^2 else x) l

--11

patratePozImp :: Num b => [b] -> [b]
patratePozImp l = map (^2) (map snd (filter (odd . fst) (zip [1..] l)))

--12

numaiVocale :: [String] -> [String]
numaiVocale strings = map (filter (`elem` "aeiouAEIOU")) strings

--13
myzip :: [a] -> [b] -> [(a,b)]
myzip [] _ = []
myzip _ [] = []
myzip (x:xs) (y:ys)  = (x,y) : myzip xs ys 

myfilter :: (a -> Bool) -> [a] -> [a]
myfilter _ [] = []
myfilter p (x:xs)
    | p x       = x : myfilter p xs
    | otherwise = myfilter p xs

-- X si 0

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
    -- Verifică linii
    checkLine [board!!0, board!!1, board!!2] ||
    checkLine [board!!3, board!!4, board!!5] ||
    checkLine [board!!6, board!!7, board!!8] ||
    -- Verifică coloane
    checkLine [board!!0, board!!3, board!!6] ||
    checkLine [board!!1, board!!4, board!!7] ||
    checkLine [board!!2, board!!5, board!!8] ||
    -- Verifică diagonale
    checkLine [board!!0, board!!4, board!!8] ||
    checkLine [board!!2, board!!4, board!!6]
  where
    checkLine cells = all (== Just p) cells

-- 4. Funcția win - filtrează configurațiile câștigătoare
win :: Char -> [[Maybe Char]] -> [[Maybe Char]]
win p configs = [config | config <- configs, isWinner p config]

-- 5. Verifică dacă tabla este plină
isBoardFull :: [Maybe Char] -> Bool
isBoardFull board = not (Nothing `elem` board)

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
          remaining = [config | config <- configs, not (isBoardFull config)]
          nextConfigs = next player remaining
      in winning : playGame nextConfigs (nextPlayer player)

-- 8. Configurație inițială (tablă goală)
initialConfig :: [Maybe Char]
initialConfig = [Nothing, Nothing, Nothing, Nothing, Nothing, Nothing, Nothing, Nothing, Nothing]

-- 9. Afișare tabla
showBoard :: [Maybe Char] -> String
showBoard board = 
    " " ++ showCell (board!!0) ++ " | " ++ showCell (board!!1) ++ " | " ++ showCell (board!!2) ++ " \n" ++
    "-----------\n" ++
    " " ++ showCell (board!!3) ++ " | " ++ showCell (board!!4) ++ " | " ++ showCell (board!!5) ++ " \n" ++
    "-----------\n" ++
    " " ++ showCell (board!!6) ++ " | " ++ showCell (board!!7) ++ " | " ++ showCell (board!!8) ++ " \n"
  where
    showCell Nothing = " "
    showCell (Just c) = [c]

-- 10. Teste simple
testStep :: IO ()
testStep = do
    putStrLn "Configurație inițială:"
    putStrLn $ showBoard initialConfig
    
    putStrLn "Mutări posibile pentru X:"
    let moves = step 'X' initialConfig
    putStrLn $ "Număr mutări: " ++ show (length moves)
    putStrLn $ showBoard (head moves)

testNext :: IO ()
testNext = do
    putStrLn "\nTest next:"
    let configs = [initialConfig]
    let afterFirstMove = next 'X' configs
    putStrLn $ "După prima mutare: " ++ show (length afterFirstMove) ++ " configurații"
    
    let afterSecondMove = next '0' afterFirstMove
    putStrLn $ "După a doua mutare: " ++ show (length afterSecondMove) ++ " configurații"

testWin :: IO ()
testWin = do
    putStrLn "\nTest win:"
    -- Configurație câștigătoare pentru X
    let winningBoard = [Just 'X', Just 'X', Just 'X', Nothing, Nothing, Nothing, Nothing, Nothing, Nothing]
    putStrLn $ "Tabla câștigătoare:"
    putStrLn $ showBoard winningBoard
    putStrLn $ "X a câștigat? " ++ show (isWinner 'X' winningBoard)
    putStrLn $ "0 a câștigat? " ++ show (isWinner '0' winningBoard)

-- 11. Exemplu de joc scurt
exampleGame :: IO ()
exampleGame = do
    putStrLn "\nSimulare joc scurt:"
    let game = playGame [initialConfig] 'X'
    
    putStrLn $ "Runda 1 - Configurații câștigătoare pentru X: " ++ show (length (game !! 0))
    putStrLn $ "Runda 2 - Configurații câștigătoare pentru 0: " ++ show (length (game !! 1))
    putStrLn $ "Runda 3 - Configurații câștigătoare pentru X: " ++ show (length (game !! 2))

-- Funcție principală
main :: IO ()
main = do
    testStep
    testNext
    testWin
    exampleGame