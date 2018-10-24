import matplotlib.pyplot as plt
import numpy as np
import math
from src.commons import pick_at_random, generate_test_points, get_angle


def act_3(max_dim=50, repeats_per_dim=20, should_plot=False):
    x = list(range(2, max_dim))

    def get_mean_angle(dim_num):
        space = generate_test_points(200, dim_num)

        def get_for_repeat(i):
            vertices = pick_at_random(space, 4)
            v1 = np.subtract(vertices[1], vertices[0]).tolist()
            v2 = np.subtract(vertices[3], vertices[2]).tolist()
            rr = get_angle(v1, v2)
            return rr

        r = np.mean(list(map(get_for_repeat, range(repeats_per_dim))))
        return r

    y = list(map(get_mean_angle, x))
    if should_plot:
        plt.plot(x, y)
        plt.show(block=True)
    return x, y


# v1 = [.5, .5]
# v2 = [.5 * math.sqrt(3), .5]
# a = get_angle(v1, v2)
# a