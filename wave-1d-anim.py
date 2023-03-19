import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

nx, nt = 1000, 1000
dt = 0.5
dx = 1
X = np.linspace(0, 10, nx)
c = 1
C = dt/dx * c # Courant's number

u = np.zeros((nx, nt))

u[0, :] = 0
u[nx - 1, :] = 0
u[:, 0] = [1 if 0 < x < 1 else 0.0 for x in X]

def waveEquationSolve(u):
    for t in range(0, nt - 1):
        for x in range(1, nx - 1):
            u[x, t + 1] = 2 * (1-C**2)*u[x, t] + C**2 * (u[x + 1, t] + u[x - 1, t])
    return u

u = waveEquationSolve(u)
fig = plt.figure()

def animate(i):
    fig.clear()
    plt.plot(u[:, i])
    print("Time = ", i)

anim = FuncAnimation(fig, animate, frames = nt, interval = 0.5,)
plt.show()
