import itertools
import json
import os
import warnings

import ccal
import numpy as np
import pandas as pd
import plotly as pl

warnings.filterwarnings("ignore")

pl.offline.init_notebook_mode(connected=True)
