import matplotlib.pyplot as plt
from bresenham_line import bresenham_adopt

#vertexs
vertex_xs = [7, 2, 2, 7, 13, 13, 7]
vertex_ys = [1, 3, 9, 7, 11, 5, 1]

def seef_fill(seed_x, seed_y, boundary_xs, boundary_ys):
    colored_xs = []
    colored_ys = []
    stack = [(seed_x, seed_y)]

    def not_boundary(x, y):
        return (x, y) not in zip(boundary_xs, boundary_ys)

    def not_colored(x, y):
        return (x, y) not in zip(colored_xs, colored_ys)

    while len(stack) != 0:
        x, y = stack.pop()
        colored_xs.append(x)
        colored_ys.append(y)
        
        for xn, yn in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if not_boundary(xn, yn) and not_colored(xn, yn):
                stack.append((xn, yn))

    return colored_xs, colored_ys


if __name__ == '__main__':
    
    boundary_xs = []
    boundary_ys = []

    for i in range(len(vertex_xs) - 1):
        xs, ys = bresenham_adopt(vertex_xs[i], vertex_ys[i], vertex_xs[i+1], vertex_ys[i+1])
        boundary_xs.extend(xs)
        boundary_ys.extend(ys)

    colored_xs, colored_ys = seef_fill(5, 7, boundary_xs, boundary_ys)

    plt.title('Seed Fill')
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.xticks(range(min(vertex_xs) - 1, max(vertex_xs) + 2))
    # plt.yticks(range(min(vertex_ys) - 1, max(vertex_ys) + 2))
    plt.grid(color='black',
        linestyle='--',
        linewidth=1,
        alpha=0.3)

    plt.plot(vertex_xs, vertex_ys, 'r-')
    plt.fill(vertex_xs, vertex_ys, 'y', alpha=0.3)
    plt.plot(boundary_xs, boundary_ys, 'go')
    plt.plot(colored_xs, colored_ys, 'ro')

    plt.axis("equal")
    plt.show()