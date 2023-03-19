import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import pyplot as plt, cm
import numba as nb
from numba import njit, jit


fig = plt.figure(figsize=(11, 7), dpi=100)
ax = plt.axes(projection='3d')
X, Y = np.meshgrid(X, Y)

@jit
def LinearConvection2D():
    nx = 100
    ny = 100
    nt = 100

    c = 1
    L = 10
    dx = L/(nx - 1)
    dy = L/(ny - 1)

    sigma = 0.2
    dt = dx * sigma * c

    X = np.linspace(0, L, nx)
    Y = np.linspace(0, L, ny)

    u = np.ones((nx, ny, nt))
    un = u.copy()

    # At t = 0
    u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1), 0] = 2 
    row, col, _ = u.shape
    u0 = u.copy()
    for t in range(0, nt - 1):
        for i in range(1, row):
            for j in range(1, col):
                u[i, j, t + 1] = u0[i, j, t] - c * dt/dx * (u[i, j, t] - u[i - 1, j, t]) - c * dt/dy * (u[i, j, t] - u[i, j-1, t])
                u0 = u

@jit
def animate(i):
    ax.clear()
    p = ax.plot_surface(X, Y, u[:, :, i], cmap=cm.viridis)
    return p,

LinearConvection2D()
anim = FuncAnimation(fig, animate, frames = nt, interval = 10)
plt.show()
