import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math


def f(x):
    return x**2-1

domain=np.linspace(-5,5,200)
range=f(domain)

plt.plot(domain,range)
plt.axhline(0,color='black')
plt.show()