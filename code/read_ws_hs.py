from pandas import read_csv


def read_ws_hs(directory_path, model_mode, model_data_dicts):

    n_data_dict = len(model_data_dicts)

    if model_mode == "range":

        n_w = 1

        n_h = n_data_dict

    elif model_mode == "deep":

        n_w = n_data_dict

        n_h = 1

    ws = tuple(
        read_csv("{}w_{}.tsv".format(directory_path, i), sep="\t", index_col=0)
        for i in range(n_h)
    )

    hs = tuple(
        read_csv("{}h_{}.tsv".format(directory_path, i), sep="\t", index_col=0)
        for i in range(n_w)
    )

    factor_name = hs[0].index.name

    for w in ws:

        w.columns.name = factor_name

    for dict_, h in zip(model_data_dicts, hs):

        h.columns.name = dict_["axis_1_name"]

    return ws, hs
