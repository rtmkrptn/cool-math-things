import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

s = 0.01

# Grid of integer starting points
grid = [(x, y) for x in range(-10, 11) for y in range(-10, 11)]
X = [[x] for x, _ in grid]
Y = [[y] for _, y in grid]

# Definition of the xy plane
fig, ax = plt.subplots()
lines = [ax.plot([], [], linewidth=0.4)[0] for _ in grid]

# Definition of the vector field
def f(x):
    return np.cos(x)
def g(y):
    return np.cos(y)
def vector_field(x, y):
    return (f(x), g(y))

# Update func for the animation
def update(frame):
    for i in range(len(grid)):
        vx, vy = vector_field(X[i][-1], Y[i][-1])
        X[i].append(X[i][-1] + s * vx)
        Y[i].append(Y[i][-1] + s * vy)
        lines[i].set_data(X[i], Y[i])
    return lines

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axhline(0, color='black', linewidth=0.6)
plt.grid(color='k', linestyle='-', linewidth=0.2)
ax.axvline(0, color='black', linewidth=0.6)

ani = anim.FuncAnimation(fig, update, interval=1, cache_frame_data=False)
plt.show()
