import itertools
import json
import os
import warnings

import ccal
import numpy as np
import pandas as pd
import plotly as pl

from make_data_dicts import make_data_dicts

warnings.filterwarnings("ignore")

pl.offline.init_notebook_mode(connected=True)
