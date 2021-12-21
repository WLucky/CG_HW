import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(x, y, G):
    c = np.array(x + 1j * y)
    z = np.zeros(c.shape, dtype=complex)
    r = np.ones(c.shape)
    m = np.ones(c.shape, dtype=bool)
    for k in range(50):
        z[m] = z[m] ** 2 + c[m]
        m = np.abs(z) < 2
        r -= k * m * G / 50
    return r

def get_index(a, b, n):
    x = np.linspace(-a, a,n)
    y = np.linspace(-b, b, n)
    return np.meshgrid(x,y)

if __name__ == '__main__':
    (X, Y)= get_index(2, 2, 1500)
    G = 1
    extent = (X.min(), X.max(), Y.min(), Y.max())
    plt.figure(dpi=800)
    plt.imshow(mandelbrot(X, Y, G), extent=extent)
    plt.axis('off')
    plt.savefig("Mandelbort_G{:.2f}.png".format(G))