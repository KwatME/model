from pandas import read_csv


def read_ws_hs(directory_path, model_mode, model_data_dicts):

    n_data_dict = len(model_data_dicts)

    if model_mode == "range":

        n_w = 1

        n_h = n_data_dict

    elif model_mode == "deep":

        n_w = n_data_dict

        n_h = 1

    ws = []

    for w_i in range(n_w):

        w = read_csv("{}/w_{}.tsv".format(directory_path, w_i), sep="\t", index_col=0)

        ws.append(w)

    hs = []

    for h_i in range(n_h):

        h = read_csv("{}/h_{}.tsv".format(directory_path, h_i), sep="\t", index_col=0)

        name = h.index.name

        h.columns.name = model_data_dicts[h_i]["axis_1_name"]

        hs.append(h)

    for w in ws:

        w.columns.name = name

    return ws, hs
