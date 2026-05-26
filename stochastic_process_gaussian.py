import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
import math

N=10
S=1000
y0=0

xs=[[0] for _ in range(N)]
ys=[[y0] for _ in range(N)]
E=0
done=0

sigma=10
mu=0

def StochasticProcess(i):
    global xs,ys,sigma,mu,done
    if len(xs[i]) >= S:
        return
    xs[i].append(xs[i][-1]+1)
    ys[i].append(ys[i][-1]+random.gauss(mu,sigma))
    if len(xs[i]) == S:
        done += 1

fig,ax = plt.subplots()
lines = [ax.plot([],[], linewidth=0.4)[0] for _ in range(N)]
expected_value = ax.axhline(E, color='red', linewidth=1)

def update(frame):
    for i in range(N):
        StochasticProcess(i)
        lines[i].set_data(xs[i],ys[i])
    E = sum(ys[i][-1] for i in range(N))/N
    expected_value.set_ydata([E,E])
    if done == N:
        print(E)
        ani.event_source.stop()
    return lines + [expected_value]

ax.set_xlim(0, S+0.05*S)
spread = 3 * math.sqrt(S * (sigma**2 + mu**2))
ax.set_ylim(y0 + S*mu - spread, y0 + S*mu + spread)
ax.axhline(0, color='black', linewidth=0.8)

ani = anim.FuncAnimation(fig, update, interval=5, cache_frame_data=False)
plt.show()
