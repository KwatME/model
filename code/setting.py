NAME = 'mRNA CCLE Glioma'

FEATURE_X_SAMPLE_FILE_PATH = '../data/mrna_max__gene_x_suffix_None__histology_glioma__hist_subtype1_None__cell_line.tsv'

FEATURES_TO_DROP = None

SAMPLES_TO_DROP = None

NANIZE_0 = True

DROP_NA_AXIS = 1

MAX_NA = 0

MIN_N_NOT_NA_UNIQUE_VALUE = None

LOG = True

NORMALIZATION_AXIS = None

NORMALIZATION_METHOD = None

SELECT_ONLY_GENES = True

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
    'DKMG_CENTRAL_NERVOUS_SYSTEM',
    'LN428_CENTRAL_NERVOUS_SYSTEM',
)

MAX_N_JOB = 1

SELECT_CONTEXT = 'both'

FEATURES = None

N_TOP_FEATURE = None

SELECT_FEATURE_AUTOMATICALLY = True

NMF_KS = tuple(range(
    2,
    10,
))

NMF_K = 4

EXTREME_FEATURE_THRESHOLD = 16

NMF_MAP_MDS_RANDOM_SEED = 20121020

NMF_MAP_WT_PULL_POWER = 1.6

NMF_MAP_WT_ELEMENT_MARKER_SIZE = 8

NMF_MAP_H_PULL_POWER = 1.6

NMF_MAP_H_ELEMENT_MARKER_SIZE = 24

HCC_KS = NMF_KS

WT_HCC_K = 8

H_HCC_K = 8

NMF_MAP_WT_BANDWIDTH_FACTOR = 1.6

NMF_MAP_H_BANDWIDTH_FACTOR = 1.6
