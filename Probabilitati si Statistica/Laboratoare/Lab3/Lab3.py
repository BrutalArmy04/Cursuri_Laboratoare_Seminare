import numpy as np
#Ex 1

a = 1
b = 10
c = 3
d = 5
nrbune = 0
rap = (d-c)/(b-a)

for num in range(10000):
    x =  (np.random.random())*(b-a) + a
    if x>=c and x<=d:
        nrbune+=1
        print(x)


print(nrbune/10000)
print(rap)


#Ex 2

import numpy as np

def rho(theta):
    return 3 + np.cos(4 * theta)

def is_in_Omega(x, y, rho):
    may_theta = np.arctan2(y, x)
    return np.linalg.norm(np.array([x, y])) <= (rho(may_theta))

r = 4
l = 2 * r
num = 10000
nr_true = 0
nr_false = 0

x = (np.random.random())*(8) - 4
y = (np.random.random())*(8) - 4

for i in range(num):
    x = (np.random.random())*(8) - 4
    y = (np.random.random())*(8) - 4
    if is_in_Omega(x, y, rho):
        nr_true += 1

print(nr_true/num)

#Ex 6
import numpy as np
l = 5
num = 1000000

nr_true = 0
for num in range(num):
    x = (np.random.random()) * (l*2) # unde pun chibrit
    y = (np.random.random()) * np.pi # unghiul chibritului
    offset = (l/2) * np.sin(y)
    if not(x + offset <=(2*l) and x - offset >=0):
        nr_true+=1
print(num/nr_true)






