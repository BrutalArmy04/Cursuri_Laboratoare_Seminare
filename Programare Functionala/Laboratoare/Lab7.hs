data Expr = Const Int -- integer constant
          | Expr :+: Expr -- addition
          | Expr :*: Expr -- multiplication
           deriving Eq

data Operation = Add | Mult deriving (Eq, Show)

data Tree = Lf Int -- leaf
          | Node Operation Tree Tree -- branch
           deriving (Eq, Show)

instance Show Expr where
  show :: Expr -> String
  show (Const x) = show x
  show (e1 :+: e2) = "(" ++ show e1 ++ " + "++ show e2 ++ ")"
  show (e1 :*: e2) = "(" ++ show e1 ++ " * "++ show e2 ++ ")"


--1

evalExp :: Expr -> Int
evalExp (Const x) = x
evalExp (e1 :+: e2) = evalExp e1 + evalExp e2
evalExp (e1 :*: e2) = evalExp e1 * evalExp e2

exp1 = (Const 2 :*: Const 3) :+: (Const 0 :*: Const 5)
exp2 = Const 2 :*: (Const 3 :+: Const 4)
exp3 = Const 4 :+: (Const 3 :*: Const 3)
exp4 = ((Const 1 :*: Const 2) :*: (Const 3 :+: Const 1)) :*: Const 2
test11 = evalExp exp1 == 6
test12 = evalExp exp2 == 14
test13 = evalExp exp3 == 13
test14 = evalExp exp4 == 16

--2

evalArb :: Tree -> Int
evalArb = (\arb -> case arb of
                Lf x -> x
                Node op left right -> case op of
                                        Add -> evalArb left + evalArb right
                                        Mult -> evalArb left * evalArb right)


arb1 = Node Add (Node Mult (Lf 2) (Lf 3)) (Node Mult (Lf 0)(Lf 5))
arb2 = Node Mult (Lf 2) (Node Add (Lf 3)(Lf 4))
arb3 = Node Add (Lf 4) (Node Mult (Lf 3)(Lf 3))
arb4 = Node Mult (Node Mult (Node Mult (Lf 1) (Lf 2)) (Node Add (Lf 3)(Lf 1))) (Lf 2)

test21 = evalArb arb1 == 6
test22 = evalArb arb2 == 14
test23 = evalArb arb3 == 13
test24 = evalArb arb4 == 16

--3

expToArb :: Expr -> Tree
expToArb (Const x) = Lf x
expToArb (e1 :+: e2) = Node Add (expToArb e1) (expToArb e2)
expToArb (e1 :*: e2) = Node Mult (expToArb e1) (expToArb e2)

--4

data IntSearchTree value
  = Empty
  | BNode
      (IntSearchTree value)     -- elemente cu cheia mai mica
      Int                       -- cheia elementului
      (Maybe value)             -- valoarea elementului
      (IntSearchTree value)     -- elemente cu cheia mai mare

lookup' :: Int -> IntSearchTree value -> Maybe value
lookup' _ Empty = Nothing
lookup' key (BNode left k val right)
  | key == k = val
  | key < k  = lookup' key left
  | otherwise = lookup' key right

--5

keys :: IntSearchTree value -> [Int]
keys Empty = []
keys (BNode left k _ right) = keys left ++ [k] ++ keys right

--6

values :: IntSearchTree value -> [value]
values Empty = []
values (BNode left k val right) = 
  values left ++ maybe [] (:[]) val ++ values right

--7

insert :: Int -> value -> IntSearchTree value -> IntSearchTree value
insert key val Empty = BNode Empty key (Just val) Empty
insert key val (BNode left k v right)
  | key == k = BNode left k (Just val) right
  | key < k  = BNode (insert key val left) k v right
  | otherwise = BNode left k v (insert key val right)

--8

delete :: Int -> IntSearchTree value -> IntSearchTree value
delete _ Empty = Empty
delete key (BNode left k v right)
  | key == k = BNode left k Nothing right
  | key < k  = BNode (delete key left) k v right
  | otherwise = BNode left k v (delete key right)

--9

toList :: IntSearchTree value -> [(Int, value)]
toList Empty = []
toList (BNode left k v right) =
  toList left ++ maybe [] (\val -> [(k, val)]) v ++ toList right 

--10

fromList :: [(Int, value)] -> IntSearchTree value
fromList = foldr (\(k, v) acc -> insert k v acc) Empty

--11  

printTree :: IntSearchTree value -> String
printTree Empty = ""
printTree (BNode left k v right) =
  let leftStr = printTree left
      rightStr = printTree right
      valStr = case v of
                 Just _  -> show k
                 Nothing -> "(" ++ show k ++ ")"
  in  (if leftStr /= "" then leftStr ++ " " else "") ++ valStr ++ (if rightStr /= "" then " " ++ rightStr else "")

--12

balance :: IntSearchTree value -> IntSearchTree value
balance tree = buildBalancedTree (toList tree)
  where
    buildBalancedTree [] = Empty
    buildBalancedTree xs =
      let mid = length xs `div` 2
          (leftList, (k, v):rightList) = splitAt mid xs
      in BNode (buildBalancedTree leftList) k (Just v) (buildBalancedTree rightList)