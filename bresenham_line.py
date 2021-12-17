import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    xs = [i for i in range(x1, x2 + 1)]
    ys = [y1]
    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx

    xk = x1
    while xk != x2:
        if p < 0:
            p = p + 2 * dy
            ys.append(ys[-1])
        else:
            p = p + 2 * dy - 2 * dx
            ys.append(ys[-1] + 1)
        xk += 1

    return xs, ys

def bresenham_adopt(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if(dy >= dx):
        #  m >= 1 swap
        ys, xs = bresenham(y1, x1, y2, x2)
    else:
        xs, ys = bresenham(x1, y1, x2, y2)

    return xs, ys



if __name__ == '__main__':
    x1, y1, x2, y2= map(int, input("please input two point(x1 y1 x2 y2): ").split(' '))

    xs, ys = bresenham_adopt(x1, y1, x2, y2)

    plt.title('bresenham')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xticks(range(x1, x2 + 1))
    plt.yticks(range(y1, y2 + 1))
    plt.grid(color='black',
        linestyle='--',
        linewidth=1,
        alpha=0.3)
    plt.scatter(xs, ys, color="blue")
    plt.plot([x1, x2], [y1, y2], 'y', alpha=0.4)
    plt.axis("equal")
    plt.show()