import matplotlib.pyplot as plt
import numpy as np
from src.commons import fit_in_sphere, generate_test_points


def act_1(max_dim=50, test_points_num=1000, should_plot=False):
    x = list(range(1, max_dim))
    fit_points_num = [sum([fit_in_sphere(point) for point in generate_test_points(test_points_num, dim_num)] * 100)/test_points_num for dim_num in x]
    if should_plot:
        plt.plot(x, fit_points_num)
        plt.show(block=True)
    return x, fit_points_num


