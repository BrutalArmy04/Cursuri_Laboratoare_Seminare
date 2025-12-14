import Data.List (nub)
import Data.Maybe (fromJust)

--8

type Nume = String
data Prop
  = Var Nume
  | F
  | T
  | Not Prop
  | Prop :|: Prop
  | Prop :&: Prop
  | Prop :->: Prop  
  | Prop :<->: Prop
  deriving Eq

infixr 2 :|:
infixr 3 :&:
infixr 4 :->:
infixr 4 :<->:

-- 1
pa :: Prop
pa = (Var "P" :|: Var "Q") :&: (Var "P" :&: Var "Q")

pb :: Prop
pb = (Var "P" :|: Var "Q") :&: (Not (Var "P") :&: Not (Var "Q"))

pc :: Prop
pc = (Var "P" :&: (Var "Q" :|: Var "R")) :&: 
     ((Not (Var "P") :|: Not (Var "Q")) :&: (Not (Var "P") :|: Not (Var "R")))

--2
instance Show Prop where
  show (Var name) = name
  show F = "F"
  show T = "T"
  show (Not p) = "(~" ++ show p ++ ")"
  show (p :|: q) = "(" ++ show p ++ "|" ++ show q ++ ")"
  show (p :&: q) = "(" ++ show p ++ "&" ++ show q ++ ")"
  show (p :->: q) = "(" ++ show p ++ "->" ++ show q ++ ")"
  show (p :<->: q) = "(" ++ show p ++ "<->" ++ show q ++ ")"

test_ShowProp :: Bool
test_ShowProp =
    show (Not (Var "P") :&: Var "Q") == "((~P)&Q)"

type Env = [(Nume, Bool)]

impureLookup :: Eq a => a -> [(a,b)] -> b
impureLookup a = fromJust . lookup a

--3
eval :: Prop -> Env -> Bool
eval (Var name) env = impureLookup name env
eval F _ = False
eval T _ = True
eval (Not p) env = not (eval p env)
eval (p :|: q) env = eval p env || eval q env
eval (p :&: q) env = eval p env && eval q env
eval (p :->: q) env = not (eval p env) || eval q env  -- p -> q = not p sau q
eval (p :<->: q) env = eval p env == eval q env       -- p <-> q = (p -> q) and (q -> p)

test_eval = eval  (Var "P" :|: Var "Q") [("P", True), ("Q", False)] == True

--4
variabile :: Prop -> [Nume]
variabile (Var name) = [name]
variabile F = []
variabile T = []
variabile (Not p) = variabile p
variabile (p :|: q) = nub (variabile p ++ variabile q)
variabile (p :&: q) = nub (variabile p ++ variabile q)
variabile (p :->: q) = nub (variabile p ++ variabile q)
variabile (p :<->: q) = nub (variabile p ++ variabile q)

test_variabile =
  variabile (Not (Var "P") :&: Var "Q") == ["P", "Q"]

--5
envs :: [Nume] -> [Env]
envs [] = [[]]
envs (x:xs) = 
    let rest = envs xs
    in [((x, False):e) | e <- rest] ++ [((x, True):e) | e <- rest]

test_envs =
    envs ["P", "Q"]
    ==
    [ [ ("P",False)
      , ("Q",False)
      ]
    , [ ("P",False)
      , ("Q",True)
      ]
    , [ ("P",True)
      , ("Q",False)
      ]
    , [ ("P",True)
      , ("Q",True)
      ]
    ]

--6
satisfiabila :: Prop -> Bool
satisfiabila p = any (eval p) (envs (variabile p))

test_satisfiabila1 = satisfiabila (Not (Var "P") :&: Var "Q") == True
test_satisfiabila2 = satisfiabila (Not (Var "P") :&: Var "P") == False

--7
valida :: Prop -> Bool
valida p = all (eval p) (envs (variabile p))

test_valida1 = valida (Not (Var "P") :&: Var "Q") == False
test_valida2 = valida (Not (Var "P") :|: Var "P") == True

-- 9
echivalenta :: Prop -> Prop -> Bool
echivalenta p q = all (\env -> eval p env == eval q env) (envs (nub (variabile p ++ variabile q)))

test_echivalenta1 =
  True
  ==
  (Var "P" :&: Var "Q") `echivalenta` (Not (Not (Var "P") :|: Not (Var "Q")))
test_echivalenta2 =
  False
  ==
  (Var "P") `echivalenta` (Var "Q")
test_echivalenta3 =
  True
  ==
  (Var "R" :|: Not (Var "R")) `echivalenta` (Var "Q" :|: Not (Var "Q"))
