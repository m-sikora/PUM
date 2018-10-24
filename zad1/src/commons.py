import random
import numpy as np
import math
from itertools import combinations


def dist(p1, p2):
    dist_combined = .0
    for idx, val in enumerate(p1):
        dist_combined += (val - p2[idx]) ** 2
    return math.sqrt(dist_combined)


def generate_test_points(points_num, dimensions, cube_size=1):
    return [[np.random.uniform(-cube_size, cube_size) for _ in range(dimensions)] for _ in range(points_num)]


def fit_in_sphere(point):
    dist_combined = 0
    for dim in point:
        dist_combined += dim ** 2
    return int(dist_combined <= 1)


def get_measures(points):
    pairs = combinations(points, 2)
    distances = [dist(p1, p2) for p1, p2 in pairs]
    return np.mean(distances), np.std(distances, ddof=1)


def pick_at_random(points, length):
    random.shuffle(points)
    return points[0:length]


def get_scalar_product(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))


def get_v_length(v):
    return math.sqrt(get_scalar_product(v, v))


def get_angle(v1, v2):
    return math.acos(get_scalar_product(v1, v2) / (get_v_length(v1) * get_v_length(v2)))
