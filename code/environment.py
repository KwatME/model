import itertools
import json
import os

import ccal
import numpy as np
import pandas as pd
from plotly.offline import init_notebook_mode

from make_feature_dicts import make_feature_dicts
from path import path

init_notebook_mode(connected=True)
