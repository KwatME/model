from gzip import open as gzip_open
from pickle import load


def make_feature_dicts():

    feature_feature_dicts = {}

    sample_feature_dicts = {}

    # pickle_gz_file_path = '../data/ccle.pickle.gz'
    #
    # keys = (
    #     'Mutation',
    #     'Mutational Signature',
    #     'CNV',
    #     'Methylation',
    #     'RNA',
    #     'Gene Set',
    #     'Protein',
    #     'Metabolite',
    #     'RNAi',
    #     'CRISPR',
    #     'NP24',
    #     'CTRP',
    #     'Binary Information',
    # )

    pickle_gz_file_path = '../data/tcga.pickle.gz'

    keys = (
        'Mutation',
        'Mutational Signature',
        'CNV',
        'Methylation',
        'RNA',
        'miRNA',
        'Gene Set',
        'Protein',
        'Immune Signature',
        'Continuous Information',
        'Binary Information',
    )

    with gzip_open(pickle_gz_file_path) as pickle_gz_file:

        feature_dicts = load(pickle_gz_file)

    for key in keys:

        sample_feature_dicts[key] = feature_dicts[key]

    return {
        'Feature': feature_feature_dicts,
        'Sample': sample_feature_dicts,
    }
