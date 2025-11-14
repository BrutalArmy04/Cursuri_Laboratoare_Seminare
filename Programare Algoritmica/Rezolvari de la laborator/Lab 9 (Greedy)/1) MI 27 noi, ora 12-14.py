## Laborator 9, MI 27 noi, ora 12-14

# ## Problema 1 - minimizarea timpului mediu de asteptare
# def citire():
#     f = open("tis.txt")
#     L_timpi = [int(x) for x in f.read().split()]
#     f.close()
#     L_persoane = [(i + 1, v) for i, v in enumerate(L_timpi)]
#     # L_persoane=[(i+1,L_timpi[i]) for i in range(len(L_timpi))]
#     return L_persoane
#
#
# def afisare_timp_servire(L_persoane):
#     L_timpi_sortati = sorted(L_persoane, key=lambda t: t[1])
#     suma_timpi_servire = 0
#     suma_timpi_asteptare = 0
#     SOL = []
#     for nr_ord, t_servire in L_timpi_sortati:
#         suma_timpi_servire += t_servire
#         suma_timpi_asteptare += suma_timpi_servire
#         SOL.append((nr_ord, t_servire, suma_timpi_servire))
#     t_mediu_asteptare = suma_timpi_asteptare / len(L_persoane)
#     return SOL, t_mediu_asteptare
#
# def afisare(L, tma):
#     a,b,c=len('nr_persoana'),len("t_servire"),len('t_asteptare')
#
#     print(f"{'nr_persoana'.ljust(a)}"
#           f"\t{'t_servire'.center(b)}"
#           f"\t{'t_asteptare'.rjust(c)}")
#
#     for nr_persoana, t_servire,t_asteptare in L:
#         print(f"{nr_persoana:<11}\t{t_servire:^9}\t {t_asteptare:>11}")
#     print(f"Timpul mediu de asteptare este: {tma:.2f}")
#
#
# L = citire()
# print(L)
# G, tma = afisare_timp_servire(L)
# print(G)
# afisare(G, tma)


# ## Problema 2 - planificarea optima a unor spectacole
# # intr-o singura sala
#
#
# def citire():
#     with open("spectacole.txt", "r") as f:
#         L = []
#         for linie in f:
#             ore,nume = linie.strip().split(' ', 1)
#             inceput, sfarsit = ore.split('-')
#             L.append((inceput, sfarsit, nume))
#         return L
#
#
# def greedy(L):
#     L.sort(key=lambda t:t[1]) #crescator dupa ora sfarsit
#     sol = [L[0]]
#     for i in range(1, len(L)):
#         if L[i][0] >= sol[-1][1]:
#             sol.append(L[i])
#     return sol
#
#
# def afisare(L):
#     with open("programare.txt", "w") as g:
#         for inceput,sfarsit,nume in L:
#             g.write(f"{inceput}-{sfarsit} {nume}\n")
#
#
# L = citire()
# print(L)
# G = greedy(L)
# print(G)
# afisare(G)


# ## problema 3 - turn cuburi
#
# def citire():
#     f = open("cuburi.txt")
#     nr_cuburi = int(f.readline())
#     cuburi = []
#     for line in f:
#         latura, culoare = line.strip().split()
#         cuburi += [(int(latura), culoare)]
#     f.close()
#     return cuburi
#
#
# def Greedy(L_cuburi):
#     L_cuburi.sort(reverse=True)  # descrescator dupa laturi
#     sol = [L_cuburi[0]]
#     h_turn = L_cuburi[0][0]
#     for i in range(1, len(L_cuburi)):
#         if L_cuburi[i][1] != sol[-1][1]:
#             sol.append(L_cuburi[i])
#             h_turn += L_cuburi[i][0]
#     return sol, h_turn
#
#
# def afisare(SOL, h):
#     with open("turn.txt", 'w') as g:
#         for latura, culoare in SOL:
#             g.write(f"{latura} {culoare}\n")
#         g.write(f"\nInaltimea totala: {h}")
#
#
# L_cuburi = citire()
# print(L_cuburi)
# SOL, h = Greedy(L_cuburi)
# afisare(SOL, h)

