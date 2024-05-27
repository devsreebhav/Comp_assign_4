import numpy as np
from scipy.stats import chi2

obs1=np.array([4,10,10,13,20,18,18,11,13,14,13])
obs2=np.array([3,7,11,15,19,24,21,17,13,9,5])
exp=np.array([4,8,12,16,20,24,20,16,12,8,4])

def chi2test(x,dof):
  p=1-chi2.cdf(x,dof)
  if((p<0.01 )|(p>0.99)):
    print("Not sufficiently random")
  if((0.01<p<0.05)|(0.95<p<0.99)):
    print("Suspect")
  if((0.05<p<0.10)|(0.9<p<0.95)):
    print("Almost suspect")
  if(0.1<p<0.9):
    print("Sufficiently random")

for i in range(2):
  if i==0:
    obs=obs1
  else:
    obs=obs2
  V1=(obs-exp)*(obs-exp)/exp
  V=np.sum(V1)
  print("For observed counts ",i+1,", numbers are:")
  chi2test(V,len(obs-1))
