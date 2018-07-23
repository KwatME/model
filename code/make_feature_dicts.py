from gzip import open as gzip_open
from pickle import load

from ccal import make_membership_df_from_categorical_series


def make_feature_dicts(
        data_name,
        information_indices_to_make_membership_df,
):

    if data_name == 'ccle':

        pickle_gz_file_path = '../data/ccle.pickle.gz'

        features = (
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

    elif data_name == 'tcga':

        pickle_gz_file_path = '../data/tcga.pickle.gz'

        features = (
            'Information',
            'Mutation',
            'Mutational Signature',
            'CNV',
            'Methylation',
            'miRNA',
            'mRNA',
            'Protein',
        )

    with gzip_open(pickle_gz_file_path) as pickle_gz_file:

        feature_dicts = load(pickle_gz_file)

    feature_dicts = {
        feature_type: feature_dicts[feature_type]
        for feature_type in features
    }

    for information_index in information_indices_to_make_membership_df:

        feature_dicts[information_index] = feature_dicts['Information'].copy()

        feature_dicts[information_index][
            'df'] = make_membership_df_from_categorical_series(feature_dicts[
                'Information']['df'].loc[information_index]).astype(int)

        feature_dicts[information_index]['data_type'] = 'binary'

    return feature_dicts
