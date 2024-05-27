import numpy as np
import matplotlib.pyplot as plt
# Function to generate Gaussian distributed random numbers using the Box-Muller method
def box_muller(n):
    u1 = np.random.rand(n)
    u2 = np.random.rand(n)
    z1 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    return z1
# Number of random numbers to generate
n = 10000
# Generate random numbers using Box-Muller method
random_numbers = box_muller(n)
# Plot the histogram of the generated random numbers
plt.hist(random_numbers, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black', label='Histogram')
# Plot the Gaussian PDF for reference
x = np.linspace(-4, 4, 1000)
gaussian_pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
plt.plot(x, gaussian_pdf, 'r--', linewidth=2, label='Gaussian PDF')
plt.title('Density Histogram of 10000 Gaussian random numbers and Gaussian PDF')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
