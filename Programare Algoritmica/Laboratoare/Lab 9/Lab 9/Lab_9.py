
# #Prob 1

# def citire():
#     with open("tis.txt", 'r') as f:
#         L = [(i+1, int(x))for i, x in enumerate(f.readline().split())]
#         return L

# def greedy(L):
#     L.sort(key = lambda t: t[1])
#     G=[]
#     suma_t_servire=0
#     suma_t_asteptare=0
#     for poz, t_servire in L:
#         suma_t_servire+=t_servire
#         suma_t_asteptare+=suma_t_servire
#         G.append((poz, t_servire, suma_t_servire))
#     tma=suma_t_asteptare/len(G)
#     return G, tma

# def afisare(G, tma):
#     print(f"{'nr_persoana'.ljust(1)}\t{'t_servire'.center(9)}\t{'t_asteptare'.rjust(11)}")
#     for poz, t_servire, t_asterpare in G:
#         print(f"{poz:<11}\t{t_servire:^9}\t{t_asterpare:>11}")
#     print(f'Timpul de asteptare mediu este {tma:.2f}')

# L = citire()
# G, tma = greedy(L)
# afisare(G, tma)

#Prob 2

# def citire():
#     with open ('Spectacole.txt', 'r') as f:
#         L = []
#         for linie in f:
#             ore, nume = linie.strip().split(maxsplit = 1)
#             inceput, sfarsit = ore.split('-')
#             L.append((inceput, sfarsit, nume))
#         return L

# def greedy(L):
#     L.sort(key = lambda t: t[1])
#     G = [L[0]]
#     for i in range(1, len(L)):
#         if L[i][0] >= G[-1][1]:
#             G.append(L[i])
#     return G

# def afisare(G):
#     with open ("programare.txt", 'w') as g:
#         for inceput, sfarsit, nume in G:
#             g.write(f'{inceput}-{sfarsit} {nume}\n')
# L = citire()
# G = greedy(L)
# afisare(G)

#Prob 3

# def citire():
#     with open('cuburi.txt') as f:
#         L=[]
#         n = None
#         for linie in f:
#             if n == None:
#                 n = int(linie)
#             else:
#                 size, color = linie.strip().split()
#                 L.append((int(size), color))
#         return n, L

# def greedy(L):
#     L.sort(key = lambda t: -t[0])
#     G = []
#     G.append(L[0])
#     s = L[0][0]
#     for i in range(1, n):
#         if G[-1][1] != L[i][1]:
#             G.append(L[i])
#             s+=L[i][0]
#     return G,s

# def afisare(G, s):
#     with open('turn.txt', 'w') as g:
#         for size, color in G:
#             g.write(f'{size} {color}\n')
#         g.write(f'\nInaltimea totala: {s}')




# n, L = citire()
# G, s = greedy(L)
# afisare(G, s)

#Prob 4

# def citire():
#     with open('bani.txt', 'r') as f:
#         bani = []
#         b = f.readline()
#         s = int(f.readline())
#         bani = [int(x) for x in b.strip().split()]
#         return bani, s

# def greedy(bani, s):
#     bani.sort(key = lambda x: -x)
#     suma=f'{s} = '
#     for ban in bani:
#         if ban<=s:
#             nr = s//ban
#             if ban!=1:
#                 suma+= f'{ban} * {nr} + '
#             else:
#                 suma+= f'{ban} * {nr}'
#             s-=ban*nr

#     return suma


# def afisare(suma):
#      with open('plata.txt', 'w') as g:
#         g.write(suma)

# bani, s = citire()
# suma = greedy(bani,s)
# afisare(suma)

#Prob 5

# def citire():
#     n = int(input('n = '))
#     h = int(input('h = '))
#     l = []
#     for i in range(n):
#         m = int(input(f'l[{i}] = '))
#         l.append(m)
#     return n, h, l

# n, h, l = citire()

# def greedy(n, h, l):
#     g = []
#     l.sort()
#     i = 0
#     j = 1
#     while j<n:
#         if l[j]-l[i]>=h:
#             i += 1
#             j += 1
#         else:
#             g.append((l[i], l[j]))
#             i += 2
#             j += 2
#     return g

# print(greedy(n, h, l))

