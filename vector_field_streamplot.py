import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

t = 0
dt = 0.05

x = np.linspace(0, 10, 21)
y = np.linspace(0, 10, 21)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots()

def get_field(t):
    u = X**(2*t)-Y**(-1*t)
    v = X**(-1*t)-Y**(2*t)
    return u, v

def update(frame):
    global t, dt
    t += dt
    ax.cla()
    u, v = get_field(t)
    ax.streamplot(x, y, u, v, density=1)

ani = anim.FuncAnimation(fig, update, interval=1, cache_frame_data=False)
plt.show()
