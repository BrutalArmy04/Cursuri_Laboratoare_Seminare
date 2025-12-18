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




#######################################################

#Rezolvare oficiala

import numpy as np
import matplotlib.pyplot as plt

EXERCISE=2

if EXERCISE==1:
    a=2
    b=7
    c=3
    d=5

    NUM=10000

    cnt=0

    for _ in range(NUM):
        r=a+np.random.random()*(b-a)

        if r>=c and r<=d:
            cnt+=1

    print('Probabilitatea empirică este: ',cnt/NUM)

if EXERCISE==2:

    R=4

    rho1=lambda theta: R

    rho2=lambda theta: 3+np.cos(4*theta)

    rho=rho2

    NUM=10000

    cnt=0

    for _ in range(NUM):
        x=-R+2*R*np.random.random()
        y=-R+2*R*np.random.random()

        P=np.array([x,y]) #punctul P arbitrar în pătratul de latură 2R

        r=np.linalg.norm(P)
        th=np.arctan2(y,x)

        if r<=rho(th):
            cnt+=1


    prob=cnt/NUM
    print('Probabilitatea empirică de a nimeri înăuntru: ',prob)
    print('Aria este aproximativ:', prob*(2*R)**2)


if EXERCISE==3:
    dist=10
    l=5

    NUM=1000

    cnt=0

    fig,ax=plt.subplots()

    ax.set_xlim(-l,dist+l)
    ax.set_ylim(-l,l)

    ax.plot([0,0],[-l,l],color='b')
    ax.plot([dist,dist],[-l,l],color='b')

    for _ in range(NUM):
        P=dist* np.random.random() #centrul chibritului

        th=np.pi * np.random.random() #unghiul cu verticala

        umbra=l/2*np.sin(th) #lungimea proiectiei unei jumatati de chibrtit pe axa orizontala

        if P+umbra>=dist or P-umbra<0: #chibritul taie una dintre linii
            cnt+=1

        x1=P-umbra
        x2=P+umbra

        y1=l/2*np.cos(th)
        y2=-l/2*np.cos(th)

        ax.plot([x1,x2],[y1,y2],color='k')



    print('Probabilitatea empirică este:',cnt/NUM)

    print('Pi este aproximativ:',NUM/cnt)

    plt.show()



def plot_Omega(with_ball=False,with_points=None):
    fig,ax=plt.subplots()
    v_theta=np.linspace(0,2*np.pi,num=100)
    v_x=np.multiply(rho(v_theta),np.cos(v_theta))
    v_y=np.multiply(rho(v_theta),np.sin(v_theta))
    ax.set_aspect(1)

    ax.plot(v_x,v_y,color="blue")

    if with_ball:
        v_R_x=R*np.cos(v_theta)
        v_R_y=R*np.sin(v_theta)
        ax.plot(v_R_x,v_R_y,color="red")

    if with_points:

        vp_x=[p[0]*np.cos(p[1]) for p in with_points]
        vp_y=[p[0]*np.sin(p[1]) for p in with_points]

        ax.scatter(vp_x, vp_y, color="black",marker='*')

    plt.show()

def points_inside(rho,R,number): # generates 'number' uniform random points in the star-shaped domain characterised by rho, via exclusion technique
                                 # R is the radius of a ball enclosing the domain
    points=[]
    num=0
    while (num<number):
        x,y=2*R*np.random.random(2)-R
        theta=np.arctan2(y,x)
        r=np.sqrt(x**2+y**2)
        if r<rho(theta):
            points.append((r,theta))
            num+=1
    return points


def rho(theta):
    return 3+np.cos(4*theta)

R=4

points=points_inside(rho,R,100)

plot_Omega(with_ball=True,with_points=points)


