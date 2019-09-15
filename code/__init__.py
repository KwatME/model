import itertools
import os

import numpy as np
import pandas as pd

import kraft
from make_path_dict import make_path_dict

SETTING = kraft.read_json("../project.json")

if "project_directory_path" in SETTING:

    SETTING.update(
        kraft.read_json(os.path.join(SETTING["project_directory_path"], "project.json"))
    )

    SETTING["output_directory_path"] = os.path.join(
        SETTING["project_directory_path"], "output"
    )

PATH = make_path_dict(SETTING)
