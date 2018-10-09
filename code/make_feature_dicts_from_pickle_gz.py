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

    return feature_dicts
