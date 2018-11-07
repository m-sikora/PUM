from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from src.generate_points import *
from src.wrap_point import act as wrap_point
import numpy as np
import pandas as pd
from src.visualise import v2d, v3d

dim_num = 4
target_dim = 3

edge_points_raw = on_edges(dim_num, 5)
vertex_points_raw = on_vertices(dim_num)
inside_matched_raw, inside_unmatched_raw = inside(dim_num, 100)

edge_points = [wrap_point(p, 'r') for p in edge_points_raw]
vertex_points = [wrap_point(p, 'y') for p in vertex_points_raw]
inside_matched = [wrap_point(p, 'g') for p in inside_matched_raw]
inside_unmatched = [wrap_point(p, 'b') for p in inside_unmatched_raw]

all_points = pd.DataFrame(edge_points + vertex_points + inside_matched + inside_unmatched)

x = all_points.loc[:, list(range(dim_num))]
y = all_points.loc[:, [dim_num]]

pca = PCA(n_components=target_dim)
mapped_points = pca.fit_transform(x)
mapped_df = pd.DataFrame(mapped_points)
final_df = pd.concat([mapped_df, y], axis=1)

if target_dim == 2:
    v2d(final_df)

v3d(final_df)