from ccal import establish_path


def path(
        NAME,
        NMF_K,
        WT_HCC_K,
        H_HCC_K,
        UPLOAD_TO_PLOTLY,
):

    path_dict = {}

    path_dict['feature_x_sample_file_path'] = '../output/feature_x_sample.tsv'

    for element in (
            'feature',
            'sample',
    ):

        element_directory_path = '../output/{}'.format(element)

        path_dict['{}_directory_path'.format(element)] = element_directory_path

        path_dict['{}_skew_t_pdf_fit_parameter_file_path'.format(
            element)] = '{}/skew_t_pdf_fit_parameter.tsv'.format(
                element_directory_path)

        path_dict['{}_context_matrix_file_path'.format(
            element)] = '{}/context_matrix.tsv'.format(element_directory_path)

    path_dict['signal_matrix_file_path'] = '../output/signal/signal_matrix.tsv'

    path_dict[
        'selected_signal_matrix_file_path'] = '../output/signal/selected_signal_matrix.tsv'

    path_dict['nmf_directory_path'] = '../output/signal/nmf'

    for w_or_h in (
            'w',
            'h',
    ):

        path_dict['{}_file_path'.format(
            w_or_h)] = '../output/signal/nmf/nmf_k{}_{}.tsv'.format(
                NMF_K,
                w_or_h,
            )

    nmf_k_directory_path = '../output/signal/nmf/{}'.format(NMF_K)

    for wt_or_h in (
            'wt',
            'h',
    ):

        wt_or_h_directory_path = '{}/{}'.format(
            nmf_k_directory_path,
            wt_or_h,
        )

        path_dict['{}_directory_path'.format(wt_or_h)] = wt_or_h_directory_path

        path_dict['{}_match_directory_path'.format(
            wt_or_h)] = '{}/match'.format(wt_or_h_directory_path)

        path_dict['{}_map_directory_path'.format(wt_or_h)] = '{}/map'.format(
            wt_or_h_directory_path)

        path_dict['{}_hcc_directory_path'.format(wt_or_h)] = '{}/hcc'.format(
            wt_or_h_directory_path)

        path_dict['{}_hcc__k_x_column_file_path'.format(
            wt_or_h)] = '{}/hcc/hcc__k_x_column.tsv'.format(
                wt_or_h_directory_path)

        if wt_or_h is 'wt':

            hcc_k = WT_HCC_K

        elif wt_or_h is 'h':

            hcc_k = H_HCC_K

        path_dict['{}_hcc_match_directory_path'.format(
            wt_or_h)] = '{}/hcc/{}/match'.format(
                wt_or_h_directory_path,
                hcc_k,
            )

    path_dict['gps_map_file_path'] = '{}/gps_map.pickle.gz'.format(
        nmf_k_directory_path)

    for name, path in path_dict.items():

        if 'file_path' in name:

            establish_path(
                path,
                'file',
            )

        elif 'directory_path' in name:

            establish_path(
                path,
                'directory',
            )

    plotly_directory_path = 'Cellular Context/{}'.format(NAME)

    for wt_or_h, element in (
        (
            'wt',
            'Feature',
        ),
        (
            'h',
            'Sample',
        ),
    ):

        if UPLOAD_TO_PLOTLY:

            path_dict['{}_map_plotly_file_path'.format(
                wt_or_h)] = '{}/{} Map.html'.format(
                    plotly_directory_path,
                    element,
                )

            path_dict['{}_state_map_plotly_file_path'.format(
                wt_or_h)] = '{}/{} State Map.html'.format(
                    plotly_directory_path,
                    element,
                )

            path_dict['{}_state_maps_plotly_directory_path'.format(
                wt_or_h)] = '{}/{} State Maps'.format(
                    plotly_directory_path,
                    element,
                )

            path_dict['{}_match_plotly_directory_path'.format(
                wt_or_h)] = '{}/{} Match'.format(
                    plotly_directory_path,
                    element,
                )

        else:

            path_dict['{}_map_plotly_file_path'.format(wt_or_h)] = None

            path_dict['{}_state_map_plotly_file_path'.format(wt_or_h)] = None

            path_dict['{}_state_maps_plotly_directory_path'.format(
                wt_or_h)] = None

            path_dict['{}_match_plotly_directory_path'.format(wt_or_h)] = None

    return path_dict
