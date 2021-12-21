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
    neg_k = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    # 如果斜率为负数 则 进行水平方向对称 之后再反转
    if y2 < y1:
        neg_k = True
        y2 = 2 * y1 - y2

    dx = x2 - x1
    dy = y2 - y1        
    if dy >= dx:
        #  m >= 1 swap
        ys, xs = bresenham(y1, x1, y2, x2)
    else:
        xs, ys = bresenham(x1, y1, x2, y2)

    if neg_k:
        ys = [2 * y1 - y for y in ys]

    return xs, ys



if __name__ == '__main__':
    x1, y1, x2, y2= map(int, input("please input two point(x1 y1 x2 y2): ").split(' '))

    xs, ys = bresenham_adopt(x1, y1, x2, y2)

    plt.title('bresenham')
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.xticks(range(min(x1, x2), max(x1, x2) + 1))
    # plt.yticks(range(min(y1, y2), max(y1, y2) + 1))
    plt.grid(color='black',
        linestyle='--',
        linewidth=1,
        alpha=0.3)
    plt.scatter(xs, ys, color="blue")
    plt.plot([x1, x2], [y1, y2], 'y', alpha=0.4)
    plt.axis("equal")
    plt.show()
