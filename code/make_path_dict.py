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

    for name in ("feature_x_sample.signal.tsv", "nmf/"):

        path_dict[name] = "{}/signal/{}/{}".format(
            setting["output_directory_path"], setting["signal_type"], name
        )

    for w_or_h in ("w", "h"):

        for name in ("{}.tsv".format(w_or_h), "{}/".format(w_or_h)):

            path_dict[name] = "{}/signal/{}/nmf/{}/{}".format(
                setting["output_directory_path"],
                setting["signal_type"],
                setting["nmf_k"],
                name,
            )

        for name in ("signature.tsv", "match/", "gps_map/", "hcc/"):

            path_dict[
                "{}|{}".format(w_or_h, name)
            ] = "{}/signal/{}/nmf/{}/{}/{}".format(
                setting["output_directory_path"],
                setting["signal_type"],
                setting["nmf_k"],
                w_or_h,
                name,
            )

        path_dict[
            "{}|hcc.k_x_column.tsv".format(w_or_h)
        ] = "{}/signal/{}/nmf/{}/{}/hcc/hcc.k_x_column.tsv".format(
            setting["output_directory_path"],
            setting["signal_type"],
            setting["nmf_k"],
            w_or_h,
        )

        hcc_k = setting["{}_hcc_k".format(w_or_h)]

        name = "cluster_x_column.tsv"

        path_dict[
            "{}|{}".format(w_or_h, name)
        ] = "{}/signal/{}/nmf/{}/{}/hcc/{}/{}".format(
            setting["output_directory_path"],
            setting["signal_type"],
            setting["nmf_k"],
            w_or_h,
            hcc_k,
            name,
        )

        for name in ("match/", "gps_map/", "comparison/"):

            path_dict[
                "{}|hcc|{}".format(w_or_h, name)
            ] = "{}/signal/{}/nmf/{}/{}/hcc/{}/{}".format(
                setting["output_directory_path"],
                setting["signal_type"],
                setting["nmf_k"],
                w_or_h,
                hcc_k,
                name,
            )

    name = "gps_map.pickle.gz"

    path_dict[name] = "{}/signal/{}/nmf/{}/{}".format(
        setting["output_directory_path"], setting["signal_type"], setting["nmf_k"], name
    )

    name = "summary/"

    path_dict[name] = "{}/{}".format(setting["output_directory_path"], name)

    for name, path in path_dict.items():

        if name.endswith("/"):

            path_type = "directory"

        else:

            path_type = "file"

        establish_path(path, path_type)

    if setting["plotly_directory_path"] is not None:

        for element_type_title in ("Feature", "Sample"):

            if element_type_title == "Feature":

                w_or_h = "w"

            elif element_type_title == "Sample":

                w_or_h = "h"

            path_dict["plotly|{}_match/".format(w_or_h)] = "{}/{} Match".format(
                setting["plotly_directory_path"], element_type_title
            )

            path_dict["plotly|{}_gps_map/".format(w_or_h)] = "{}/{} GPS Map".format(
                setting["plotly_directory_path"], element_type_title
            )

    return path_dict
