from ccal import log_nd_array, make_membership_df_from_categorical_series
from pandas import read_table


def make_feature_dicts():

    feature_dicts = {
        'Feature Group 0': {
            'df': None
            'data_type': 'continuous',
            'emphasis': 'high',
        },
    }

    return feature_dicts
