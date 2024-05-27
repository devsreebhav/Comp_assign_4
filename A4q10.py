import numpy as np
import emcee
import matplotlib.pyplot as plt
import corner
from scipy.optimize import minimize
# Given data
x = np.array([201,244,47,287,203,58,210,202,198,158,165,201,157,131,166,160,186,125,218,146])
y = np.array([592,401,583,402,495,173,479,504,510,416,393,442,317,311,400,337,423,334,533,344])
yerr = np.array([61,25,38,15,21,15,27,14,30,16,14,25,52,16,34,31,42,26,16,22])
def model(theta, x):
  a,b,c = theta
  return a*x**2+b*x+c
def log_likelihood(theta, x, y, yerr):
    model_y = model(theta, x)
    sigma2 = yerr**2
    return -0.5 * np.sum((y - model_y)**2 / sigma2 + np.log(2 * np.pi * sigma2))
def log_prior(theta):
  return 0

def log_posterior(theta, x, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, x, y, yerr)


ndim = 3
nwalkers = 50
nsteps = 4000
#Initializing
initial = np.array([0.0,3.0,100.0])
nll = lambda *args: -log_likelihood(*args)
soln = minimize(nll,initial,args=(x,y,yerr))
pos = soln.x + 1e-4 * np.random.randn(nwalkers, ndim)
# Create the sampler
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior, args=(x, y, yerr))

# Run the MCMC sampler
sampler.run_mcmc(pos, nsteps, progress=True)

# Analyze the results
samples = sampler.get_chain();
#plotting the chains
fig, axes = plt.subplots(3,figsize=(10,7),sharex=True)
labels = ['a','b','c']
for i in range(ndim):
  ax = axes[i]
  ax.plot(samples[:,:,i],'b')
  ax.set_xlim(0,len(samples))
  ax.set_ylabel(labels[i])
  ax.yaxis.set_label_coords(-0.1,0.5)
axes[-1].set_xlabel('Step number');
# Plot the corner plot
samples = sampler.get_chain(discard=100, thin=10, flat=True)
fig = corner.corner(samples, labels=["a", "b","c"])
plt.show()


a_med ,b_med, c_med = np.median(samples, axis=0)
per = np.percentile(samples,[16,50,84],axis=0)
#a_med,b_med,c_med = per[1]
a_err_min,a_err_max = np.diff(per[:,0])
b_err_min,b_err_max = np.diff(per[:,1])
c_err_min,c_err_max = np.diff(per[:,2])
#a_err,b_err,c_err = np.percentile(samples,axis=0)
print("The median values of")
print(f"a: {a_med: .3f},  b: {b_med: .3f}, c:{c_med: .3f}")
print("The one sigma uncertainties of")
print(f"a:(-{a_err_min: .3f},+{a_err_max: .3f}), b:(-{b_err_min: .3f},+{b_err_max: .3f}), c:(-{c_err_min: .3f},+{c_err_max: .3f})")

inds = np.random.randint(len(samples),size=200)
x0 = np.linspace(0,300,100)
for ind in inds:
  sample = samples[ind]
  plt.plot(x0,np.dot(np.vander(x0,3),sample[:3]),'C1',alpha=0.1)
plt.errorbar(x,y,yerr=yerr,fmt='.k',capsize=0)
plt.plot(x0,model([a_med,b_med,c_med],x0),'k',label='truth')
plt.legend()
plt.xlim(0,300)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
     

     

