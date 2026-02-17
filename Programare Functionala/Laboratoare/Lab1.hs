{-
# Laborator 1 - Introducere în Haskell

Pentru început, vă veți familiariza cu mediul de programare GHC (Glasgow Haskell Compiler). 
Acesta include două componente: GHCi (un interpretor) și GHC (un compilator).

## Descărcare și instalare

### Instrucțiuni instalare Haskell folosind GHCup
GHCup permite dezvoltatorilor să instaleze versiuni ale GHC și să gestioneze proiecte.
Haskell Toolchain este format din:
- GHC
- Cabal (gestionare proiecte/dependințe)
- HLS (Haskell Language Server - erori și sugestii)
- Stack (gestionare proiecte cu versiuni diferite)

Instrucțiuni: https://www.haskell.org/ghcup/

### IDE
Recomandăm VSCode cu extensia Haskell sau orice editor text.
Stil recomandat: https://github.com/tibbe/haskell-style-guide/blob/master/haskell-style.md

## GHCi (Interpretor)

Comenzi utile în terminal (`ghci`):
- Expresii matematice: `2+3`
- Boolean: `False || True`
- Liste: `head [1,2,3]`

Comenzi GHCi (precedate de ":"):
:?  - help
:q  - quit
:cd - change directory
:t  - type (ex: `:t True`)
:l  - load file
:r  - reload file

-------------------------------------------------------------------------------
## SECȚIUNEA DE COD (REZOLVARE)
Mai jos sunt definițiile cerute în laborator pentru fișierul sursă.
-------------------------------------------------------------------------------
-}

-- 1. Definiția numărului mare (myInt)
-- Acest număr depășește capacitatea unui integer standard pe 64 de biți, 
-- dar Haskell gestionează automat numere mari (Integer).
myInt :: Integer
myInt = 31415926535897932384626433832795028841971693993751058209749445923

-- 2. Funcția double
-- Primește un Integer și returnează dublul acestuia.
double :: Integer -> Integer
double x = x + x

-- 3. Funcția triple
-- Cerință: "Adăugați o funcție triple fișierului lab1.hs".
-- Aceasta folosește funcția `double` definită anterior.
triple :: Integer -> Integer
triple x = double x + x

{-
-------------------------------------------------------------------------------
## Instrucțiuni de testare a codului de mai sus:

1. Salvați acest fișier (de exemplu `Lab1Complet.hs`).
2. Deschideți terminalul în directorul fișierului.
3. Porniți GHCi: `ghci`
4. Încărcați fișierul: `:l Lab1Complet.hs`
5. Testați funcțiile:
   *Main> double myInt
   *Main> triple myInt
   *Main> double 2000

## Resurse Suplimentare

Hoogle (Motor de căutare API Haskell):
https://hoogle.haskell.org/

Carte recomandată:
"Learn You a Haskell for Great Good!" - Capitolul Introductiv
https://learnyouahaskell.com/introduction
-}