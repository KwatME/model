from ccal import make_summary_match_panel
from pandas import read_table


def make_summary_match_panels_with_common_top_features(
        targets,
        target_type,
        feature_dicts,
        input_directory_path,
        feature_types,
        n_top_features,
        output_directory_path,
):

    selected_feature_dicts = {
        feature_type: feature_dicts[feature_type].copy()
        for feature_type in feature_types
    }

    for target_index in targets.index:

        top_features = []

        for feature_type in feature_types:

            features_ = read_table(
                '{}/{}/{}.tsv'.format(
                    input_directory_path,
                    target_index,
                    feature_type,
                ),
                index_col=0).index

            if 'RRBS' in feature_type:

                methylation_top_features = features_[-n_top_features:]

                features_ = methylation_top_features.map(
                    _get_gene_name_from_methylation_feature_name)

            top_features.append(features_[:n_top_features])

        common_top_features = top_features[0]

        for top_features_ in top_features[1:]:

            common_top_features &= top_features_

        if 0 < len(common_top_features):

            for feature_type in feature_types:

                if 'RRBS' in feature_type:

                    selected_feature_dicts[feature_type][
                        'indices'] = methylation_top_features[
                            methylation_top_features.map(
                                _get_gene_name_from_methylation_feature_name)
                            in common_top_features]

                else:

                    selected_feature_dicts[feature_type][
                        'indices'] = common_top_features

            make_summary_match_panel(
                targets.loc[target_index],
                selected_feature_dicts,
                target_type=target_type,
                title=target_index,
                html_file_path=
                '{}/{}_summary_match_panel_of_common_top_features.html'.format(
                    output_directory_path,
                    target_index,
                ),
            )


def _get_gene_name_from_methylation_feature_name(methylation_feature_name):

    return methylation_feature_name.split('_')[0]
