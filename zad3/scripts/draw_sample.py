import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from src.generate_points import *

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

edge_points = on_edges(3)
vertex_points = on_vertices(3)
inside_matched, inside_unmatched = inside(3)

for x, y, z in edge_points:
    ax.scatter(x, y, z, c='r', marker='o')

for x, y, z in vertex_points:
    ax.scatter(x, y, z, c='b', marker='o')

for x, y, z in inside_matched:
    ax.scatter(x, y, z, c='y', marker='o')

for x, y, z in inside_unmatched:
    ax.scatter(x, y, z, c='g', marker='o')

plt.show()
