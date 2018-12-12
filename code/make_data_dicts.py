from gzip import open as gzip_open
from pickle import load

from pandas import read_table


def make_data_dicts():

    data_dicts = {"feature": {}, "sample": {}}

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

        pickle_data_dicts = load(pickle_gz_file)

    for key in keys:

        data_dicts["sample"][key] = pickle_data_dicts[key]

    return data_dicts
