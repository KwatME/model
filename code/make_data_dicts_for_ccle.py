from gzip import open as gzip_open
from pickle import load


def make_data_dicts_for_ccle(
    pickle_gz_file_path="../data/ccle.pickle.gz",
    data_names=(
        "Mutation",
        "Mutational Signature",
        "CNV",
        "Methylation",
        "RNA",
        "Gene Set",
        "Protein",
        "Metabolite",
        "RNAi",
        "CRISPR",
        "NP24",
        "CTRP",
        "Binary Information",
    ),
):

    data_dicts = {"feature": {}, "sample": {}}

    with gzip_open(pickle_gz_file_path) as pickle_gz_file:

        pickle_data_dicts = load(pickle_gz_file)

    for data_name in data_names:

        data_dicts["sample"][data_name] = pickle_data_dicts[data_name]

    return data_dicts
