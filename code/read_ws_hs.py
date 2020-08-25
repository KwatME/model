from pandas import read_csv


def read_ws_hs(directory_path, model_mode, model_data_):

    n_data = len(model_data_)

    if model_mode == "range":

        n_w = 1

        n_h = n_data

    elif model_mode == "deep":

        n_w = n_data

        n_h = 1

    w_ = tuple(
        read_csv("{}w_{}.tsv".format(directory_path, i), sep="\t", index_col=0)
        for i in range(n_h)
    )

    h_ = tuple(
        read_csv("{}h_{}.tsv".format(directory_path, i), sep="\t", index_col=0)
        for i in range(n_w)
    )

    for w in w_:

        w.columns.name = "Factor"

    for data, h in zip(model_data_, h_):

        h.columns.name = data["axis_1_name"]

    return w_, h_
