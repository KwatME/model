NAME = 'mRNA KRAS Map Breast'

MAX_PLOT_N = int(1e6)

FEATURE_X_SAMPLE_FILE_PATH = '../data/mrna_max__gene_x_cell_line.breast.tsv'

NANIZE = 0

DROP_NA_AXIS = 1

MAX_NA = 0.05

MIN_N_NOT_NA_UNIQUE_VALUE = None

SHIFT_AS_NECESSARY_BEFORE_LOGGING = '0<'

LOG_BASE = '2'

NORMALIZATION_AXIS = 0

NORMALIZATION_METHOD = '-0-'

SELECT_GENE_SYMBOLS = True

FEATURES_TO_PEEK = (
    'APC',
    'AR',
    'AXL',
    'BRAF',
    'BRCA1',
    'CDK4',
    'CDK6',
    'E2F1',
    'EGFR',
    'ERBB3',
    'ESR1',
    'EZH2',
    'F2RL1',
    'FAT1',
    'GAPDH',
    'GPX1',
    'HNF1A',
    'IKBKE',
    'IL6',
    'IL8',
    'KRAS',
    'NOTCH1',
    'MAP4K4',
    'MTOR',
    'MYC',
    'NF1',
    'NRAS',
    'PGR',
    'PIK3CA',
    'PPP2CA',
    'PTEN',
    'RAD17',
    'RELA',
    'SOX10',
    'ST14',
    'TP53',
    'VIM',
    'YAP1',
    'ZEB1',
)

SAMPLES_TO_PEEK = ()

SCALE_WITH_KL = True

MAX_N_JOB = 33

SELECT_CONTEXT = 'both'

FEATURES_FILE_PATH = '../output/features.txt'

SELECT_FEATURE_AUTOMATICALLY = True

N_TOP_FEATURE = None

NMF_KS = tuple(range(
    2,
    10,
))

NMF_K = 6

HCC_KS = NMF_KS

WT_HCC_K = NMF_K

H_HCC_K = NMF_K

from make_feature_dicts_for_ccle import make_feature_dicts_for_ccle as make_feature_dicts

EXTREME_FEATURE_THRESHOLD = 24

ELEMENT_ENTROPY_QUANTILE = 1

GPS_MAP_WT_PULL_POWER = 1

GPS_MAP_WT_ELEMENT_MARKER_SIZE = 10

GPS_MAP_WT_BANDWIDTH_FACTOR = 2

GPS_MAP_H_PULL_POWER = 1

GPS_MAP_H_ELEMENT_MARKER_SIZE = 10

GPS_MAP_H_BANDWIDTH_FACTOR = 2

UPLOAD_TO_PLOTLY = False
