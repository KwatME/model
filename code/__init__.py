import os
import re

import numpy as np
import pandas as pd

import kraft
from read_factorization import read_factorization

SETTING = kraft.json.read("setting.json")
