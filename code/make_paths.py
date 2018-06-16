from ccal import establish_path


def make_paths(a):

    # ==========================================================================
    paths = {}

    # ==========================================================================
    directory_path = '../output/{}'.format(a.NAME)

    # ==========================================================================
    paths['feature_x_sample_file_path'] = '{}/feature_x_sample.tsv'.format(
        directory_path)

    # ==========================================================================
    for element in ('feature', 'sample'):

        element_directory_path = '{}/{}'.format(directory_path, element)

        paths['{}_directory_path'.format(element)] = element_directory_path

        paths['{}_skew_t_pdf_fit_parameter_file_path'.format(
            element)] = '{}/skew_t_pdf_fit_parameter.tsv'.format(
                element_directory_path)

        paths['{}_1d_context_matrix_file_path'.format(
            element)] = '{}/1d_context_matrix.tsv'.format(
                element_directory_path)

    # ==========================================================================
    signal_directory_path = '{}/{}'.format(directory_path, a.SELECT_CONTEXT)

    signal_directory_path += '__feature'

    if a.FEATURES is not None:

        signal_directory_path += '__{}'.format(len(a.FEATURES))

    elif a.N_TOP_FEATURE is not None:

        signal_directory_path += '__top_{}'.format(a.N_TOP_FEATURE)

    elif a.SELECT_FEATURE_AUTOMATICALLY:

        signal_directory_path += '__auto'

    if a.FEATURE_CONTEXT_NORMALIZATION_METHOD is not None:

        signal_directory_path += '__{}'.format(
            a.FEATURE_CONTEXT_NORMALIZATION_METHOD)

    signal_directory_path += '__sample'

    if a.SAMPLES is not None:

        signal_directory_path += '__{}'.format(len(a.SAMPLES))

    elif a.N_TOP_SAMPLE is not None:

        signal_directory_path += '__top_{}'.format(a.N_TOP_SAMPLE)

    elif a.SELECT_SAMPLE_AUTOMATICALLY:

        signal_directory_path += '__auto'

    if a.SAMPLE_CONTEXT_NORMALIZATION_METHOD is not None:

        signal_directory_path += '__{}'.format(
            a.SAMPLE_CONTEXT_NORMALIZATION_METHOD)

    signal_directory_path += '__{}'.format(a.COMBINING_FUNCTION.__name__)

    paths['signal_matrix_file_path'] = '{}/signal_matrix.tsv'.format(
        signal_directory_path)

    # ==========================================================================
    nmf_directory_path = '{}/nmf'.format(signal_directory_path)

    paths['nmf_directory_path'] = nmf_directory_path

    # ==========================================================================
    for w_or_h in ('w', 'h'):

        paths['{}_file_path'.format(w_or_h)] = '{}/nmf_k{}_{}.tsv'.format(
            nmf_directory_path, a.NMF_K, w_or_h)

    nmf_k_directory_path = '{}/{}'.format(nmf_directory_path, a.NMF_K)

    for wt_or_h in ('wt', 'h'):

        wt_or_h_directory_path = '{}/{}'.format(nmf_k_directory_path, wt_or_h)

        paths['{}_directory_path'.format(wt_or_h)] = wt_or_h_directory_path

        paths['{}_match_directory_path'.format(wt_or_h)] = '{}/match'.format(
            wt_or_h_directory_path)

        paths['{}_map_directory_path'.format(wt_or_h)] = '{}/map'.format(
            wt_or_h_directory_path)

        paths['{}_hcc_directory_path'.format(wt_or_h)] = '{}/hcc'.format(
            wt_or_h_directory_path)

        paths['{}_hcc__k_x_column_file_path'.format(
            wt_or_h)] = '{}/hcc/hcc__k_x_column.tsv'.format(
                wt_or_h_directory_path)

        if wt_or_h is 'wt':

            hcc_k = a.WT_HCC_K

        elif wt_or_h is 'h':

            hcc_k = a.H_HCC_K

        paths['{}_hcc_match_directory_path'.format(
            wt_or_h)] = '{}/hcc/{}/match'.format(wt_or_h_directory_path, hcc_k)

    # ==========================================================================
    for name, path in paths.items():

        if 'file_path' in name:

            establish_path(path, 'file')

        elif 'directory_path' in name:

            establish_path(path, 'directory')

    # ==========================================================================
    plotly_directory_path = 'Cellular Context/{}'.format(a.NAME)

    # ==========================================================================
    for wt_or_h, element in (('wt', 'Feature'), ('h', 'Sample')):

        paths['{}_map_plotly_file_path'.format(
            wt_or_h)] = '{}/{} Map.html'.format(plotly_directory_path, element)

        paths['{}_state_map_plotly_file_path'.format(
            wt_or_h)] = '{}/{} State Map.html'.format(plotly_directory_path,
                                                      element)
        paths['{}_match_plotly_directory_path'.format(
            wt_or_h)] = '{}/{} Match'.format(plotly_directory_path, element)

    return paths
