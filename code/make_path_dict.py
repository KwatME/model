from ccal import establish_path


def make_path_dict(setting):

    path_dict = {}

    name = "feature_x_sample.processed.tsv"

    path_dict[name] = "{}/{}".format(setting["output_directory_path"], name)

    for name in ("feature_x_fit_parameter.tsv", "sample_x_fit_parameter.tsv"):

        path_dict[name] = "{}/fit/{}".format(setting["output_directory_path"], name)

    for name in (
        "feature_x_sample.feature_context.tsv",
        "feature_x_sample.sample_context.tsv",
    ):

        path_dict[name] = "{}/context/{}".format(setting["output_directory_path"], name)

    for name in (
        "feature_x_sample.raw_signal.tsv",
        "feature_x_sample.context_signal.tsv",
        "nmf/",
    ):

        path_dict[name] = "{}/signal/{}".format(setting["output_directory_path"], name)

    for w_or_h in ("w", "h"):

        for name in ("{}.tsv".format(w_or_h), "{}/".format(w_or_h)):

            path_dict[name] = "{}/signal/nmf/{}/{}".format(
                setting["output_directory_path"], setting["nmf_k"], name
            )

        for name in ("signature", "match", "hcc"):

            path_dict["{}|{}/".format(w_or_h, name)] = "{}/signal/nmf/{}/{}/{}".format(
                setting["output_directory_path"], setting["nmf_k"], w_or_h, name
            )

        path_dict[
            "{}|hcc__k_x_column.tsv".format(w_or_h)
        ] = "{}/signal/nmf/{}/{}/hcc/hcc__k_x_column.tsv".format(
            setting["output_directory_path"], setting["nmf_k"], w_or_h
        )

        hcc_k = setting["{}_hcc_k".format(w_or_h)]

        name = "cluster_x_column.tsv"

        path_dict[
            "{}|{}".format(w_or_h, name)
        ] = "{}/signal/nmf/{}/{}/hcc/{}/{}".format(
            setting["output_directory_path"], setting["nmf_k"], w_or_h, hcc_k, name
        )

        for name in ("match", "gps_map", "comparison"):

            path_dict[
                "{}|hcc|{}/".format(w_or_h, name)
            ] = "{}/signal/nmf/{}/{}/hcc/{}/{}".format(
                setting["output_directory_path"], setting["nmf_k"], w_or_h, hcc_k, name
            )

    name = "gps_map.pickle.gz"

    path_dict[name] = "{}/signal/nmf/{}/{}".format(
        setting["output_directory_path"], setting["nmf_k"], name
    )

    name = "summary/"

    path_dict[name] = "{}/{}".format(setting["output_directory_path"], name)

    for name, path in path_dict.items():

        if name.endswith("/"):

            path_type = "directory"

        else:

            path_type = "file"

        establish_path(path, path_type)

    path_dict["plotly/"] = setting["plotly_directory_path"]

    if path_dict["plotly/"] is None:

        for w_or_h in ("w", "h"):

            path_dict["plotly|{}_match/".format(w_or_h)] = None

            path_dict["plotly|{}_gps_map/".format(w_or_h)] = None

    else:

        for w_or_h in ("w", "h"):

            if w_or_h == "w":

                element_type_title = "Feature"

            elif w_or_h == "h":

                element_type_title = "Sample"

            path_dict["plotly|{}_match/".format(w_or_h)] = "{}/{} Match".format(
                setting["plotly_directory_path"], element_type_title
            )

            path_dict["plotly|{}_gps_map/".format(w_or_h)] = "{}/{} GPS Map".format(
                setting["plotly_directory_path"], element_type_title
            )

    return path_dict
