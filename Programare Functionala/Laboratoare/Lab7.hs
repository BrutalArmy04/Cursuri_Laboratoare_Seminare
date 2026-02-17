{-
# Laborator 7 - ADT (Abstract Data Types)

## Expresii și arbori
Se dau următoarele tipuri de date reprezentând expresii și arbori de expresii.
-}

data Expr = Const Int -- integer constant
          | Expr :+: Expr -- addition
          | Expr :*: Expr -- multiplication
           deriving Eq

data Operation = Add | Mult deriving (Eq, Show)

data Tree = Lf Int -- leaf
          | Node Operation Tree Tree -- branch
           deriving (Eq, Show)

-- Instanța Show pentru afișarea expresiilor
instance Show Expr where
  show (Const x) = show x
  show (e1 :+: e2) = "(" ++ show e1 ++ " + " ++ show e2 ++ ")"
  show (e1 :*: e2) = "(" ++ show e1 ++ " * " ++ show e2 ++ ")"

{-
1. Scrieți o funcție `evalExp :: Expr -> Int` care evaluează o expresie.
-}
evalExp :: Expr -> Int
evalExp (Const x) = x
evalExp (e1 :+: e2) = evalExp e1 + evalExp e2
evalExp (e1 :*: e2) = evalExp e1 * evalExp e2

-- Teste pentru evalExp
exp1 = (Const 2 :*: Const 3) :+: (Const 0 :*: Const 5)
exp2 = Const 2 :*: (Const 3 :+: Const 4)
exp3 = Const 4 :+: (Const 3 :*: Const 3)
exp4 = ((Const 1 :*: Const 2) :*: (Const 3 :+: Const 1)) :*: Const 2

test11 = evalExp exp1 == 6
test12 = evalExp exp2 == 14
test13 = evalExp exp3 == 13
test14 = evalExp exp4 == 16

{-
2. Scrieți o funcție `evalArb :: Tree -> Int` care evaluează o expresie modelată sub formă de arbore.
-}
evalArb :: Tree -> Int
evalArb (Lf x) = x
evalArb (Node op left right) = case op of
    Add -> evalArb left + evalArb right
    Mult -> evalArb left * evalArb right

-- Teste pentru evalArb
arb1 = Node Add (Node Mult (Lf 2) (Lf 3)) (Node Mult (Lf 0)(Lf 5))
arb2 = Node Mult (Lf 2) (Node Add (Lf 3)(Lf 4))
arb3 = Node Add (Lf 4) (Node Mult (Lf 3)(Lf 3))
arb4 = Node Mult (Node Mult (Node Mult (Lf 1) (Lf 2)) (Node Add (Lf 3)(Lf 1))) (Lf 2)

test21 = evalArb arb1 == 6
test22 = evalArb arb2 == 14
test23 = evalArb arb3 == 13
test24 = evalArb arb4 == 16

{-
3. Scrieți o funcție `expToArb :: Expr -> Tree` care transformă o expresie în arborele corespunzător.
-}
expToArb :: Expr -> Tree
expToArb (Const x) = Lf x
expToArb (e1 :+: e2) = Node Add (expToArb e1) (expToArb e2)
expToArb (e1 :*: e2) = Node Mult (expToArb e1) (expToArb e2)


{-
## Arbori binari de căutare
Observați că tipul valorilor este `Maybe value` pentru a permite "ștergerea logică" (soft delete).
-}
data IntSearchTree value
  = Empty
  | BNode
      (IntSearchTree value)     -- subarbore stâng (chei mai mici)
      Int                       -- cheia curentă
      (Maybe value)             -- valoarea (Nothing dacă e șters)
      (IntSearchTree value)     -- subarbore drept (chei mai mari)
  deriving Show

{-
4. Scrieți o funcție `lookup'` de căutare a unui element într-un arbore.
-}
lookup' :: Int -> IntSearchTree value -> Maybe value
lookup' _ Empty = Nothing
lookup' key (BNode left k val right)
  | key == k  = val
  | key < k   = lookup' key left
  | otherwise = lookup' key right

