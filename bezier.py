import matplotlib.pyplot as plt
import numpy as np

# 定义阶乘函数
def factorial(n):
    s = 1
    for index in range(n, 0, -1):
        s *= index
    return s

# 定义组合函数
def C(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def B_nk_t(n, k, t):
    return C(n, k) * (t**k) * (1 - t)**(n - k) 

def p(points, t):
    n = len(points) - 1
    pt = 0
    for k in range(n + 1):
        _, pk = points[k]
        pt += pk * B_nk_t(n, k, t)

    return pt

def bezier_line(points):
    xs = [x for x, y in points]

    select_xs = np.linspace(min(xs), max(xs), 100)
    ts = (select_xs - min(xs)) / (max(xs) - min(xs))
    select_ys = [p(points, t) for t in ts]

    return select_xs, select_ys


if __name__ == '__main__':
    points = []
    p_n = int(input("please input  contral points number(>1): "))
    for i in range(p_n):
        x, y= map(int, input("please input p{:d}:(x y) ".format(i)).strip().split(' '))
        points.append((x, y))

    vertex_xs = [x for x, y in points]
    vertex_ys = [y for x, y in points]
    xs, ys = bezier_line(points)
    x1 = min(vertex_xs)
    x2 = max(vertex_xs)
    y1 = min(vertex_ys)
    y2 = max(vertex_ys)

    plt.title('Bezier')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xticks(range(x1, x2 + 1))
    plt.yticks(range(y1, y2 + 1))
    plt.grid(color='black',
        linestyle='--',
        linewidth=1,
        alpha=0.3)
    plt.plot(vertex_xs, vertex_ys, 'g-')

    plt.plot(xs, ys, 'r')
    plt.axis("equal")
    plt.show()
