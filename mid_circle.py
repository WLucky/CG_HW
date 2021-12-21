import matplotlib.pyplot as plt

def mid_point_circle(r):
    xs = [0]
    ys = [r]
    p = 1 - r
    
    while xs[-1] < ys[-1]:
        if p < 0:
            p = p + 2 * xs[-1] + 3
            ys.append(ys[-1])
        else:
            p = p + 2 * xs[-1] - 2 * ys[-1] + 5
            ys.append(ys[-1] - 1)

        xs.append(xs[-1] + 1)

    return xs, ys

def mid_point_circle_adopt(r):
    circle_xs = []
    circle_ys = []

    xs, ys = mid_point_circle(r)

    for x, y in zip(xs, ys):
        circle_xs.append(x)
        circle_ys.append(y)

        circle_xs.append(-x)
        circle_ys.append(y)

        circle_xs.append(-x)
        circle_ys.append(-y)

        circle_xs.append(x)
        circle_ys.append(-y)

        circle_xs.append(y)
        circle_ys.append(x)

        circle_xs.append(-y)
        circle_ys.append(x)

        circle_xs.append(-y)
        circle_ys.append(-x)

        circle_xs.append(y)
        circle_ys.append(-x)

    return circle_xs, circle_ys



if __name__ == '__main__':
    r= int(input("please input circle radius: "))

    xs, ys = mid_point_circle_adopt(r)

    plt.title('mid point circle')
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.xticks(range(min(xs), max(xs) + 1))
    # plt.yticks(range(min(ys), max(ys) + 1))
    plt.grid(color='black',
        linestyle='--',
        linewidth=1,
        alpha=0.3)
    plt.scatter(xs, ys, color="blue")

    circle = plt.Circle((0, 0), r, color='y', fill=False)
    plt.gcf().gca().add_artist(circle)
    plt.axis("equal")
    plt.show()

