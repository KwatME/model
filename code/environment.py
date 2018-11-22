import itertools
import json
import os
from warnings import filterwarnings

import ccal
import numpy as np
import pandas as pd
import plotly as pl

from make_feature_dicts import make_feature_dicts

filterwarnings('ignore')

pl.offline.init_notebook_mode(connected=True)
