from os.path import join

from ccal import establish_path, get_absolute_path


def make_path_dict(setting):

    output_directory_path = get_absolute_path(setting["output_directory_path"])

    path_dict = {}

    name = "feature_x_sample.processed.tsv"

    path_dict[name] = join(output_directory_path, name)

    for name in ("feature_x_fit_parameter.tsv", "sample_x_fit_parameter.tsv"):

        path_dict[name] = join(output_directory_path, "fit", name)

    for name in (
        "feature_x_sample.feature_context.tsv",
        "feature_x_sample.sample_context.tsv",
    ):

        path_dict[name] = join(output_directory_path, "context", name)

    for name in ("feature_x_sample.signal.tsv", "mf/"):

        path_dict[name] = join(
            output_directory_path, "signal", setting["signal_type"], name
        )

    mf_k = str(setting["mf_k"])

    for w_or_h in ("w", "h"):

        for name in ("{}.tsv".format(w_or_h), "{}/".format(w_or_h)):

            path_dict[name] = join(
                output_directory_path,
                "signal",
                setting["signal_type"],
                "mf",
                mf_k,
                name,
            )

        for name in ("match/", "gps_map/", "hcc/", "summary/"):

            path_dict["{}|{}".format(w_or_h, name)] = join(
                output_directory_path,
                "signal",
                setting["signal_type"],
                "mf",
                mf_k,
                w_or_h,
                name,
            )

        hcc_k = str(setting["{}_hcc_k".format(w_or_h)])

        name = "cluster_x_column.tsv"

        path_dict["{}|{}".format(w_or_h, name)] = join(
            output_directory_path,
            "signal",
            setting["signal_type"],
            "mf",
            mf_k,
            w_or_h,
            "hcc",
            hcc_k,
            name,
        )

        for name in ("match/", "gps_map/", "comparison/"):

            path_dict["{}|hcc|{}".format(w_or_h, name)] = join(
                output_directory_path,
                "signal",
                setting["signal_type"],
                "mf",
                mf_k,
                w_or_h,
                "hcc",
                hcc_k,
                name,
            )

    name = "gps_map.pickle.gz"

    path_dict[name] = join(
        output_directory_path, "signal", setting["signal_type"], "mf", mf_k, name
    )

    for name in ("summary/", "infer/"):

        path_dict[name] = join(output_directory_path, name)

    for name, path in path_dict.items():

        if name.endswith("/"):

            path_type = "directory"

        else:

            path_type = "file"

        establish_path(path, path_type)

    return path_dict
