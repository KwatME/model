from make_feature_dicts_from_pickle_gz import make_feature_dicts_from_pickle_gz


def make_feature_dicts_for_tcga():

    return make_feature_dicts_from_pickle_gz(
        '../data/tcga.pickle.gz',
        (
            'Categorical Information',
            'Continuous Information',
            'Mutation',
            'Mutational Signature',
            'CNV',
            'Methylation',
            'miRNA',
            'RNA',
            'Gene Set',
            'Protein',
            'Immune Signature',
        ),
        {},
    )
