import itertools
import os
import warnings

import numpy as np
import pandas as pd
import plotly
import yaml

import ccal
from make_path_dict import make_path_dict

warnings.filterwarnings("ignore")

plotly.offline.init_notebook_mode(connected=True)
