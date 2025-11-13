import numpy as np
import matplotlib.pyplot as plt

def intersecteaza(A, B):
    return np.linalg.norm(np.array(A)-np.array(B))>=3**0.5


a = (np.random.random())*2*np.pi
b = (np.random.random())*2*np.pi
A = (np.cos(a), np.sin(a))
B = (np.cos(b), np.sin(b))
#Plotare in python (cu matplotlib)
#plt.plot([A[0], B[0]] (x-urile),[A[1], B[1]] (y-urile)) 
#plt.show()
#plt.plot([A[0], B[0]],[A[1], B[1]]) 

#gca() = get current axis
plt.gca().set_xlim(-1.05, 1.05)
plt.gca().set_ylim(-1.05, 1.05)
plt.gca().set_aspect(1) #am facut aici cutia
#fac cercuri
circle = plt.Circle((0,0), 1, color='b', fill=False, linewidth = 3)
plt.gca().add_patch(circle)

small_circle = plt.Circle((0,0), 0.5, color='g', fill=False, linewidth = 3)
plt.gca().add_patch(small_circle)
#print(intersecteaza(A, B))
num = 10000
nr_true = 0
nr_false = 0
for i in range(num):
    a = (np.random.random())*2*np.pi
    b = (np.random.random())*2*np.pi
    A = (np.cos(a), np.sin(a))
    B = (np.cos(b), np.sin(b))
    if intersecteaza(A, B) == True:
        nr_true+=1
    else:
        nr_false+=1
    #print(intersecteaza(A, B))
    plt.plot([A[0], B[0]],[A[1], B[1]]) 

#print(nr_true, nr_false)
#print(nr_true/(nr_true+nr_false))
plt.show() # cu asta afisez plotul
nr_puncte = 0
nr_pct_bune = 0
#something else
while (nr_puncte < num):
    
    p1 = (np.random.random())
    p2 = (np.random.random())
    if(np.linalg.norm(np.array([p1, p2]))<=1):
        #pastrez (p1, p2)
        nr_puncte+=1
        if(np.linalg.norm(np.array([p1, p2]))<=0.5):
            nr_pct_bune+=1
print(nr_pct_bune/num)
