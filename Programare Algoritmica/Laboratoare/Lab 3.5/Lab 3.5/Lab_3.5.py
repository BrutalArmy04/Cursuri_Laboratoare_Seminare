prop = "Mancare Ana ;are. mere si mancare sau >are,"
s = "are"
t = "VREA"
poz = prop.find(s)
while poz != -1:
    if ((poz == 0 or prop[poz-1] == ",.:;? ") and (poz + len(s) == len(prop))) or s[poz + len(s)] == " ,.:;?":
        prop = prop[:poz] + t + prop[poz + len(s):]
        prop = prop.find(s, poz + len(t))
    else:
        poz = prop.find(s, poz, len(s))
print(prop)