import gzip
import itertools
import json
import os
import pickle
import sys
from warnings import filterwarnings

import ccal
import numpy as np
import pandas as pd
from plotly.offline import init_notebook_mode

from path import path

filterwarnings('ignore')

init_notebook_mode(connected=True)

