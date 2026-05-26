import math
import matplotlib.pyplot as plt
import numpy as np
import mpmath 

# Use mp.dps to set decimal places globally
mpmath.mp.dps = 50 

m = 50

def taylor_cos(x, n):
    # Ensure x is high precision inside the function
    x_mp = mpmath.mpf(x)
    total_sum = mpmath.mpf(0)
    for i in range(0, n):
        # Calculating using mpmath's factorial and power
        term = ((-1)**i) * (x_mp**(2*i)) / mpmath.factorial(2*i)
        total_sum += term
    return total_sum 

X = []
Y = []

for N in range(1, m):
    # np.linspace returns standard floats, which is fine for the range...
    for x_i in np.linspace(0, N*5, 500):
        # ...but we compare using high precision here
        t_cos = taylor_cos(x_i, N)
        m_cos = mpmath.cos(mpmath.mpf(x_i)) # High-precision ground truth
        
        if abs(m_cos - t_cos) > mpmath.mpf('1e-10'):
            X.append(N)
            Y.append(x_i)
            break

# Linear regression for the "frontier" of accuracy
coeffs = np.polyfit(X, Y, 1)
fit = np.poly1d(coeffs)
print(f"Linear Fit Coefficients: {coeffs}")

plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='black', s=10, label='Limit of Accuracy (10^-10)')
plt.plot(X, fit(X), color='red', linestyle='--', label=f'Fit: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}')

plt.title("Relationship between Number of Terms (N) and Max x for Accuracy")
plt.xlabel("Number of Terms (N)")
plt.ylabel("Maximum Distance (x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

