import sys, os
sys.dont_write_bytecode = True  # 不產生 pyc

import json
from Model.Domain.color import Color
from Model.Domain.station import Station
sys.path.append(os.getcwd())  # 抓取路徑

