from make_feature_dicts_from_pickle_gz import make_feature_dicts_from_pickle_gz


def make_feature_dicts_for_ccle():

    return make_feature_dicts_from_pickle_gz(
        '../data/ccle.pickle.gz',
        (
#             'Information',
            'Mutation',
            'Mutational Signature',
            'CNV',
            'RRBS TSS 1kB',
            'RRBS TSS Cluster',
            'miRNA',
            'RNA',
            'Gene Set Affymetrix',
            'Gene Set C1',
            'Gene Set C2',
            'Gene Set C3',
            'Gene Set C6',
            'Gene Set Hallmark',
            'Gene Set IPA Regulator',
            'Gene Set Isogenic Signature',
            'Protein',
            'Metabolite',
            'Achilles RNAi',
            'Achilles CRISPR',
            'NP24 Compound',
            'CTRP Compound',
        ),
        {},
    )
