from ccal import make_membership_df_from_categorical_series
from pandas import read_table

from make_feature_dicts_from_pickle_gz import make_feature_dicts_from_pickle_gz


def make_feature_dicts(
        load_ccle=False,
        load_tcga=False,
):

    feature_dicts = {}

    if load_ccle:

        feature_dicts.update(
            make_feature_dicts_from_pickle_gz(
                '../data/ccle.pickle.gz',
                (
                    #  'Information',
                    'Mutation',
                    'Mutational Signature',
                    'CNV',
                    'Methylation',
                    'miRNA',
                    'RNA',
                    'Gene Set',
                    'Protein',
                    'Metabolite',
                    'Achilles RNAi',
                    'Achilles CRISPR',
                    'NP24 Compound',
                    'CTRP Compound',
                ),
                {},
            ))

    if load_tcga:

        feature_dicts.update(
            make_feature_dicts_from_pickle_gz(
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
            ))

    cell_line_state = read_table(
        '../data/pablo/states.tsv',
        index_col=0,
        header=None,
        squeeze=True,
    )

    cell_line_state.name = 'State'

    cell_line_state.index.name = 'Cell Line'

    state_x_cell_line = make_membership_df_from_categorical_series(
        cell_line_state)

    state_x_cell_line.index = ('State {}'.format(i)
                               for i in state_x_cell_line.index)

    feature_dicts['Pablo State'] = {
        'df': state_x_cell_line.append(cell_line_state),
        'data_type': 'categorical',
        'emphasis': 'high',
    }

    return feature_dicts
