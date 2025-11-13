import Distribution.Compat.Lens (_1)
--1

data Fruct
  = Mar String Bool
  | Portocala String Int

ionatanFaraVierme :: Fruct
ionatanFaraVierme = Mar "Ionatan" False
goldenCuVierme :: Fruct
goldenCuVierme = Mar "Golden Delicious" True
portocalaSicilia10 :: Fruct
portocalaSicilia10 = Portocala "Sanguinello" 10
cosFructe :: [Fruct]
cosFructe = [Mar "Ionatan" False,
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


ePortocalaDeSicilia :: Fruct -> Bool
ePortocalaDeSicilia (Portocala soi _ ) = soi `elem` ["Tarocco", "Moro", "Sanguinello"]
ePortocalaDeSicilia _ = False

nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia x = sum[nr | (Portocala soi nr) <- filter ePortocalaDeSicilia  x]

nrMereViermi :: [Fruct] -> Int
nrMereViermi [] = 0
nrMereViermi ((Mar _ True):t) = 1 + nrMereViermi t
nrMereViermi  (_:t) = nrMereViermi t 

--2

type NumeA = String
type Rasa = String
data Animal = Pisica NumeA | Caine NumeA Rasa
    deriving Show

vorbeste :: Animal -> String
vorbeste (Pisica _) = "Meow"
vorbeste (Caine _ _) = "Woof" 


rasa :: Animal -> Maybe String
rasa (Caine _ rasa) = Just rasa 
rasa (Pisica _) = Nothing

--3

data Linie = L [Int]
   deriving Show
data Matrice = M [Linie]
   deriving Show


verifica :: Matrice -> Int -> Bool
verifica (M linii) n = foldr (\linie acc -> sumaLinie linie == n && acc) True linii
  where
    sumaLinie (L lista) = sum lista

test_veri1 :: Bool
test_veri1 = verifica (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 10 
test_verif2 :: Bool
test_verif2 = verifica (M[L[2,20,3], L[4,21], L[2,3,6,8,6], L[8,5,3,9]]) 25 

doarPozN :: Matrice -> Int -> Bool
doarPozN (M linii) n = all (allPozitive) (filter (lungimeN n) linii)
  where
    lungimeN n (L lista) = length lista == n
    allPozitive (L lista) = all (> 0) lista

testPoz1 = doarPozN (M [L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 
testPoz2 = doarPozN (M [L[1,2,-3], L[4,5], L[2,3,6,8], L[8,5,3]]) 3 

corect :: Matrice -> Bool
corect (M []) = True
corect (M (L primaLinie:restul)) = all (\(L linie) -> length linie == length primaLinie) restul

testcorect1 = corect (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 
testcorect2 = corect (M[L[1,2,3], L[4,5,8], L[3,6,8], L[8,5,3]]) 

