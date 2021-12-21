import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def mid_point_ellipse(a, b):
    xs = [0]
    ys = [b]
    p = b**2 - a**2 * b - a**2 / 4

    # step1
    while b**2 * xs[-1] < a**2 * ys[-1]:
        if p < 0:
            p = p + 2 * b**2 * xs[-1] + 3 * b**2
            ys.append(ys[-1])
        else:
            p = p + 2 * b**2 * xs[-1] - 2 * a**2 * ys[-1] + 3 * b**2 + 2 * a**2
            ys.append(ys[-1] - 1)
        xs.append(xs[-1] + 1)
    
    # step2
    q = b**2 * (xs[-1] + 1/2)**2 + a**2 * (ys[-1] - 1)**2 - a**2 * b**2
    while ys[-1] != 0:
        if q < 0:
            q = q + 2 * b**2 * xs[-1] - 2 * a**2 * ys[-1] + 2 * b**2 + 3 * a**2
            xs.append(xs[-1] + 1)
        else:
            q = q - 2 * a**2 * ys[-1] + 3 * a**2
            xs.append(xs[-1])
        ys.append(ys[-1] - 1)

    return xs, ys



def mid_point_ellipse_adopt(a, b):
    ellipse_xs = []
    ellipse_ys = []

    xs, ys = mid_point_ellipse(a, b)

    for x, y in zip(xs, ys):
        ellipse_xs.append(x)
        ellipse_ys.append(y)

        ellipse_xs.append(-x)
        ellipse_ys.append(y)

        ellipse_xs.append(-x)
        ellipse_ys.append(-y)

        ellipse_xs.append(x)
        ellipse_ys.append(-y)

    return ellipse_xs, ellipse_ys



if __name__ == '__main__':
    a, b = map(int, input("please input ellipse param(a b): ").split(' '))


    xs, ys = mid_point_ellipse_adopt(a, b)

    plt.title('mid point ellipse')
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.xticks(range(min(xs), max(xs) + 1))
    # plt.yticks(range(min(ys), max(ys) + 1))
    plt.grid(color='black',
        linestyle='--',
        linewidth=1,
        alpha=0.3)
    plt.scatter(xs, ys, color="blue")

    ellipse = Ellipse((0, 0), width = 2*a, height = 2*b, color='y', fill=False)
    plt.gcf().gca().add_artist(ellipse)
    plt.axis("equal")
    plt.show()

