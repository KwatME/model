NAME = 'mRNA Cho Medullublastoma'

MAX_PLOT_N = int(1e6)

FEATURE_X_SAMPLE_FILE_PATH = '../data/cho__gene_x_patient.tsv'

NANIZE =  40

DROP_NA_AXIS = 1

MAX_NA = 0

LOG_BASE = '2'

NORMALIZATION_AXIS = None

NORMALIZATION_METHOD = '-0-'

SELECT_GENE_SYMBOLS = True

FEATURES_TO_PEEK = (
    'APC',
    'AR',
    'AXL',
    'BRAF',
    'BRCA1',
    'CASP8AP2',
    'CDK4',
    'CDK6',
    'CTGF',
    'E2F1',
    'EGFR',
    'ERBB3',
    'ESR1',
    'EZH2',
    'FAT1',
    'GAPDH',
    'GPX1',
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
    'POU2F1',
    'POU2F2',
    'POU5F1',
    'PPP2CA',
    'PTEN',
    'RAD17',
    'RELA',
    'SOX10',
    'TP53',
    'YAP1',
    'ZEB1',
)

SAMPLES_TO_PEEK = ()

SCALE_WITH_KL = False

MAX_N_JOB = 16

SELECT_CONTEXT = 'both'

N_TOP_FEATURE = 16

SELECT_FEATURE_AUTOMATICALLY = False

NMF_KS = tuple(range(
    2,
    10,
))

NMF_K = 6

ELEMENT_ENTROPY_QUANTILE = 1

EXTREME_FEATURE_THRESHOLD = 80

GPS_MAP_MDS_RANDOM_SEED = 20121020

GPS_MAP_WT_PULL_POWER = 1.6

GPS_MAP_WT_ELEMENT_MARKER_SIZE = 16

GPS_MAP_H_PULL_POWER = 1.6

GPS_MAP_H_ELEMENT_MARKER_SIZE = 16

HCC_KS = NMF_KS

WT_HCC_K = NMF_K

H_HCC_K = NMF_K

GPS_MAP_WT_BANDWIDTH_FACTOR = 1.6

GPS_MAP_H_BANDWIDTH_FACTOR = 1.6
