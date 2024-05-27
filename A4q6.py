import numpy as np
import matplotlib.pyplot as plt
m=10000
y1=[]
x1=5*np.random.rand(m)
x2=np.random.rand(m)
def f(x):
  return (np.sqrt((2/np.pi)) *np.exp(-x*x/2))
for i in range(len(x1)):
  if x2[i]<=f(x1[i]):
    y1.append(x1[i])
h=np.linspace(0, 4, 100)
k=f(h)
plt.hist(y1, density=True, bins=20, color='blue', edgecolor='black', label='Rejection method')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Density Histogram')
plt.plot(h,k,linestyle='dashed',label='Analytical PDF')
plt.legend()
plt.show()
