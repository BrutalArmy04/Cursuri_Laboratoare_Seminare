prop = "Problemele cu siruri de caracteger nu sunt ggerle!"
t = "ger"
s= "re"
prop2 = prop.replace(t, s)
#print(prop2)
nr_inlocuiri = int(input('nr_inlocuiri = '))
nr_aparitii = prop.count(t)
prop3 = prop.replace(t, s, nr_inlocuiri)
print(prop3)
if nr_aparitii <= nr_inlocuiri:
    print('Toate greselile au fost corectate')
else:
    print(f'Sirul "{prop}" contine prea multe greseli. Au fost corectate doar {nr_inlocuiri}')
