from gzip import open as gzip_open
from pickle import load

from ccal import make_membership_df_from_categorical_series


def make_feature_dicts():

    with gzip_open('../../../data/ccle.pickle.gz') as pickle_gz_file:

        feature_dicts = load(pickle_gz_file)

    feature_dicts = {
        feature_type: feature_dicts[feature_type]
        for feature_type in (
            'Information',
            'Mutation',
            'Mutational Signature',
            'CNV',
            'RRBS TSS 1kB',
            'RRBS TSS Cluster',
            'miRNA',
            'mRNA',
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
        )
    }

    # feature_dicts['Primary Site'] = feature_dicts['Information'].copy()
    #
    # feature_dicts['Primary Site'][
    #     'df'] = make_membership_df_from_categorical_series(
    #         feature_dicts['Information']['df'].loc['Site Primary']).astype(int)

    # feature_dicts['Primary Site']['data_type'] = 'binary'

    feature_dicts['Histology Subtype'] = feature_dicts['Information'].copy()

    feature_dicts['Histology Subtype'][
        'df'] = make_membership_df_from_categorical_series(feature_dicts[
            'Information']['df'].loc['Hist Subtype1']).astype(int)

    feature_dicts['Histology Subtype']['data_type'] = 'binary'

    feature_dicts.pop('Information')

    return feature_dicts
