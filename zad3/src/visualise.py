import matplotlib.pyplot as plt


def v2d(df):
    for x, y, c in df.values.tolist():
        plt.plot([x], [y], marker='o', markersize=1, color=c)
    plt.show()


def v3d(df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for x, y, z, c in df.values.tolist():
        ax.scatter(x, y, z, c=c, marker='o', s=1)

    plt.show()
