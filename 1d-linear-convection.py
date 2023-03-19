import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


nx = 100 # try changing this number from 41 to 81 and Run All ... what happens?
L = 10
dx = L/(nx - 1)
print(dx)
nt = 1000    #nt is the number of timesteps we want to calculate
c = 1      #assume wavespeed of c = 1
dt = 0.5 * dx / c  #dt is the amount of time each timestep covers (delta t)
k = c * dt/dx
X = np.linspace(0, L, nx)
u = np.zeros((nx, nt))
#u[:, 0] = 0.05 * np.exp(-(X - 1)**2)/(2 * 0.4**2)
u[4: 10, 0] = 11

u[0, :] = 0
u[nx - 1, :] = 0

u0 = u.copy()
for t in range(nt - 1):
    for x in range(1, nx - 1):
        u[x, t + 1] = u0[x, t] - k * (u0[x, t] - u0[x - 1, t])
        u0 = u

def animate(i):
    fig.clear()
    p, = plt.plot(u[:, i])
    return p,

fig = plt.figure()
anim = FuncAnimation(fig, animate, frames = nt, interval = 10)
plt.show()
