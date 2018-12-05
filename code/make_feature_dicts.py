from gzip import open as gzip_open
from pickle import load

from ccal import process_feature_x_sample
from pandas import DataFrame, read_table


def make_feature_dicts():

    feature_feature_dicts = {}

    sample_feature_dicts = {}

    sample_feature_dicts["RNA"] = {
        "df": process_feature_x_sample(
            read_table("../data/feature_x_sample.tsv", index_col=0),
            shift_as_necessary_to_achieve_min_before_logging="0<",
            log_base="2",
            plot=False,
        ),
        "data_type": "continuous",
    }

    information_x_sample = read_table("../data/information_x_sample.tsv", index_col=0)

    sample_feature_dicts["Phenotype"] = {
        "df": information_x_sample,
        "data_type": "binary",
    }

    blood_indices = information_x_sample.index[
        information_x_sample.index.str.lower().str.contains("blood")
    ]

    brain_cerebel_indices = information_x_sample.index[
        information_x_sample.index.str.lower().str.contains("cerebel")
    ]

    brain_other_indices = information_x_sample.index[
        information_x_sample.index.str.lower().str.contains("brain")
        & ~information_x_sample.index.str.lower().str.contains("cerebel")
    ]

    selected_information_x_sample = DataFrame(
        columns=information_x_sample.columns, index=("Blood and Brain",)
    )

    selected_information_x_sample.loc[
        "Blood and Brain", information_x_sample.loc[blood_indices].sum().astype(bool)
    ] = 0

    selected_information_x_sample.loc[
        "Blood and Brain",
        information_x_sample.loc[brain_cerebel_indices].sum().astype(bool),
    ] = 1

    selected_information_x_sample.loc[
        "Blood and Brain",
        information_x_sample.loc[brain_other_indices].sum().astype(bool),
    ] = 2

    sample_feature_dicts["Selected Phenotype"] = {
        "df": selected_information_x_sample,
        "data_type": "categorical",
    }

    return {"feature": feature_feature_dicts, "sample": sample_feature_dicts}
