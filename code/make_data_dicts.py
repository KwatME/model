from gzip import open as gzip_open
from pickle import load

from pandas import read_table


def make_data_dicts():

    feature_data_dicts = {}

    sample_data_dicts = {}

    pickle_gz_file_path = "../data/ccle.pickle.gz"

    keys = (
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
    )

    # pickle_gz_file_path = '../data/tcga.pickle.gz'
    #
    # keys = (
    #     'Mutation',
    #     'Mutational Signature',
    #     'CNV',
    #     'Methylation',
    #     'RNA',
    #     'miRNA',
    #     'Gene Set',
    #     'Protein',
    #     'Immune Signature',
    #     'Continuous Information',
    #     'Binary Information',
    # )

    with gzip_open(pickle_gz_file_path) as pickle_gz_file:

        pickle_sample_data_dicts = load(pickle_gz_file)

    for key in keys:

        sample_data_dicts[key] = pickle_sample_data_dicts[key]

    state_x_cell_line = read_table(
        "../data/test/states.tsv", index_col=0, header=None
    ).T

    state_x_cell_line.index = ("State from CCLE Breast Used in KRAS Map",)

    sample_data_dicts["Test"] = {"df": state_x_cell_line, "data_type": "categorical"}

    return {"feature": feature_data_dicts, "sample": sample_data_dicts}
