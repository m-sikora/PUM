from itertools import product
import numpy as np
import math


def on_vertices(dim_num):
    coords_range = [-1, 1]
    coords = list(product(coords_range, repeat=dim_num))
    return coords


def on_edges(dim_num, points_per_edge=10):
    r = []
    for axe in range(dim_num):
        for edge_tp in list(product([-1, 1], repeat=dim_num - 1)):
            edge = list(edge_tp)
            offsets = [np.random.uniform(-1, 1) for _ in range(points_per_edge)]
            for offset in offsets:
                coords = edge[:axe] + [offset] + edge[axe:]
                r.append(tuple(coords))
    return r


def inside(dim_num, points_per_class=20):
    matched = []
    not_matched = []

    if dim_num > 1:
        while len(not_matched) < points_per_class:
            random_point = [np.random.uniform(-1, 1) for _ in range(dim_num)]
            distance = 0
            for dim_coord in random_point:
                distance += dim_coord ** 2
            distance = math.sqrt(distance)
            if distance > 1:
                not_matched.append(tuple(random_point))

    while len(matched) < points_per_class:
        random_point = [np.random.uniform(-1, 1) for _ in range(dim_num)]
        distance = 0
        for dim_coord in random_point:
            distance += dim_coord ** 2
        distance = math.sqrt(distance)
        if distance < 1:
            matched.append(tuple(random_point))
            continue
        max_scale = 1.0 / distance
        scale = np.random.uniform(.0, max_scale)
        sq_scale = math.sqrt(scale)
        scaled_point = [sq_scale * x for x in random_point]
        matched.append(tuple(scaled_point))

    return matched, not_matched
