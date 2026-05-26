import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random

X, Y = [0], [0]

def Move():
    global X, Y
    move = random.choice(['up', 'down', 'right', 'left'])
    if move == 'up':
        Y.append(Y[-1] + 1)
        X.append(X[-1])
    elif move == 'down':
        Y.append(Y[-1] - 1)
        X.append(X[-1])
    elif move == 'right':
        X.append(X[-1] + 1)
        Y.append(Y[-1])
    elif move == 'left':
        X.append(X[-1] - 1)
        Y.append(Y[-1])

fig, ax=plt.subplots()
line, = ax.plot([], [])

def update(frame):
    Move()
    line.set_data(X, Y)
    return line,

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ani = anim.FuncAnimation(fig, update, interval=50)
plt.show()
