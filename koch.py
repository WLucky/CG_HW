import matplotlib.pyplot as plt
import numpy as np

def rotate(p_r, p_o, angle = np.radians(60)):
    x1, y1 = p_r
    x2, y2 = p_o
    x = (x1 - x2) * np.cos(angle) - (y1 - y2) * np.sin(angle) + x2
    y = (y1 - y2) * np.cos(angle) + (x1 - x2) * np.sin(angle) + y2

    return [x, y]

def koch(points, iter_num):
    if iter_num == 0:
        return points

    new_points = []
    for i in range(len(points) - 1):
        pa = np.array(points[i])
        pb = np.array(points[i+1])
        p1 = (pb - pa) / 3 + pa
        p2 = (pb - pa) / 3 * 2 + pa
        pr = rotate(p2, p1)
        nps = [pa.tolist(), p1.tolist(), pr, p2.tolist()]
        new_points.extend(nps)
    new_points.append(points[-1])

    return koch(new_points, iter_num - 1)



if __name__ == '__main__':
    start_points = [(0,0), (1, 0)]
    iter_num = int(input("please input iteration times(>=1): "))

    points = koch(start_points, iter_num)
    xs = [x for x, y in points]
    ys = [y for x, y in points]

    plt.title('Kouch Iter {:d}'.format(iter_num))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(xs, ys, 'b')
    plt.axis("equal")
    plt.show()
