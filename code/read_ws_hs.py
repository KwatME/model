from pandas import read_csv


def read_ws_hs(directory_path, model_mode, model_data_):

    n_data = len(model_data_)

    if model_mode == "range":

        n_w = 1

        n_h = n_data

    elif model_mode == "deep":

        n_w = n_data

        n_h = 1

    w_table_ = tuple(
        read_csv("{}w_{}.tsv".format(directory_path, w_index), sep="\t", index_col=0)
        for w_index in range(n_w)
    )

    h_table_ = tuple(
        read_csv("{}h_{}.tsv".format(directory_path, h_index), sep="\t", index_col=0)
        for h_index in range(n_h)
    )

    for w_table in w_table_:

        w_table.columns.name = "Factor"

    for h_table, data in zip(h_table_, model_data_):

        h_table.columns.name = data["axis_1_name"]

    return w_table_, h_table_
