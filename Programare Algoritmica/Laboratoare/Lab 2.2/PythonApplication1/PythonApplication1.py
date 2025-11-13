lungime, latime = input('lungime, latime =').split()
lungime, latime = int(lungime), int(latime)
x = lungime
y = latime
while x!=y:
    if (x > y):
        x -= y
    else:
        y -= x
print(f'Folosim {lungime*latime/x} placi patrate de latura {x}')

