from make_path_dict import make_path_dict

TITLE = 'RNA CCLE Breast Used in KRAS Map (18.11.26)'

FEATURE_X_SAMPLE_FILE_PATH = '../data/ccle_breast_used_in_kras_map/rna_kras_map__gene_x_cell_line.breast.tsv'

FEATURE_NAME = 'Gene'

SAMPLE_NAME = 'Cell Line'

NANIZE = 0

DROP_AXIS = 1

MAX_NA = 0.05

MIN_N_NOT_NA_UNIQUE_VALUE = None

SHIFT_AS_NECESSARY_BEFORE_LOGGING = '0<'

LOG_BASE = '2'

NORMALIZATION_AXIS = 0

NORMALIZATION_METHOD = '-0-'

SELECT_GENE_SYMBOL = True

FEATURES_TO_PEEK = (
    'AR',
    'E2F3',
    'ERBB2',
    'ERBB3',
    'ESR1',
    'HER2',
    'KRT5',
    'PGR',
    'ZEB1',
)

SAMPLES_TO_PEEK = ('HMEL_BREAST', )

MAX_N_JOB = 1

ELEMENTS = ('feature', )

CONTEXTS = (
    'negative',
    'positive',
)

SELECT_FEATURE_AUTOMATICALLY = True

SELECT_SAMPLE_AUTOMATICALLY = False

NMF_KS = tuple(range(
    2,
    10,
))

NMF_K = 6

HCC_KS = NMF_KS

W_HCC_K = NMF_K

H_HCC_K = NMF_K

EXTREME_FEATURE_THRESHOLD = 24

ELEMENT_ENTROPY_QUANTILE = 1

GPS_MAP_W_PULL_POWER = 2

GPS_MAP_W_ELEMENT_MARKER_SIZE = 12

GPS_MAP_W_BANDWIDTH_FACTOR = 3.2

GPS_MAP_H_PULL_POWER = 1.6

GPS_MAP_H_ELEMENT_MARKER_SIZE = 24

GPS_MAP_H_BANDWIDTH_FACTOR = 3.2

PLOT_STD = 2.4

UPLOAD_TO_PLOTLY = False

PATH_DICT = make_path_dict(
    TITLE,
    NMF_K,
    W_HCC_K,
    H_HCC_K,
    UPLOAD_TO_PLOTLY,
)
