from pandas import read_csv


def read_ws_hs(directory_path, model_mode, model_data_):

    data_number = len(model_data_)

    if model_mode == "range":

        w_number = 1

        h_number = data_number

    elif model_mode == "deep":

        w_number = data_number

        h_number = 1

    w_dataframe_ = tuple(
        read_csv("{}w_{}.tsv".format(directory_path, w_index), sep="\t", index_col=0)
        for w_index in range(w_number)
    )

    h_dataframe_ = tuple(
        read_csv("{}h_{}.tsv".format(directory_path, h_index), sep="\t", index_col=0)
        for h_index in range(h_number)
    )

    for w_dataframe in w_dataframe_:

        w_dataframe.columns.name = "Factor"

    for h_dataframe, data in zip(h_dataframe_, model_data_):

        h_dataframe.columns.name = data["axis_1_name"]

    return w_dataframe_, h_dataframe_
