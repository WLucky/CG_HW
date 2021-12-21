import numpy as np
import matplotlib.pyplot as plt

julia_C = -0.125 + 1j * 0.842
def julia(x, y, G):
    z = np.array(x + 1j * y)
    r = np.zeros(z.shape)
    m = np.ones(z.shape, dtype=bool)
    for k in range(20):
        z[m] = z[m] ** 2 + julia_C
        m = np.abs(z) < 2
        r -= k * m * G / 20
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
    plt.imshow(julia(X, Y, G), extent=extent)
    plt.axis('off')
    plt.savefig("julia_G{:.2f}.png".format(G))