import matplotlib.pyplot as plt
import numpy as np
from src.commons import get_measures, generate_test_points


def act_2(max_dim=50, test_points_num=100, should_plot=False):
    x = list(range(1, max_dim))
    points_for_dim_num = [generate_test_points(test_points_num, dim_num, 0.5) for dim_num in x]
    measures_per_dim = [get_measures(points_for_dim_num[dim_num - 1]) for dim_num in x]
    means = [elem[0] for elem in measures_per_dim]
    stds = [elem[1] for elem in measures_per_dim]
    ratios = [means[i] / stds[i] for i in range(0, len(means))]
    if should_plot:
        plt.plot(x, ratios)
        plt.show(block=True)

    # plt.plot(x, means)
    # plt.show(block=True)
    # plt.plot(x, stds)
    # plt.show(block=True)

    return x, ratios

