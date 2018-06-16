from numpy import multiply as combining_function

NAME = 'CRISPR (Achilles 17Q2)'

FEATURE_X_SAMPLE_FILE_PATH = '../data/viability_after_knockout__achilles_vavana_17q2_v2__gene_x_cell_line.tsv'

FEATURES_TO_DROP = None

SAMPLES_TO_DROP = None

NANIZE_0 = False

MIN_N_NOT_NA_UNIQUE_VALUE = 64

LOG = False

NORMALIZATION_METHOD = '-0-'

NORMALIZATION_AXIS = 1

FEATURES_TO_PEEK = (
    'APC',
    'BRAF',
    'BRCA1',
    'CASP8AP2',
    'CDK6',
    'CTGF',
    'CTNNB1',
    'EGFR',
    'ERBB3',
    'E2F1',
    'EZH2',
    'FAT1',
    'GAPDH',
    'GPX',
    'KRAS',
    'MAP4K4',
    'MTOR',
    'MYC',
    'NF1',
    'NRAS',
    'PAX8',
    'PIK3CA',
    'POU2F1',
    'POU2F2',
    'POU5F1',
    'PPP2CA',
    'PRKCA',
    'PTEN',
    'RAD17',
    'RELA',
    'SOX10',
    'TCF7L2',
    'TP53',
    'YAP1',
    'ZEB1',
)

SAMPLES_TO_PEEK = (
    'HCC1395_BREAST',
    'CL40_LARGE_INTESTINE',
)

SELECT_CONTEXT = 'negative'

ALL_FEATURES = False

FEATURES = None

N_TOP_FEATURE = 1000

SELECT_FEATURE_AUTOMATICALLY = False

FEATURE_CONTEXT_NORMALIZATION_METHOD = '0-1'

ALL_SAMPLES = True

SAMPLES = None

N_TOP_SAMPLE = None

SELECT_SAMPLE_AUTOMATICALLY = False

SAMPLE_CONTEXT_NORMALIZATION_METHOD = '0-1'

COMBINING_FUNCTION = combining_function

NMF_KS = tuple(range(3, 18))

NMF_K = 14

NMF_MAP_MDS_RANDOM_SEED = 20121020

NMF_MAP_WT_PULL_POWER = 1.6

NMF_MAP_WT_ELEMENT_MARKER_SIZE = 16

NMF_MAP_H_PULL_POWER = 1.6

NMF_MAP_H_ELEMENT_MARKER_SIZE = 24

HCC_KS = NMF_KS

WT_HCC_K = 14

H_HCC_K = 14

NMF_MAP_WT_BANDWIDTH_FACTOR = 6.4

NMF_MAP_H_BANDWIDTH_FACTOR = 6.4
