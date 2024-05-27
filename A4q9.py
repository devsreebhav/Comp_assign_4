import numpy as np
np.set_printoptions(threshold=np.inf)
from scipy.stats import norm
import matplotlib.pyplot as plt
mu=2
sigma=2
nsteps = 10000
theta = 5
a=[]
aprime=[]
def f(x):
    if 3 < x < 7:
        return 1
    else:
        return 0
for i in range(nsteps):
  theta_prime = theta + np.random.standard_normal()
  aprime.append(theta_prime)
  r = np.random.rand()
  if(f(theta_prime)/f(theta)>r):
    theta = theta_prime
    a.append(theta)
  else:
    a.append(theta)
steps=np.arange(0,nsteps,1)
plt.figure(1) 
plt.hist(a,bins=10,density='True',label="Random numbers generated")
x=np.arange(3,7.1,0.1)
y=np.full(len(x),1/4)
plt.ylabel("$\\theta$")
plt.xlabel("$step number$")
plt.plot(x,y,label="uniform PDF")
plt.title("Histogram along with the uniform PDF")
plt.legend(fontsize=17)

plt.figure(2)
plt.title("Complete Chain")
plt.plot(steps,aprime,".-",label="genetated points")
plt.plot(steps,a,".-r",label="selected points")
plt.ylabel("$\\theta$")
plt.xlabel("$step number$")
plt.legend()
plt.show()
