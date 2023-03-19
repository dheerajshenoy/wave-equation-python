import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import pyplot as plt, cm

class LinearConvection2D:
    def __init__(self, nx, ny, nt, L, sigma):
        self.nx = nx
        self.ny = ny
        self.nt = nt
        self.c = 1
        self.L = L
        self.sigma = sigma
        self.dx = L/(self.nx - 1)
        self.dy = L/(self.ny - 1)
        self.X = np.linspace(0, L, nx)
        self.Y = np.linspace(0, L, ny)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        self.dt = self.dx * sigma * self.c
        self.u = np.ones((nx, ny, nt))
        self.un = self.u.copy()
        self.fig = plt.figure()
        self.ax = plt.axes(projection='3d')
        self.u[int(.5 / self.dy):int(1 / self.dy + 1),int(.5 / self.dx):int(1 / self.dx + 1), 0] = 2 
        self.row, self.col, _ = self.u.shape
        self.evolve()
    
    def evolve(self):
        self.u0 = self.u.copy()
        for t in range(0, self.nt - 1):
            for i in range(1, self.row):
                for j in range(1, self.col):
                    self.u[i, j, t + 1] = self.u0[i, j, t] - self.c * self.dt/self.dx * (self.u[i, j, t] - self.u[i - 1, j, t]) - self.c * self.dt/self.dy * (self.u[i, j, t] - self.u[i, j-1, t])
                    self.u0 = self.u

    def animate(self, i):
        self.ax.clear()
        self.ax.set_title("2D Linear Convection")
        p = self.ax.plot_surface(self.X, self.Y, self.u[:, :, i], cmap=cm.viridis)
        return p,
    
    def anim(self):
        a = FuncAnimation(self.fig, self.animate, frames = self.nt, interval = 40)
        #plt.show()
        a.save("anim.mp4")

l = LinearConvection2D(nx = 100, ny = 100, nt = 100, L = 10, sigma = 0.1)
l.anim()

