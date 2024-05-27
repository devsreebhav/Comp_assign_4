import numpy as np
np.set_printoptions(threshold=np.inf)
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use(preferred_backend)
a=1104678569
c=10234
m=2037586678
x=13
x=15
n=10000
random_nos=[]
for i in range(n):
  x=(a*x+c)%m
  random_nos.append(x/m)
plt.hist(random_nos,density ="True",label="Uniform random numbers")
x=np.arange(0,1.1,0.1)
y=np.ones(x.size)
plt.plot(x,y,label="Uniform PDF")
plt.xlabel("x",fontsize=17)
plt.ylabel("PDF",fontsize=17)
plt.legend(fontsize=17)
plt.show()


