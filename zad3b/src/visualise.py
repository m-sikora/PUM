import matplotlib.pyplot as plt


def v2d(df):
    for x, y, c in df.values.tolist():
        plt.plot([x], [y], marker='o', markersize=1, color=c)
    # plt.quiver(0, 0, 1, 0)
    # plt.quiver(0, 0, 0, 1)
    plt.show(block=True)
