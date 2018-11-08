import pandas as pd
from sklearn.decomposition import PCA, KernelPCA
from zad3b.src.read_data import act as read_data
from zad3b.src.visualise import v2d
from zad3b.src.scale_2d import act as scale

points = read_data('../data/PCA.png')

df = pd.DataFrame(points)
x = df.loc[:, list(range(2))]
y = df.loc[:, [2]]
mean_0 = x.loc[:, 0].mean()
mean_1 = x.loc[:, 1].mean()
new_0 = x.loc[:, 0] - mean_0
new_1 = x.loc[:, 1] - mean_1
x.loc[:, 0] = new_0
x.loc[:, 1] = new_1
# scale(x)

kpca = KernelPCA(kernel="cosine", n_components=2)
mapped_points = kpca.fit_transform(x)
mapped_df = pd.DataFrame(mapped_points)
final_df = pd.concat([mapped_df, y], axis=1)

# v2d(df)
v2d(final_df)
