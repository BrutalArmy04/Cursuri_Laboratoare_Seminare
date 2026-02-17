module Lab10 where

import Data.List (nub)
import Data.Maybe (fromJust)

-- 8. Extinderea tipului Prop cu Implicație și Echivalență
-- (Am mutat definiția la început pentru a fi vizibilă în tot fișierul)

type Nume = String
data Prop
  = Var Nume
  | F
  | T
  | Not Prop
  | Prop :|: Prop
  | Prop :&: Prop
  | Prop :->: Prop   -- Implicație
  | Prop :<->: Prop  -- Echivalență
  deriving Eq

infixr 2 :|:
infixr 3 :&:
infixr 4 :->:
infixr 5 :<->:

-- 1. Definirea formulelor pa, pb, pc

-- a. (P \/ Q) /\ (P /\ Q)
pa :: Prop
pa = (Var "P" :|: Var "Q") :&: (Var "P" :&: Var "Q")

-- b. (P \/ Q) /\ (~P /\ ~Q)
pb :: Prop
pb = (Var "P" :|: Var "Q") :&: (Not (Var "P") :&: Not (Var "Q"))

-- c. (P /\ (Q \/ R)) /\ ((~P \/ ~Q) /\ (~P \/ ~R))
pc :: Prop
pc = (Var "P" :&: (Var "Q" :|: Var "R")) :&: 
     ((Not (Var "P") :|: Not (Var "Q")) :&: (Not (Var "P") :|: Not (Var "R")))

-- 2. Instanța Show pentru Prop
instance Show Prop where
  show (Var name)   = name
  show F            = "F"
  show T            = "T"
  show (Not p)      = "(~" ++ show p ++ ")"
  show (p :|: q)    = "(" ++ show p ++ "|" ++ show q ++ ")"
  show (p :&: q)    = "(" ++ show p ++ "&" ++ show q ++ ")"
  show (p :->: q)   = "(" ++ show p ++ "->" ++ show q ++ ")"
  show (p :<->: q)  = "(" ++ show p ++ "<->" ++ show q ++ ")"

test_ShowProp :: Bool
test_ShowProp = show (Not (Var "P") :&: Var "Q") == "((~P)&Q)"

-- Mediu de evaluare
type Env = [(Nume, Bool)]

impureLookup :: Eq a => a -> [(a,b)] -> b
impureLookup a = fromJust . lookup a

-- 3. Evaluarea expresiilor logice
eval :: Prop -> Env -> Bool
eval (Var name) env = impureLookup name env
eval F _            = False
eval T _            = True
eval (Not p) env    = not (eval p env)
eval (p :|: q) env  = eval p env || eval q env
eval (p :&: q) env  = eval p env && eval q env
eval (p :->: q) env = not (eval p env) || eval q env  -- p -> q  <=>  not p or q
eval (p :<->: q) env = eval p env == eval q env       -- p <-> q <=>  p == q

test_eval :: Bool
test_eval = eval (Var "P" :|: Var "Q") [("P", True), ("Q", False)] == True

-- 4. Colectarea variabilelor
variabile :: Prop -> [Nume]
variabile (Var name)   = [name]
variabile F            = []
variabile T            = []
variabile (Not p)      = variabile p
variabile (p :|: q)    = nub (variabile p ++ variabile q)
variabile (p :&: q)    = nub (variabile p ++ variabile q)
variabile (p :->: q)   = nub (variabile p ++ variabile q)
variabile (p :<->: q)  = nub (variabile p ++ variabile q)

test_variabile :: Bool
test_variabile = variabile (Not (Var "P") :&: Var "Q") == ["P", "Q"] -- Ordinea poate varia in functie de nub, dar continutul e acelasi

-- 5. Generarea tuturor mediilor posibile
envs :: [Nume] -> [Env]
envs [] = [[]]
envs (x:xs) = 
    let rest = envs xs
    in [((x, False):e) | e <- rest] ++ [((x, True):e) | e <- rest]

test_envs :: Bool
test_envs =
    envs ["P", "Q"]
    ==
    [ [ ("P",False), ("Q",False) ]
    , [ ("P",False), ("Q",True) ]
    , [ ("P",True), ("Q",False) ]
    , [ ("P",True), ("Q",True) ]
    ]

-- 6. Satisfiabilitate
satisfiabila :: Prop -> Bool
satisfiabila p = any (eval p) (envs (variabile p))

test_satisfiabila1 :: Bool
test_satisfiabila1 = satisfiabila (Not (Var "P") :&: Var "Q") == True

test_satisfiabila2 :: Bool
test_satisfiabila2 = satisfiabila (Not (Var "P") :&: Var "P") == False

-- 7. Validitate
valida :: Prop -> Bool
valida p = all (eval p) (envs (variabile p))
-- Alternativ: valida p = not (satisfiabila (Not p))

test_valida1 :: Bool
test_valida1 = valida (Not (Var "P") :&: Var "Q") == False

test_valida2 :: Bool
test_valida2 = valida (Not (Var "P") :|: Var "P") == True

-- 9. Echivalență
echivalenta :: Prop -> Prop -> Bool
echivalenta p q = 
    let vars = nub (variabile p ++ variabile q)
        allEnvs = envs vars
    in all (\env -> eval p env == eval q env) allEnvs
-- Alternativ: echivalenta p q = valida (p :<->: q)

test_echivalenta1 :: Bool
test_echivalenta1 = (Var "P" :&: Var "Q") `echivalenta` (Not (Not (Var "P") :|: Not (Var "Q")))

test_echivalenta2 :: Bool
test_echivalenta2 = not ((Var "P") `echivalenta` (Var "Q"))

test_echivalenta3 :: Bool
test_echivalenta3 = (Var "R" :|: Not (Var "R")) `echivalenta` (Var "Q" :|: Not (Var "Q"))