from make_path_dict import make_path_dict

# ==============================================================================
# Please tell me about your feature-by-sample data.
# ==============================================================================
FEATURE_X_SAMPLE_FILE_PATH = (
    "../data/ccle_breast_used_in_kras_map/rna_kras_map__gene_x_cell_line.breast.tsv"
)

FEATURE_X_SAMPLE_ALIAS = "RNA CCLE Breast Used in KRAS Map (18.12.07)"

FEATURE_ALIAS = "Gene"

SAMPLE_ALIAS = "Cell Line"

FEATURE_X_SAMPLE_VALUE_NAME = "Gene Expression"

HIGHLIGHT_JSON_FILE_PATH = "../data/highlight/cancer.ccle_breast_used_in_kras_map.json"

# ==============================================================================
# How do you want to plot?
# ==============================================================================
PLOT_MAX_SIZE = int(1e6)

PLOT_STD = 2.4

UPLOAD_TO_PLOTLY = True

# ==============================================================================
# How many thread(s) are you willing to use simultaneously?
# ==============================================================================
MAX_N_JOB = 1

# ==============================================================================
# How do you want to pre-process the data?
# ==============================================================================
FEATURES_TO_DROP = None

SAMPLES_TO_DROP = None

NANIZE = None  # Value less than or equal to NANIZE will become nan

DROP_AXIS = None  # "0" for column | "1" for row | None for both

MAX_NA = None

MIN_N_NOT_NA_UNIQUE_VALUE = 1

SHIFT_AS_NECESSARY_TO_ACHIEVE_MIN_BEFORE_LOGGING = "0<"

LOG_BASE = 2

NORMALIZATION_AXIS = 0

NORMALIZATION_METHOD = "-0-"  # "-0-" | "0-1" | "sum" | "rank"

CLIP_MIN = None

CLIP_MAX = None

# ==============================================================================
# Do you want to select only good gene symbols?
# ==============================================================================
SELECT_GENE_SYMBOL = True

# ==============================================================================
# What are some elements you want to focus on?
# ==============================================================================
FEATURES_TO_PEEK = (
    "AR",
    "E2F3",
    "ERBB2",
    "ERBB3",
    "ESR1",
    "HER2",
    "KRT5",
    "PGR",
    "ZEB1",
)

SAMPLES_TO_PEEK = ("HMEL_BREAST",)


# ==============================================================================
# Which element type(s) do you want to compute context for?
# ==============================================================================
ELEMENT_TYPES = ("feature",)

# ==============================================================================
# Which context(s) do you want to focus on?
# ==============================================================================
CONTEXTS = ("negative", "positive")

# ==============================================================================
# Do you want to select elements automatically when making signal?
# ==============================================================================
SELECT_FEATURE_AUTOMATICALLY = True

SELECT_SAMPLE_AUTOMATICALLY = False

# ==============================================================================
# How do you want to factorize the signal?
# ==============================================================================
NMF_KS = tuple(range(2, 10))

NMF_K = 6

# ==============================================================================
# How do you want to cluster elements using the factors?
# ==============================================================================
HCC_KS = NMF_KS

W_HCC_K = NMF_K

H_HCC_K = NMF_K

# ==============================================================================
# How do you want to make match panel?
# ==============================================================================
EXTREME_FEATURE_THRESHOLD = 24

N_SAMPLING = 0

N_PERMUTATION = 0

# ==============================================================================
# How do you want to filter noisy elements when making GPS Map?
# ==============================================================================
ELEMENT_ENTROPY_QUANTILE = 1

# ==============================================================================
# How do you want to make feature GPS Map?
# ==============================================================================
GPS_MAP_W_PULL_POWER = 2.4

GPS_MAP_W_ELEMENT_MARKER_SIZE = 10

GPS_MAP_W_BANDWIDTH_FACTOR = 6.4

# ==============================================================================
# How do you want to make sample GPS Map?
# ==============================================================================
GPS_MAP_H_PULL_POWER = 1.6

GPS_MAP_H_ELEMENT_MARKER_SIZE = 24

GPS_MAP_H_BANDWIDTH_FACTOR = 2.4

# ==============================================================================
# I'm making output paths based on these settings and populating `../output`.
# ==============================================================================
PATH_DICT = make_path_dict(
    NMF_K, W_HCC_K, H_HCC_K, FEATURE_X_SAMPLE_ALIAS, UPLOAD_TO_PLOTLY
)

# ==============================================================================
# All set! Enjoy this workflow :)
# ==============================================================================
