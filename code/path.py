from ccal import establish_path, untitle_str


def path(setting):

    path_dict = {}

    directory_path = '../output/{}'.format(untitle_str(setting.NAME))

    path_dict['feature_x_sample_file_path'] = '{}/feature_x_sample.tsv'.format(
        directory_path)

    for element in (
            'feature',
            'sample',
    ):

        element_directory_path = '{}/{}'.format(
            directory_path,
            element,
        )

        path_dict['{}_directory_path'.format(element)] = element_directory_path

        path_dict['{}_skew_t_pdf_fit_parameter_file_path'.format(
            element)] = '{}/skew_t_pdf_fit_parameter.tsv'.format(
                element_directory_path)

        path_dict['{}_context_matrix_file_path'.format(
            element)] = '{}/context_matrix.tsv'.format(element_directory_path)

    signal_directory_path = '{}/signal'.format(directory_path)

    path_dict['signal_matrix_file_path'] = '{}/signal_matrix.tsv'.format(
        signal_directory_path)

    path_dict[
        'selected_signal_matrix_file_path'] = '{}/selected_signal_matrix.tsv'.format(
            signal_directory_path)

    nmf_directory_path = '{}/nmf'.format(signal_directory_path)

    path_dict['nmf_directory_path'] = nmf_directory_path

    for w_or_h in (
            'w',
            'h',
    ):

        path_dict['{}_file_path'.format(w_or_h)] = '{}/nmf_k{}_{}.tsv'.format(
            nmf_directory_path,
            setting.NMF_K,
            w_or_h,
        )

    nmf_k_directory_path = '{}/{}'.format(
        nmf_directory_path,
        setting.NMF_K,
    )

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

            hcc_k = setting.WT_HCC_K

        elif wt_or_h is 'h':

            hcc_k = setting.H_HCC_K

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

    plotly_directory_path = 'Cellular Context/{}'.format(setting.NAME)

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

        if setting.UPLOAD_TO_PLOTLY:

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
