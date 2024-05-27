import numpy as np
import matplotlib.pyplot as plt

# Parameters for the Linear Congruential Generator (LCG)
a = 1104678569
c = 10234
m = 2037586678
x = 13  # Initial seed
n = 10000  # Number of random numbers to generate

# Generate random numbers using LCG
random_nos = np.empty(n)
for i in range(n):
    x = (a * x + c) % m
    random_nos[i] = x / m

# Plot the histogram of the generated random numbers
plt.hist(random_nos, bins=15, density=True, alpha=0.6, color='g', label="Uniform random numbers")

# Plot the uniform PDF
x_vals = np.linspace(0, 1, 100)
y_vals = np.ones_like(x_vals)
plt.plot(x_vals, y_vals, label="Uniform PDF", lw=2, color='r')

# Labels and legend
plt.xlabel("x", fontsize=17)
plt.ylabel("PDF", fontsize=17)
plt.legend(fontsize=17)
plt.title("Histogram of Uniform Random Numbers and Uniform PDF", fontsize=17)

# Show the plot
plt.show()
