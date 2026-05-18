import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

dt = 0.01
t=0

# Grid of initial conditions
initial_conditions = [(x, y) for x in range(-10, 11) for y in range(-10, 11)]
x_traj = [[x] for x, _ in initial_conditions]
y_traj = [[y] for _, y in initial_conditions]

fig, ax = plt.subplots()
trajectories = [ax.plot([], [], linewidth=0.4)[0] for _ in initial_conditions]

# Right hand side of the system x' = f(x,y,t), y' = g(x,y,t)
def f(x, y, t):
    return np.cos(x) + y 

def g(x, y, t):
    return x*(np.sin(t)) + x
    
def rhs(x, y):
    return (f(x, y, t), g(x, y, t))

# Euler step
def update(frame):
    global t,dt
    t += dt
    for i in range(len(initial_conditions)):
        dx, dy = rhs(x_traj[i][-1], y_traj[i][-1])
        x_traj[i].append(x_traj[i][-1] + dt * dx)
        y_traj[i].append(y_traj[i][-1] + dt * dy)
        trajectories[i].set_data(x_traj[i], y_traj[i])
    return trajectories

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axhline(0, color='black', linewidth=0.6)
ax.axvline(0, color='black', linewidth=0.6)
plt.grid(color='k', linestyle='-', linewidth=0.2)

ani = anim.FuncAnimation(fig, update, interval=1, cache_frame_data=False)
plt.show()