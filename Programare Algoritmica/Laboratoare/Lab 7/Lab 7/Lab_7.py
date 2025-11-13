# #Prob 1
# def citire():
#     n = int(input('n= '))
#     L=[]
#     for i in range(n):
#         L.append(int(input(f'L[{i}]= ')))
#     return n, L

# def cautare(s, x, i = 0, j = None):
#     if j is None:
#         j = len(s)
#     for y in range(i, j):
#         if s[y] == x:
#             return y
#     return -1

# n, L = citire()
# for poz in range(n-1):
#     if cautare(L, L[poz], poz+1, poz+2)!= -1:
#         print('nu')
#         break
# else:
#     print('da')


# #Prob 2
# # def cifmaxim(*numere):
# #     return int("".join([max(str(x)) for x in numere]))

# # def baza2(a, b, c):
# #     return cifmaxim(a, b, c) == 111


# # print(baza2(10001, 100111, 111))
# Prob 3
# def cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
#     cuv = cuv.lower()
#     with open(nume_fis_out, 'w') as g:
#         for nume in nume_fis_in:
#             L = [] #indecsii liniilor
#             with open(nume, 'r') as f:
#                 for i, linie in enumerate(f):
#                     L_cuvinte = [c.strip("!.:;?") for c in linie.lower().replace('-', ' ').split()]
#                     if cuv in L_cuvinte:
#                         L.append(i + 1)
#             g.write(f'{nume} {'Cuvantul nu a fost gasit' if L==[] else " ".join([str(x) for x in L])}\n')
# cautare_cuvant("AlBastrA","rez.txt", "eminescu.txt", "paunescu.txt")
# Prob 4