{-
5. Scrieți o funcție care întoarce lista cheilor nodurilor dintr-un arbore de căutare.
Include și cheile nodurilor marcate ca șterse (Nothing), conform definiției structurii.
Dacă se dorește excluderea lor, trebuie filtrat. Aici returnăm toate cheile structurale.
-}
keys :: IntSearchTree value -> [Int]
keys Empty = []
keys (BNode left k _ right) = keys left ++ [k] ++ keys right

{-
6. Scrieți o funcție care întoarce lista valorilor nodurilor dintr-un arbore de căutare.
Doar valorile existente (Just v) sunt returnate.
-}
values :: IntSearchTree value -> [value]
values Empty = []
values (BNode left _ val right) = 
  values left ++ maybe [] (:[]) val ++ values right

{-
7. Scrieți o funcție de adăugare a unui element într-un arbore de căutare.
-}
insert :: Int -> value -> IntSearchTree value -> IntSearchTree value
insert key val Empty = BNode Empty key (Just val) Empty
insert key val (BNode left k v right)
  | key == k  = BNode left k (Just val) right -- Actualizăm valoarea (sau "reînviem" nodul)
  | key < k   = BNode (insert key val left) k v right
  | otherwise = BNode left k v (insert key val right)

{-
8. Scrieți o funcție care șterge (marchează ca șters) un element.
-}
delete :: Int -> IntSearchTree value -> IntSearchTree value
delete _ Empty = Empty
delete key (BNode left k v right)
  | key == k  = BNode left k Nothing right -- Soft delete
  | key < k   = BNode (delete key left) k v right
  | otherwise = BNode left k v (delete key right)

{-
9. Scrieți o funcție care întoarce lista elementelor (perechi cheie-valoare) dintr-un arbore.
-}
toList :: IntSearchTree value -> [(Int, value)]
toList Empty = []
toList (BNode left k v right) =
  toList left ++ maybe [] (\val -> [(k, val)]) v ++ toList right 

{-
10. Scrieți o funcție care să construiască un arbore dintr-o listă de perechi cheie-valoare.
-}
fromList :: [(Int, value)] -> IntSearchTree value
fromList = foldr (\(k, v) acc -> insert k v acc) Empty

{-
11. Scrieți o funcție care să producă o reprezentare liniară (string).
-}
printTree :: IntSearchTree value -> String
printTree Empty = ""
printTree (BNode left k v right) =
  let leftStr = printTree left
      rightStr = printTree right
      -- Afișăm cheia între paranteze dacă valoarea e Nothing (nod șters)
      nodeStr = case v of
                  Just _  -> show k
                  Nothing -> "(" ++ show k ++ ")"
      
      -- Helper pentru spațiere
      format s = if null s then "" else s ++ " "
  in  format leftStr ++ nodeStr ++ (if null rightStr then "" else " " ++ rightStr)

{-
## Extra: new balance
12. Scrieți o funcție care primește un arbore și întoarce arborele echilibrat.
Strategie: Convertim arborele în listă sortată (toList face asta deja prin in-order traversal),
apoi reconstruim arborele recursiv luând elementul din mijloc ca rădăcină.
-}
balance :: IntSearchTree value -> IntSearchTree value
balance tree = buildBalancedTree (toList tree)
  where
    buildBalancedTree :: [(Int, value)] -> IntSearchTree value
    buildBalancedTree [] = Empty
    buildBalancedTree xs =
      let mid = length xs `div` 2
          (leftPart, rightPart) = splitAt mid xs
          -- rightPart nu poate fi goală aici deoarece length xs > 0
          -- rightPart arată ca: ((k, v) : rest)
          ((k, v):restRight) = rightPart 
      in BNode (buildBalancedTree leftPart) k (Just v) (buildBalancedTree restRight)