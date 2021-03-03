# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
import math
def nd(mu,sigma,x):
    a=np.sqrt(np.pi*2)*sigma
    b=-(x-mu)**2
    c=2*sigma**2
    y=1/a*np.exp(b/c)
    return y
mu=5
std=1/4
x=np.linspace(mu-3*std,mu+3*std,300)
y=nd(mu,std,x)

fig , ax = plt.subplots()
# plt.subplot(1, 3, 1)
# fig.subplots_adjust(hspace=1, wspace=1)
plt.plot(x,y,'r-',alpha=0.3,label="std=1/4")
# plt.xticks(np.arange(mu-3*std,mu+3*std))


mu=5
std=1
x=np.linspace(mu-3*std,mu+3*std,300)
y=nd(mu,std,x)
# plt.subplot(1, 3, 2)

plt.plot(x,y,'b-',alpha=0.3,label="std=1")
# plt.xticks(np.arange(mu-3*std,mu+3*std))



mu=5
std=10
x=np.linspace(mu-3*std,mu+3*std,300)
y=nd(mu,std,x)
# plt.subplot(1, 3, 3)
plt.plot(x,y,'g-',alpha=0.3,label="std=10")
# plt.xticks(np.arange(mu-3*std,mu+3*std))

plt.legend()

def ed(c,x):
    res=[]
    for t in x:
        if(t<0):
            res.append(0)
        if(t>=0):
            res.append(c*np.exp(-c*t))
    return res
c=[1,1/2,1/4,1/8]
x=np.linspace(-5,5)

for i in c:
    y=ed(i,x)
    plt.plot(x,y,label='c='+str(i))
    plt.legend()

def lnd(mu,sigma,x):
    a=np.sqrt(np.pi*2)*sigma*x
    b=-(log(x)-mu)**2
    c=2*sigma**2
    y=1/a*np.exp(b/c)
    return y


mu=5
std=1/8
x=np.linspace(mu-3*std,mu+3*std,300)
y=nd(mu,std,x)

# fig , ax = plt.subplots()
# plt.subplot(1, 5, 1)
# fig.subplots_adjust(hspace=1, wspace=1)
plt.plot(x,y,'r-',alpha=0.3,label="std=1/8",color="red")
plt.legend()

mu=5
std=1/2
x=np.linspace(mu-3*std,mu+3*std,300)
y=nd(mu,std,x)

# plt.subplot(1, 5, 2)
# fig.subplots_adjust(hspace=1, wspace=1)
plt.plot(x,y,'b-',alpha=0.3,label="std=1/2",color="blue")


mu=5
std=1
x=np.linspace(mu-3*std,mu+3*std,300)
y=nd(mu,std,x)

# plt.subplot(1, 5, 3)
# fig.subplots_adjust(hspace=1, wspace=1)
plt.plot(x,y,'g-',alpha=0.3,label="std=1",color="green")

mu=5
std=3/2
x=np.linspace(mu-3*std,mu+3*std,300)
y=nd(mu,std,x)

# plt.subplot(1, 5, 4)
# fig.subplots_adjust(hspace=1, wspace=1)
plt.plot(x,y,'y-',alpha=0.3,label="std=3/2",color="yellow")


mu=5
std=10
x=np.linspace(mu-3*std,mu+3*std,300)
y=nd(mu,std,x)

# plt.subplot(1, 5, 5)
# fig.subplots_adjust(hspace=1, wspace=1)
plt.plot(x,y,'-',alpha=0.3,label="std=10",color="black")
plt.xlim(0,10)
# plt.xticks(np.arange(-1,1))
plt.legend()
plt.show()