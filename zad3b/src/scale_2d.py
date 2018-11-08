def act(df):
    # df_slice = df.loc[:, 0:1]
    df -= df.min()
    df /= df.max()
