from gzip import open as gzip_open
from pickle import load

from ccal import make_membership_df_from_categorical_series


def make_feature_dicts_from_pickle_gz(
        pickle_gz_file_path,
        feature_groups,
        feature_group_features,
):

    with gzip_open(pickle_gz_file_path) as pickle_gz_file:

        feature_dicts = load(pickle_gz_file)

    feature_dicts = {
        feature_group: feature_dicts[feature_group]
        for feature_group in feature_groups
    }

    for feature_group, features in feature_group_features.items():

        for feature in features:

            feature_dicts['{} {}'.format(
                feature_group,
                feature,
            )] = {
                'df':
                make_membership_df_from_categorical_series(
                    feature_dicts[feature_group]['df'].loc[feature]).astype(
                        int),
                'data_type':
                'binary',
                'emphasis':
                'high',
            }

    from pandas import read_table

    gpcr_ligand = read_table(
        '../data/gpcr_ligand.tsv',
        index_col=0,
    )

    gpcrs = set(gpcr_ligand.index)

    gpcr_ligands = set(gpcr_ligand.iloc[:, 2:].unstack().dropna())

    rna = feature_dicts['RNA']['df']

    feature_dicts['RNA GPCR'] = {
        'df': rna.loc[rna.index & gpcrs],
        'data_type': 'continuous',
        'emphasis': 'high',
    }

    feature_dicts['RNA GPCR Ligand'] = {
        'df': rna.loc[rna.index & gpcr_ligands],
        'data_type': 'continuous',
        'emphasis': 'high',
    }

    return feature_dicts
