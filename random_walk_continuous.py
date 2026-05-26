import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

X,Y=[0],[0]

def Move():
    global X,Y
    alpha=random.uniform(0,2*np.pi)
    magnitude=random.uniform(0,1)
    X.append(X[-1]+magnitude*np.cos(alpha))
    Y.append(Y[-1]+magnitude*np.sin(alpha))

fig,ax = plt.subplots()
line, = ax.plot([],[])
dot, = ax.plot([], [], 'ro')

def update(frame):
    Move()
    line.set_data(X,Y)
    dot.set_data([X[-1]], [Y[-1]])
    return line,

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ani = anim.FuncAnimation(fig, update, interval=50)
plt.show()