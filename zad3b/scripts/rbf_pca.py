import pandas as pd
from sklearn.decomposition import PCA, KernelPCA
from zad3b.src.read_data import act as read_data
from zad3b.src.visualise import v2d

points = read_data('../data/PCA.png')

df = pd.DataFrame(points)
x = df.loc[:, list(range(2))]
y = df.loc[:, [2]]
kpca = KernelPCA(kernel="rbf", n_components=2, gamma=9000)
mapped_points = kpca.fit_transform(x)
mapped_df = pd.DataFrame(mapped_points)
final_df = pd.concat([mapped_df, y], axis=1)

# v2d(df)
v2d(final_df)
