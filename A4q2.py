import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()
random_numbers = np.random.rand(10000)
end_time = time.time()
time_taken = end_time - start_time
print(f"Time taken to generate 10000 random numbers: {time_taken} seconds")
plt.hist(random_numbers, bins=12, density=True, alpha=0.7, color='blue', edgecolor='black', label='Histogram')
x = np.linspace(0, 1, 1000)
uniform_pdf = np.ones_like(x)
plt.plot(x, uniform_pdf, 'r--', linewidth=2, label='Uniform PDF')
plt.title('Density Histogram of 10000 random numbers and uniform PDF')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
