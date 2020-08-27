from pandas import read_csv


def read_factorization(directory_path, model_mode, model_data_):

    data_n = len(model_data_)

    if model_mode == "deep":

        w_n = data_n

        h_n = 1

    elif model_mode == "range":

        w_n = 1

        h_n = data_n

    path_template = "{}{{}}_{{}}.tsv".format(directory_path)

    w_df_ = tuple(
        read_csv(path_template.format("w", index), sep="\t", index_col=0)
        for index in range(w_n)
    )

    h_df_ = tuple(
        read_csv(path_template.format("h", index), sep="\t", index_col=0)
        for index in range(h_n)
    )

    for df in w_df_:

        df.columns.name = "Factor"

    for df, data in zip(h_df_, model_data_):

        df.columns.name = data["axis_1_name"]

    return w_df_, h_df_
