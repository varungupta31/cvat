import json
import cv2
import numpy as np
import sys
import pprint
import os

"""
The following Script inputs the .mp4 files present at 
@@@ /home/varun/Desktop/CVIT/CVATvideos/Dataset_Prepare @@@
and JSON files at
@@@ /home/varun/Desktop/CVIT/Week2/traffic_sign_detector/coco/All/MS_COCO/ @@@
NOTE - Having the same base name, i.e., '54.mp4' and '54.json'

And creates the log files for the google sheets table.
and stores in the LOCAL dir called 'logs'.
"""


pp = pprint.PrettyPrinter()
problematic_files = []

for file in sorted(os.listdir('.')):
    if(file.endswith(".json")):
        try:
            f = open(file, 'r') 
            data = json.load(f)
            track_to_frame = {}

            TrackSign = {}
            for i in data["annotations"]:

                frameList = []
                if "TS Boundary Color" in i["attributes"]["other"]:
                    i["attributes"]["TS Boundary Color"] = i["attributes"]["other"].split(":")[
                        1]

                if i["attributes"]["track_id"] not in track_to_frame.keys():
                    track_to_frame[i["attributes"]["track_id"]] = [[]]

                track_to_frame[i["attributes"]
                               ["track_id"]][0].append(i["image_id"])

                if(i["attributes"]["track_id"] not in TrackSign.keys()):
                    TrackSign[i["attributes"]["track_id"]
                              ] = data["categories"][i["category_id"]-1]["name"]

            for track in list(track_to_frame.keys()):
                track_to_frame[track].append(TrackSign[track])

            fout = open("./logs/" +
                        file[:-5]+'_log.txt', 'w')

            for track in list(track_to_frame.keys()):

                fout.write(str(file[:-5])+"\t"+str(track_to_frame[track][1]+"\t"+str(track)+"\t"+str(
                    min(track_to_frame[track][0]))+"\t"+str(max(track_to_frame[track][0]))+'\n'))

            fout.close()
            f.close()

        except:
            problematic_files.append(file)
            continue

print(problematic_files)
