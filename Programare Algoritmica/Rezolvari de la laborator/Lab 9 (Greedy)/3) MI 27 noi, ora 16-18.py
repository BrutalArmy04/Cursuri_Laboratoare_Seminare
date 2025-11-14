## Laborator 9, MI 27 noi, ora 16-18

# ## Problema 1 - minimizare timp mediu de asteptare
#
# def citire():
#     f = open("tis.txt")
#     timpi = [int(x) for x in f.read().split()]
#     f.close()
#     L = [(i + 1, x) for i, x in enumerate(timpi)]
#     return L
#
#
# def greedy(L):
#     L.sort(key=lambda t: t[1])
#     suma_servire = 0
#     suma_asteptare = 0
#     sol = []
#     for poz, t_servire in L:
#         suma_servire += t_servire
#         suma_asteptare += suma_servire
#         sol.append((poz,t_servire,suma_servire))
#
#     TMA = suma_asteptare / len(L)
#     return sol,TMA
#
# def afisare(sol,TMA):
#     print(f"{'nr_persoana'.ljust(11)}"
#           f"\t{'t_servire'.center(9)}"
#           f"\t{'t_asteptare'.rjust(11)}")
#     for nr_pers,t_servire,t_astept in sol:
#         print(f"{nr_pers:<11}\t{t_servire:^9}\t{t_astept:>11}")
#     print(f"Timpul mediu de asteptare este: {TMA:.2f}!!")
#
#
# L = citire()
# # print(L)
# sol,TMA = greedy(L)
# # print(sol)
# # print(TMA)
# afisare(sol,TMA)



# ## Problema 2 - Programare spectacole intr-o singura sala
#
# def citire():
#     f = open("spectacole.txt", "r")
#     L = []
#     for linie in f:
#         ore, nume = linie.strip().split(maxsplit=1)
#         inceput, sfarsit = ore.split("-")
#         L.append((inceput, sfarsit, nume))
#     f.close()
#     return L
#
#
# def greedy(L):
#     L.sort(key=lambda t: t[1])  # cresc dupa ora de sfarsit
#     sol = [L[0]]
#     # for t in L[1:]: # se creeaza o lista noua (extra spatiu)
#     #     if t[0] >= sol[-1][1]:
#     #         sol.append(t)
#
#     # var pe pozitii
#     for i in range(1, len(L)):
#         if L[i][0] >= sol[-1][1]:
#             sol.append(L[i])
#
#     return sol
#
#
# def afisare(sol):
#     g = open("programare.txt", "w")
#     for inceput, sfarsit, nume in sol:
#         g.write(f"{inceput}-{sfarsit} {nume}\n")
#     g.close()
#
#
# L = citire()
# print(L)
# sol = greedy(L)
# afisare(sol)

