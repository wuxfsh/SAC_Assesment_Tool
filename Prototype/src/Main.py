import json
import webbrowser
import pandas as pd

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QWidget,\
    QLabel, QSpacerItem, QSizePolicy, QHBoxLayout
from collections import OrderedDict
import chardet

data = {
    "number": "",
    "date": "01.10.2016",
    "name": "R 3932",
    "locations": [
        {
            "depTimeDiffMin": "0",
            "name": "Spital am Pyhrn Bahnhof",
            "arrTime": "",
            "depTime": "06:32",
            "platform": "2",
            "stationIdx": "0",
            "arrTimeDiffMin": "",
            "track": "R 3932"
        },
        {
            "depTimeDiffMin": "0",
            "name": "Windischgarsten Bahnhof",
            "arrTime": "06:37",
            "depTime": "06:40",
            "platform": "2",
            "stationIdx": "1",
            "arrTimeDiffMin": "1",
            "track": ""
        },
        {
            "depTimeDiffMin": "",
            "name": "Linz/Donau Hbf",
            "arrTime": "08:24",
            "depTime": "",
            "platform": "1A-B",
            "stationIdx": "22",
            "arrTimeDiffMin": "1",
            "track": ""
        }
    ]
}

df = pd.json_normalize(data, 'locations', ['date', 'number', 'name'],
                    record_prefix='locations_')
print (df)

with open('./data/BI_Repository.json', 'r') as load_f:
    load_dict = json.load(load_f)

    entries = load_dict['entries']
    #print(entries)
