from ccal import log_nd_array, make_membership_df_from_categorical_series
from pandas import DataFrame, read_table


def make_feature_dicts():

    cho_subtype = make_membership_df_from_categorical_series(
        read_table(
            '../data/patient_subtype.tsv',
            index_col=0,
            squeeze=True,
        ))

    rna = read_table(
        '../data/cho__gene_x_patient.tsv',
        index_col=0,
    )

    rna = DataFrame(
        log_nd_array(rna.values),
        index=rna.index,
        columns=rna.columns,
    )

    feature_dicts = {
        'Cho Subtype': {
            'df': cho_subtype,
            'data_type': 'binary',
            'emphasis': 'high',
        },
        'RNA': {
            'df': rna,
            'data_type': 'continuous',
            'emphasis': 'high',
        },
    }

    return feature_dicts
