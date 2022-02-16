"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-16
"""
import sttdata
import json
import os

dir = os.path.dirname(os.path.realpath(__file__));
path = os.path.join(dir, "__data__")
os.mkdir(path)

data = sttdata.STTData();
data.createDb();

proj = [
    {
        "name": "",
        "status": ""
    },
    {
        "name": "",
        "status": ""
    }
]

act = ["activity 0", "activity 1", "activity 2"]

with open(data.files["projects"],"w") as fp:
    json.dump(proj,fp, indent=4);
with open(data.files["activities"],"w") as fp:
    json.dump(act,fp, indent=4);
