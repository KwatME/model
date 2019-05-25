from os.path import join

from kraft import establish_path, normalize_path


def make_path_dict(setting):

    output_directory_path = normalize_path(setting["output_directory_path"])

    path_dict = {}

    for name in ("feature_x_sample.processed.tsv", "peek/", "infer/"):

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

        for name in (f"{w_or_h}.tsv", f"{w_or_h}/"):

            path_dict[name] = join(
                output_directory_path,
                "signal",
                setting["signal_type"],
                "mf",
                mf_k,
                name,
            )

        for name in ("match/", "gps_map/", "hcc/", "summary/"):

            path_dict[f"{w_or_h}|{name}"] = join(
                output_directory_path,
                "signal",
                setting["signal_type"],
                "mf",
                mf_k,
                w_or_h,
                name,
            )

        hcc_k = str(setting[f"{w_or_h}_hcc_k"])

        for name in ("cluster_x_element.tsv", "match/", "gps_map/", "comparison/"):

            path_dict[f"{w_or_h}|hcc|{name}"] = join(
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

    for name, path in path_dict.items():

        if name.endswith("/"):

            path_type = "directory"

        else:

            path_type = "file"

        establish_path(path, path_type)

    return path_dict
