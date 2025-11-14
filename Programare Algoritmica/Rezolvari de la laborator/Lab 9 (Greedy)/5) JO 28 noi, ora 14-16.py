## Laborator 9, JO 28 noi, ora 14-16

# ## Problema 1 - Minimizarea timpului mediu de așteptare
#
# def citire():
#     with open("tis.txt", "r") as f:
#         L = [(i + 1, int(x))
#              for i, x in enumerate(f.readline().split())]
#         return L
#
#
# def greedy(L):
#     L.sort(key=lambda t: t[1])
#     G = []
#     suma_t_servire = 0
#     suma_t_asteptare = 0
#     for poz, t_servire in L:
#         suma_t_servire += t_servire
#         suma_t_asteptare += suma_t_servire
#         G.append((poz,t_servire,suma_t_servire))
#     tma=suma_t_asteptare/len(G)
#     return G,tma
#
# def afisare(G,tma):
#     print(f"{'nr_persoana'.ljust(11)}"
#           f"\t{'t_servire'.center(9)}"
#           f"\t{'t_asteptare'.rjust(11)}")
#
#     for poz,t_servire,t_asteptare in G:
#         print(f"{poz:<11}\t{t_servire:^9}\t{t_asteptare:>11}")
#     print(f"Timpul mediu de asteptare este {tma:.2f}")
#
#
# L = citire()
# # print(L)
# G,tma=greedy(L)
# afisare(G,tma)

# ## Problema 2 - nr maxim spectacole intr-o sala
#
# def citire():
#     with open("spectacole.txt", "r") as f:
#         L = []
#         for linie in f:
#             ore, nume = linie.strip().split(maxsplit=1)
#             inceput, sfarsit = ore.split('-')
#             L.append((inceput, sfarsit, nume))
#         return L
#
#
# def greedy(L):
#     L.sort(key=lambda t: t[1])  # crescator dupa ora de sfarsit
#     G = [L[0]]
#     # for spectacol in L[1:] -> s-ar crea o lista noua: prea mult spatiu folosit
#     for i in range(1, len(L)):
#         if L[i][0] >= G[-1][1]:
#             G.append(L[i])
#     return G
#
#
# def afisare(G):
#     with open("programare.txt", "w") as g:
#         for inceput, sfarsit, nume in G:
#             g.write(f'{inceput}-{sfarsit} {nume}\n')
#
#
# L = citire()
# G = greedy(L)
# afisare(G)

