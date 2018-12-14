from make_data_dicts_for_ccle import make_data_dicts_for_ccle as make_data_dicts
from make_path_dict import make_path_dict

# ==============================================================================
# Please tell me about your feature-by-sample data.
# ==============================================================================
FEATURE_X_SAMPLE_FILE_PATH = "/media/kwatme/CarrotCake/data/cell_line/ctrp_select/ctrp_2g__compound_x_cell_line.CENTRAL_NERVOUS_SYSTEM.FIBROBLAST.MATCHED_NORMAL_TISSUE.tsv"

FEATURE_X_SAMPLE_ALIAS = "Compound CTRP 2g Central Nervous System (18.12.14)"

FEATURE_ALIAS = "Compound"

SAMPLE_ALIAS = "Cell Line"

FEATURE_X_SAMPLE_VALUE_NAME = "AUC"

HIGHLIGHT_JSON_FILE_PATH = "../code/highlight.json"

OUTPUT_DIRECTORY_PATH = "/home/kwatme/project/{}".format(FEATURE_X_SAMPLE_ALIAS)

# PLOTLY_DIRECTORY_PATH = None
PLOTLY_DIRECTORY_PATH = "Cellular Context/{}".format(FEATURE_X_SAMPLE_ALIAS)

# ==============================================================================
# How do you want to plot?
# ==============================================================================
PLOT_HEAT_MAP_MAX_SIZE = int(2e5)

PLOT_CLUSTER_MAX_SIZE = int(2e3)

PLOT_DISTRIBUTIONS_MAX_SIZE = int(2e4)

PLOT_RUG_MAX_SIZE = int(2e3)

PLOT_STD = 2.4

# ==============================================================================
# How many thread(s) are you willing to use simultaneously?
# ==============================================================================
MAX_N_JOB = 1

# ==============================================================================
# How do you want to pre-process the data?
# ==============================================================================
FEATURES_TO_DROP = None

SAMPLES_TO_DROP = None

NANIZE = None

DROP_AXIS = None

MAX_NA = None

MIN_N_NOT_NA_UNIQUE_VALUE = 1

SHIFT_AS_NECESSARY_TO_ACHIEVE_MIN_BEFORE_LOGGING = None

LOG_BASE = None

NORMALIZATION_AXIS = None

NORMALIZATION_METHOD = "-0-"

CLIP_MIN = None

CLIP_MAX = None

# ==============================================================================
# Do you want to select only good gene symbols?
# ==============================================================================
SELECT_GENE_SYMBOL = False

# ==============================================================================
# What are some elements you want to focus on?
# ==============================================================================
FEATURES_TO_PEEK = (
    "1S,3R-RSL-3",
    "austocystin D",
    "AZD4547",
    "erastin",
    "ML162",
    "ML210",
    "nintedanib",
    "selumetinib",
)

SAMPLES_TO_PEEK = (
    "HMCB_SKIN",
    "SKMEL31_SKIN",
    "CAL51_BREAST",
    "CAL148_BREAST",
    "HMC18_BREAST",
    "KPL1_BREAST",
    "MDAMB468_BREAST",
    "BEN_LUNG",
    "AM38_CENTRAL_NERVOUS_SYSTEM",
    "DAOY_CENTRAL_NERVOUS_SYSTEM",
    "SF126_CENTRAL_NERVOUS_SYSTEM",
)

# ==============================================================================
# How do you want to normalize signal?
# ==============================================================================
RAW_SIGNAL_NORMALIZATION_METHOD = "0-1"

CONTEXT_SIGNAL_NORMALIZATION_METHOD = "0-1"

# ==============================================================================
# Which element type(s) do you want use for signal?
# ==============================================================================
ELEMENT_TYPES = ("feature", "sample")

# ==============================================================================
# Which context(s) do you want use for signal?
# ==============================================================================
CONTEXTS = ("negative",)

# ==============================================================================
# Do you want to select elements automatically when making signal?
# ==============================================================================
SELECT_FEATURE_AUTOMATICALLY = False

SELECT_SAMPLE_AUTOMATICALLY = False

# ==============================================================================
# How do you want to factorize the signal?
# ==============================================================================
NMF_KS = tuple(range(2, 10))

NMF_K = 5

# ==============================================================================
# How do you want to cluster elements using the factors?
# ==============================================================================
HCC_KS = NMF_KS

W_HCC_K = NMF_K

H_HCC_K = NMF_K

# ==============================================================================
# How do you want to make match panel?
# ==============================================================================
EXTREME_FEATURE_THRESHOLD = 16

N_SAMPLING = 0

N_PERMUTATION = 0

# ==============================================================================
# How do you want to filter noisy elements when making GPS Map?
# ==============================================================================
ELEMENT_ENTROPY_QUANTILE = 1

# ==============================================================================
# How do you want to make feature GPS Map?
# ==============================================================================
GPS_MAP_W_PULL_POWER = 1.6

GPS_MAP_W_ELEMENT_MARKER_SIZE = 16

GPS_MAP_W_BANDWIDTH_FACTOR = 3.2

# ==============================================================================
# How do you want to make sample GPS Map?
# ==============================================================================
GPS_MAP_H_PULL_POWER = 1.6

GPS_MAP_H_ELEMENT_MARKER_SIZE = 24

GPS_MAP_H_BANDWIDTH_FACTOR = 2.4

# ==============================================================================
# I'm making output paths based on these settings ...
# ==============================================================================
PATH_DICT = make_path_dict(
    NMF_K, W_HCC_K, H_HCC_K, OUTPUT_DIRECTORY_PATH, PLOTLY_DIRECTORY_PATH
)

# ==============================================================================
# All set - enjoy this workflow :)
# ==============================================================================
