import random
import matplotlib.pyplot as plt


def get_ferns_points(iter_num):
    xs = [0]
    ys = [0]
    for _ in range(iter_num):
        r = random.random()

        if r < 0.01:
            new_x = 0
            new_y = 0.16 * ys[-1]
        elif r < 0.86:
            new_x = 0.85 * xs[-1] + 0.04 * ys[-1]
            new_y = -0.04 * xs[-1] + 0.85 * ys[-1] + 1.6
        elif r < 0.93:
            new_x = 0.2 * xs[-1] - 0.25 * ys[-1]
            new_y = 0.23 * xs[-1] + 0.22 * ys[-1] + 1.6
        else:
            new_x = -0.15 * xs[-1] + 0.28 * ys[-1]
            new_y = 0.26 * xs[-1] + 0.24 * ys[-1] + 0.44

        xs.append(new_x)
        ys.append(new_y)

    return xs, ys


if __name__ == '__main__':
    start_points = [(0,0), (1, 0)]
    iter_num = int(input("please input iteration times(>=1): "))

    xs, ys = get_ferns_points(iter_num)
    print(len(xs))
    plt.title('Frens Iter {:d}'.format(iter_num))
    plt.scatter(xs, ys, s = 6,c = 'g', alpha = 0.7)
    plt.axis('off')
    # plt.axis("equal")
    plt.show()