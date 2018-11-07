import matplotlib.pyplot as plt


def v2d(df):
    for x, y, c in df.values.tolist():
        plt.plot([x], [y], marker='o', markersize=1, color=c)
    plt.show()
