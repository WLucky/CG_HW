import matplotlib.pyplot as plt
import numpy as np

def B_kd_t(ts, k, d, t):
    if d == 1:
        return 1 if ts[k] <= t and t <= ts[k+1] else 0

    # tk --> ts[k]
    l1 = ts[k+d-1] - ts[k]
    l2 = ts[k+d] - ts[k+1]

    alpha = (t - ts[k]) / l1 if l1 != 0 else 0
    beta = (ts[k+d] - t) / l2 if l2 != 0 else 0
    
    return alpha * B_kd_t(ts, k, d-1, t) + beta * B_kd_t(ts, k+1, d-1, t)

def p(points, ts, d, t):
    n = len(points) - 1
    pt = 0
    for k in range(n + 1):
        _, pk = points[k]
        pt += pk * B_kd_t(ts, k, d, t)

    return pt

def b_spile_line(points, T,  d):
    xs = [x for x, y in points]
    n = len(points) - 1

    select_xs = np.linspace(min(xs), max(xs), 100)
    select_t = np.linspace(T[d - 1], T[n + 1], 100)
    select_ys = [p(points, T, d, t) for t in select_t]

    return select_xs, select_ys

def b_spile_base(T, n, k, d):
    select_t = np.linspace(T[d - 1], T[n + 1], 100)
    by = []
    for t in select_t:
        by.append(B_kd_t(T, k, d, t))
    
    return select_t, by


if __name__ == '__main__':
    points = []
    run_defult = input("run default?(y or n): ")
    if run_defult == 'y':
        points = [(0, 0), (1, 3), (2, 1), (3, 3), (4, 3), (5, 5), (6, 0)]
        d = 3
    else:
        p_n = int(input("please input  contral points number(>1): "))
        for i in range(p_n):
            x, y= map(int, input("please input p{:d}:(x y) ".format(i)).strip().split(' '))
            points.append((x, y))
        d = int(input("please input  d: "))

    n = len(points) - 1
    T = np.pad(range(n - d + 3), (d-1, d-1), 'edge')
    print("T: ", T)

    vertex_xs = [x for x, y in points]
    vertex_ys = [y for x, y in points]
    xs, ys = b_spile_line(points, T, d)

    plt.figure()
    # plt.xlabel("x")
    # plt.ylabel("y")
    plt.subplot(211)
    plt.subplots_adjust(right = 0.8, hspace = 0.3)
    plt.title("Base function")
    for k in range(n + 1):
        b_xs, b_ys = b_spile_base(T, n, k, d)
        plt.plot(b_xs, b_ys, label = "B{:d},{:d}".format(k, d))
        plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
        

    # plt.subplots_adjust(right=0.9)
    plt.subplot(212)
    plt.title('B Spline Line')
    plt.plot(vertex_xs, vertex_ys, 'g-')
    plt.plot(xs, ys, 'r')
    plt.show()
