# Citirea datelor
n = int(input("Introduceți numărul de spectacole: "))
spectacole = []


for i in range(n):
# Citim o linie, o despărțim după spații și convertim în întregi
    date = input().split()
    start = int(date[0])
    final = int(date[1])
    # Adăugăm un tuplu de forma (ID, start, final)
    spectacole.append((i + 1, start, final))


# Căutăm la fiecare pas minimul din porțiunea nesortată a listei
for i in range(len(spectacole) - 1):
    min_idx = i
    for j in range(i + 1, len(spectacole)):
        # Comparăm după ora de final (indexul 2 din tuplu: (id, start, final))
        if spectacole[j][2] < spectacole[min_idx][2]:
            min_idx = j
           
    # Dacă am găsit un spectacol care se termină mai devreme, interschimbăm (swap)
    if min_idx != i:
        spectacole[i], spectacole[min_idx] = spectacole[min_idx], spectacole[i]




# Pasul Greedy: Alegem primul spectacol sortat
alese = [spectacole[0]]


# Verificăm restul spectacolelor
for i in range(1, len(spectacole)):
    # spectacole[i][1] este ora de start a spectacolului analizat
    # alese[-1][2] este ora de final a ultimului spectacol adăugat
    if spectacole[i][1] >= alese[-1][2]:
        alese.append(spectacole[i])


# Afișarea datelor
print("Spectacolele alese sunt:", end=" ")
for sp in alese:
    print(sp[0], end=" ")


print(f"\nNumărul de spectacole este {len(alese)}") # Se putea face și cum am făcut la C++, dar am ales să folosesc proprietățiile limbajului