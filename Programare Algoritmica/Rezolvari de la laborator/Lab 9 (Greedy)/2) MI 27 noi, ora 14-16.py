## Laborator 9, MI 27 noi, ora 14-16

# ## Grupa 132, pb 3 din seminar 4 (cea cu csv)
#
# ## a)
# def citire(nume):
#     f = open(nume, "r")
#     L_stud = []
#     for linie in f:
#         aux = linie.split(",")
#         L_stud += [(aux[0], int(aux[1]),
#                     tuple(int(nota) for nota in aux[2:]))]
#     f.close()
#     return L_stud
#
# def promovat(L_stud, nr_min_credite=15):
#     for i in range(len(L_stud)):
#         if 0 not in L_stud[i][2] and sum(L_stud[i][2]) >= nr_min_credite:
#             L_stud[i] = L_stud[i] + (True,)
#         else:
#             L_stud[i] = L_stud[i] + (False,)
#
# def criteriu_1(t):
#     return t[1], t[0]
#
# def criteriu_2(t):
#     return -t[3], t[0]
#
# def criteriu_3(t):
#     return -sum(t[2]), t[1], t[0]
#
# def criteriu_4(t):
#     return t[1], -t[3], -sum(t[2]), t[0]
#
#
# stud = citire("studenti.csv")
# print(stud)
# # promovat(stud, 14)
# promovat(stud)
# print(stud)
#
# print(sorted(stud, key=criteriu_1), "\n")
#
# print(sorted(stud, key=criteriu_2), "\n")
#
# print(sorted(stud, key=criteriu_3), "\n")
#
# print(sorted(stud, key=criteriu_4), "\n")
#
## print(sorted([-True, -False]))


## GREEDY


# ## Problema 1 - Minimizarea timpului mediu de asteptare
#
# def citire():
#     f = open("tis.txt", "r")
#     L_pers = [(i + 1, int(x))
#               for i, x in enumerate(f.readline().split())]
#     return L_pers
#
# def greedy(L_pers):
#     L_sorted_pers = sorted(L_pers, key=lambda t: t[1])
#     suma_timpi_servire = 0
#     suma_timpi_asteptare = 0
#     L_sol = []
#     for nr_ord, t_servire in L_sorted_pers:
#         suma_timpi_servire += t_servire
#         suma_timpi_asteptare += suma_timpi_servire
#         L_sol += [(nr_ord, t_servire, suma_timpi_servire)]
#
#     ma = suma_timpi_asteptare / len(L_pers)
#     return L_sol, ma
#
# def afisare(L_pers, tma):
#     print(f"{'nr_persoana'.ljust(11)}"
#           f"\t{'t_servire'.center(9)}"
#           f"\t{'t_asteptare'.rjust(11)}")
#     for nr_persoana, t_servire, t_asteptare in L_pers:
#         print(f"{nr_persoana:<11}\t{t_servire:^9}\t{t_asteptare:>11}")
#     print(f"Timpul mediu de asteptare este: {tma:.2f}.")
#
#
# pers = citire()
# print(pers)
#
# sol, ma = greedy(pers)
# print(ma)
#
# afisare(sol, ma)


# ## Problema 2 - Programarea spectacolelor intr-o sala
#
# def citire():
#     f = open("spectacole.txt", "r")
#     L_spec = []
#     for linie in f:
#         ore, nume= linie.strip().split(" ", 1)
#         inceput, sfarsit = ore.split("-")
#         L_spec += [(inceput, sfarsit, nume)]
#     f.close()
#     return L_spec
#
# def greedy(L_spec):
#     L_spec.sort(key= lambda t: t[1])
#     solutie = [L_spec[0]]
#     for poz in range(1, len(L_spec)):
#         if L_spec[poz][0] >= solutie[-1][1]:
#             solutie += [L_spec[poz]]
#     return solutie
#
#
# def afisare(L_spec):
#     g = open("programare.txt", "w")
#     for inceput, sfarsit, nume in L_spec:
#         g.write(f"{inceput}-{sfarsit} {nume}\n")
#     g.close()
#
# spec = citire()
# print(spec)
# rez = greedy(spec)
# afisare(rez)


# ## pb3 - turn de cuburi
# 
# def citire():
#     f = open("cuburi.txt", "r")
#     nr_cuburi = int(f.readline())
#     L_cuburi = []
#     for linie in f:
#         latura, culoare = linie.strip().split()
#         L_cuburi += [(int(latura), culoare)]
# 
#     return L_cuburi
# 
# 
# def greedy(L_cuburi):
#     L_cuburi.sort(reverse=True)  # descrescator dupa latura
#     solutie = [L_cuburi[0]]
#     h_turn = L_cuburi[0][0]
#     for poz in range(1, len(L_cuburi)):
#         if L_cuburi[poz][1] != solutie[-1][1]:
#             solutie += [L_cuburi[poz]]
#             h_turn += L_cuburi[poz][0]
# 
#     return solutie, h_turn
# 
# 
# def afisare(L_cuburi, h):
#     g = open("turn.txt", "w")
#     for latura, culoare in L_cuburi:
#         g.write(f"{latura} {culoare}\n")
#     g.write(f"\nInaltime totala: {h}")
# 
# 
# cuburi = citire()
# print(cuburi)
# 
# turn, h = greedy(cuburi)
# 
# afisare(turn, h)

