import numpy as np

gradient = (0,0)
x = gradient

magnitude = np.sqrt(sum((i**2 for i in x)))

if magnitude != 0:
    direction = x/magnitude
else:
    direction = [0]*len(x)

descent_direction = -1*direction

print(magnitude,direction,descent_direction)