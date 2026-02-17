{-
# Laborator 6 - Tipuri de date utilizator

## Apples and Oranges
-}

-- 1. Definirea tipului de date Fruct
data Fruct
  = Mar String Bool
  | Portocala String Int
  deriving Show

-- Exemple de date
ionatanFaraVierme :: Fruct
ionatanFaraVierme = Mar "Ionatan" False

goldenCuVierme :: Fruct
goldenCuVierme = Mar "Golden Delicious" True

portocalaSicilia10 :: Fruct
portocalaSicilia10 = Portocala "Sanguinello" 10

listaFructe :: [Fruct]
listaFructe = [Mar "Ionatan" False,
                Portocala "Sanguinello" 10,
                Portocala "Valencia" 22,
                Mar "Golden Delicious" True,
                Portocala "Sanguinello" 15,
                Portocala "Moro" 12,
                Portocala "Tarocco" 3,
                Portocala "Moro" 12,
                Portocala "Valencia" 2,
                Mar "Golden Delicious" False,
                Mar "Golden" False,
                Mar "Golden" True]

-- a) Verifică dacă este portocală de Sicilia
ePortocalaDeSicilia :: Fruct -> Bool
ePortocalaDeSicilia (Portocala soi _ ) = soi `elem` ["Tarocco", "Moro", "Sanguinello"]
ePortocalaDeSicilia _ = False

test_ePortocalaDeSicilia1 :: Bool
test_ePortocalaDeSicilia1 = ePortocalaDeSicilia (Portocala "Moro" 12) == True
test_ePortocalaDeSicilia2 :: Bool
test_ePortocalaDeSicilia2 = ePortocalaDeSicilia (Mar "Ionatan" True) == False

-- b) Calculează numărul total de felii ale portocalelor de Sicilia
nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia x = sum [nr | (Portocala _ nr) <- filter ePortocalaDeSicilia x]

test_nrFeliiSicilia :: Bool
test_nrFeliiSicilia = nrFeliiSicilia listaFructe == 52

-- c) Calculează numărul de mere care au viermi
nrMereViermi :: [Fruct] -> Int
nrMereViermi [] = 0
nrMereViermi ((Mar _ True):t) = 1 + nrMereViermi t
nrMereViermi (_:t) = nrMereViermi t 

test_nrMereViermi :: Bool
test_nrMereViermi = nrMereViermi listaFructe == 2

{-
## Paw Patrol
-}

-- 2. Definirea tipului Animal
type NumeA = String
type Rasa = String
data Animal = Pisica NumeA | Caine NumeA Rasa
    deriving Show

-- a) Funcția vorbeste
vorbeste :: Animal -> String
vorbeste (Pisica _) = "Meow!"
vorbeste (Caine _ _) = "Woof!" 

-- b) Funcția rasa (folosind Maybe)
rasa :: Animal -> Maybe String
rasa (Caine _ r) = Just r
rasa (Pisica _) = Nothing

{-
## Matrix Resurrections
-}

-- 3. Definirea tipurilor Linie și Matrice
data Linie = L [Int]
   deriving Show
data Matrice = M [Linie]
   deriving Show

-- a) Verifică suma elementelor pe linii (folosind foldr)
verifica :: Matrice -> Int -> Bool
verifica (M linii) n = foldr (\(L l) acc -> sum l == n && acc) True linii

test_veri1 :: Bool
test_veri1 = verifica (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 10 
test_verif2 :: Bool
test_verif2 = verifica (M[L[2,20,3], L[4,21], L[2,3,6,8,6], L[8,5,3,9]]) 25 

-- b) doarPozN - verifică liniile de lungime n
doarPozN :: Matrice -> Int -> Bool
doarPozN (M linii) n = all allPozitive (filter (lungimeN n) linii)
  where
    lungimeN len (L lista) = length lista == len
    allPozitive (L lista) = all (> 0) lista

