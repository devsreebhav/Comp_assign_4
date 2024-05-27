import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('exponential_random_numbers.txt')

mean = 0.5
beta = 1 / mean

plt.hist(data, bins=50, density=True, alpha=0.6, color='g', label='Generated Data of 10000 random numbers')


def exponential_pdf(x, beta):
    return beta * np.exp(-beta * x)


x = np.linspace(0, np.max(data), 1000)
y = exponential_pdf(x, beta)


plt.plot(x, y, 'r-', lw=2, label='Exponential PDF')
plt.title('Density Histogram of Random Numbers and Exponential PDF with Mean 0.5')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
