import matplotlib.pyplot as plt
import math
import numpy as np

class Polynomial:
    def __init__(self, roots):
        self.roots=np.array(roots)

    def __call__(self, x):
        return np.prod([x - r for r in self.roots], axis=0)
    
domain=np.linspace(-3,3,200)
range=Polynomial([1,-1,2,-2])(domain)

plt.plot(domain,range)
plt.axhline(0,color='black')
plt.show()