testPoz1 :: Bool
testPoz1 = doarPozN (M [L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 
testPoz2 :: Bool
testPoz2 = doarPozN (M [L[1,2,-3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 

-- c) corect - verifică dacă toate liniile au aceeași lungime
corect :: Matrice -> Bool
corect (M []) = True
corect (M (L primaLinie:restul)) = all (\(L linie) -> length linie == length primaLinie) restul

testcorect1 :: Bool
testcorect1 = corect (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 
testcorect2 :: Bool
testcorect2 = corect (M[L[1,2,3], L[4,5,8], L[3,6,8], L[8,5,3]]) 

{-
## Extra: Turtle!
-}

-- a) Tipuri de date de bază
data Direction = North | NorthEast | East | SouthEast | South | SouthWest | West | NorthWest
    deriving (Show, Eq, Enum)

data Turtle = Turtle { position :: (Int, Int), direction :: Direction }
    deriving Show

-- b) Action
data Action = Step | Turn
    deriving Show

-- c) Command
data Command = Do Action | Repeat Int Command
    deriving Show

-- d) getPizza
getPizza :: Turtle -> [Command] -> (Int, Int)
getPizza turtle [] = position turtle
getPizza turtle (cmd:cmds) = getPizza (executeCommand turtle cmd) cmds

executeCommand :: Turtle -> Command -> Turtle
executeCommand turtle (Do action) = executeAction turtle action
executeCommand turtle (Repeat n cmd) 
    | n <= 0 = turtle
    | otherwise = executeCommand (executeCommand turtle cmd) (Repeat (n-1) cmd)

executeAction :: Turtle -> Action -> Turtle
executeAction turtle Step = moveForward turtle
executeAction turtle Turn = turnRight turtle

moveForward :: Turtle -> Turtle
moveForward (Turtle (x, y) dir) = Turtle newPos dir
  where
    newPos = case dir of
        North     -> (x, y+1)
        NorthEast -> (x+1, y+1)
        East      -> (x+1, y)
        SouthEast -> (x+1, y-1)
        South     -> (x, y-1)
        SouthWest -> (x-1, y-1)
        West      -> (x-1, y)
        NorthWest -> (x-1, y+1)

turnRight :: Turtle -> Turtle
turnRight (Turtle pos dir) = Turtle pos newDir
  where
    -- Folosim Enum pentru a roti 45 grade (un pas in Enum)
    newDir = toEnum ((fromEnum dir + 1) `mod` 8)

-- e) Extensii (folosim sufixul Ext pentru a nu intra in conflict cu definițiile de mai sus)
-- Cerința: Action cu constructorul seq care ia două comenzi.
-- Observație: Structura cerută e puțin neobișnuită (Action să conțină Command), dar o implementăm conform textului.

data ActionExt = StepExt | TurnExt | Seq CommandExt CommandExt
    deriving Show

data CommandExt = DoExt ActionExt | RepeatExt Int CommandExt | WaitExt
    deriving Show

getPizzaExt :: Turtle -> [CommandExt] -> (Int, Int)
getPizzaExt turtle [] = position turtle
getPizzaExt turtle (cmd:cmds) = getPizzaExt (executeCommandExt turtle cmd) cmds

executeCommandExt :: Turtle -> CommandExt -> Turtle
executeCommandExt turtle WaitExt = turtle
executeCommandExt turtle (DoExt action) = executeActionExt turtle action
executeCommandExt turtle (RepeatExt n cmd) 
    | n <= 0 = turtle
    | otherwise = executeCommandExt (executeCommandExt turtle cmd) (RepeatExt (n-1) cmd)

executeActionExt :: Turtle -> ActionExt -> Turtle
executeActionExt turtle StepExt = moveForward turtle -- refolosim logica de miscare
executeActionExt turtle TurnExt = turnRight turtle   -- refolosim logica de rotire
executeActionExt turtle (Seq cmd1 cmd2) = 
    executeCommandExt (executeCommandExt turtle cmd1) cmd2

-- f) Aggregate commands using fold
aggregateCommands :: [CommandExt] -> CommandExt
aggregateCommands = foldr seqCommands WaitExt
  where
    seqCommands cmd acc = DoExt (Seq cmd acc)

-- Testare Turtle
startTurtle :: Turtle
startTurtle = Turtle (0,0) North

testTurtle :: (Int, Int)
testTurtle = getPizza startTurtle [Do Step, Do Turn, Do Step] 
-- Ar trebui sa mearga Nord (0,1), apoi NordEst, apoi pas la (1,2)