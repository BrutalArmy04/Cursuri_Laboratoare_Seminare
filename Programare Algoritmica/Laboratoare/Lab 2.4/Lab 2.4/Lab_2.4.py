a, b = input('a, b= ').split()
a, b = int(a), int(b)
for num in range (0, 100, 5):
    if not(a<num<b):
        print(num, end = ' ')
print('\n')
for num in range (95, -1, -5):
    if not(a<num<b):
        print(num, end = ' ')
