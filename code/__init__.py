import os
import re

import numpy as np
import pandas as pd
import plotly as pl

import kraft
from read_ws_hs import read_ws_hs

SETTING = kraft.read_json("../project.json")

if "project_directory_path" in SETTING:

    SETTING.update(
        kraft.read_json("{}/project.json".format(SETTING["project_directory_path"]))
    )

OUTPUT_DIRECTORY_PATH = "{}/output".format(SETTING["project_directory_path"])

kraft.establish_path(OUTPUT_DIRECTORY_PATH, "directory")
