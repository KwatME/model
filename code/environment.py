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

from make_features_to_highlight import make_features_to_highlight
from path import path

filterwarnings('ignore')

init_notebook_mode(connected=True)
