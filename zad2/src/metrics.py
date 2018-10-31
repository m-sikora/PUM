import math
import pandas as pd
import scipy as sp
from scipy.spatial.distance import mahalanobis


def dist(p1, p2):
    x, y, c = p1
    x_f, y_f, c_f = p2
    return math.sqrt((x_f - x)**2 + (y_f - y)**2)


def build_maha(points):
    df = pd.DataFrame(points)
    df = df.drop([2], axis=1)
    mean_x = df[0].mean()
    mean_y = df[1].mean()
    df[0] = df[0] - mean_x
    df[1] = df[1] - mean_y
    covmx = df.cov()
    invcovmx = sp.linalg.inv(covmx)

    def calc(p1, p2):
        return mahalanobis((p1[0], p1[1]), (p2[0], p2[1]), invcovmx)

    return calc
