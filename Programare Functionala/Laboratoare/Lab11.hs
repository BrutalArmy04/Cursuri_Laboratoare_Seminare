{-
# Laborator 11 - Functori

Scrieți instanțe ale clasei `Functor` pentru tipurile de date descrise mai jos.
Hint: e posibil să fie nevoie să adăugați unele constrângeri la definirea instanțelor (ex: `Functor g => ...`).
-}

module Lab11 where

import Prelude hiding (fmap, Functor)

-- Definiția clasei Functor (pentru a nu intra în conflict cu cea din Prelude)
class Functor f where
    fmap :: (a -> b) -> f a -> f b

-- 1. Identity
newtype Identity a = Identity a
    deriving Show

instance Functor Identity where
    fmap f (Identity a) = Identity (f a)

-- 2. Pair
data Pair a = Pair a a
    deriving Show

instance Functor Pair where 
    fmap f (Pair a b) = Pair (f a) (f b)

-- 3. Constant
data Constant a b = Constant b
    deriving Show

instance Functor (Constant a) where
    fmap f (Constant b) = Constant (f b)

-- 4. Two
data Two a b = Two a b
    deriving Show

instance Functor (Two a) where
    fmap f (Two a b) = Two a (f b)

-- 5. Three
data Three a b c = Three a b c
    deriving Show

instance Functor (Three a b) where
    fmap f (Three a b c) = Three a b (f c)

-- 6. Three'
data Three' a b = Three' a b b
    deriving Show

instance Functor (Three' a) where
    fmap f (Three' a b1 b2) = Three' a (f b1) (f b2)

-- 7. Four
data Four a b c d = Four a b c d
    deriving Show

instance Functor (Four a b c) where
    fmap f (Four a b c d) = Four a b c (f d)

-- 8. Four''
data Four'' a b = Four'' a a a b
    deriving Show

instance Functor (Four'' a) where
    fmap f (Four'' a1 a2 a3 b) = Four'' a1 a2 a3 (f b)

-- 9. Quant
data Quant a b = Finance | Desk a | Bloor b
    deriving Show

instance Functor (Quant a) where
    fmap _ Finance = Finance
    fmap _ (Desk a) = Desk a
    fmap f (Bloor b) = Bloor (f b)

-- 10. LiftItOut
data LiftItOut f a = LiftItOut (f a)
    deriving Show

instance Functor f => Functor (LiftItOut f) where
    fmap f (LiftItOut fa) = LiftItOut (fmap f fa)

-- 11. Parappa
data Parappa f g a = DaWrappa (f a) (g a)
    deriving Show

instance (Functor f, Functor g) => Functor (Parappa f g) where
    fmap f (DaWrappa fa ga) = DaWrappa (fmap f fa) (fmap f ga)

-- 12. IgnoreOne
data IgnoreOne f g a b = IgnoringSomething (f a) (g b)
    deriving Show

instance Functor g => Functor (IgnoreOne f g a) where
    fmap f (IgnoringSomething fa gb) = IgnoringSomething fa (fmap f gb)

-- 13. Notorious
data Notorious g o a t = Notorious (g o) (g a) (g t)
    deriving Show

instance Functor g => Functor (Notorious g o a) where
    fmap f (Notorious go ga gt) = Notorious go ga (fmap f gt)

-- 14. GoatLord
data GoatLord a = NoGoat | OneGoat a | MoreGoats (GoatLord a) (GoatLord a) (GoatLord a)
    deriving Show

instance Functor GoatLord where
    fmap _ NoGoat = NoGoat
    fmap f (OneGoat a) = OneGoat (f a)
    fmap f (MoreGoats g1 g2 g3) = MoreGoats (fmap f g1) (fmap f g2) (fmap f g3)

-- 15. TalkToMe
data TalkToMe a = Halt | Print String a | Read (String -> a)

instance Show a => Show (TalkToMe a) where
    show Halt = "Halt"
    show (Print s a) = "Print " ++ s ++ " " ++ show a
    show (Read _) = "Read (Function)"

instance Functor TalkToMe where
    fmap _ Halt = Halt
    fmap f (Print s a) = Print s (f a)
    fmap f (Read g) = Read (f . g)