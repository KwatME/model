import gzip
import itertools
import os
import pickle
import sys
from warnings import filterwarnings

import ccal
import numpy as np
import pandas as pd
from plotly.offline import init_notebook_mode

from compute_correlation_distance import compute_correlation_distance
from make_feature_dicts import make_feature_dicts
from make_features_to_highlight import make_features_to_highlight
from make_summary_match_panels_with_common_top_features import \
    make_summary_match_panels_with_common_top_features
from path import path
from select_gene_symbols import select_gene_symbols

filterwarnings('ignore')

init_notebook_mode(connected=True)
