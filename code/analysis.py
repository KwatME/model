from numpy import add as combining_function

NAME = '<Data Type> <Description> (like: mRNA CCLE Hematopoietic Cancer)'

FEATURE_X_SAMPLE_FILE_PATH = '../data/feature_x_sample.tsv'

FEATURES_TO_DROP = None

SAMPLES_TO_DROP = None

NANIZE_0 = False

MAX_NA = None

MIN_N_NOT_NA_UNIQUE_VALUE = None

DROP_NA_AXIS = None

LOG = False

NORMALIZATION_METHOD = None

NORMALIZATION_AXIS = None

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

SAMPLES_TO_PEEK = ()

SELECT_CONTEXT = 'both'

FEATURES = None

N_TOP_FEATURE = None

SELECT_FEATURE_AUTOMATICALLY = True

FEATURE_CONTEXT_NORMALIZATION_METHOD = None

SAMPLES = None

N_TOP_SAMPLE = None

SELECT_SAMPLE_AUTOMATICALLY = False

SAMPLE_CONTEXT_NORMALIZATION_METHOD = None

COMBINING_FUNCTION = combining_function

NMF_KS = tuple(range(3, 10))

NMF_K = 8

NMF_MAP_MDS_RANDOM_SEED = 20121020

NMF_MAP_WT_PULL_POWER = 1

NMF_MAP_WT_ELEMENT_MARKER_SIZE = 8

NMF_MAP_H_PULL_POWER = 1

NMF_MAP_H_ELEMENT_MARKER_SIZE = 16

HCC_KS = NMF_KS

WT_HCC_K = NMF_K

H_HCC_K = NMF_K

NMF_MAP_WT_BANDWIDTH_FACTOR = 3.2

NMF_MAP_H_BANDWIDTH_FACTOR = 3.2
