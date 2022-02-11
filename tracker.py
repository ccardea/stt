"""
Simple Time Tracker main profram loop
Author: C. Cardea
Created 02-10-2022
"""
import json
from datetime import datetime as dt

PROJECTFILE = "/home/ccardea/repos/stt/projects.json"
ACTIVITYFILE ="/home/ccardea/repos/stt/activities.json"

class Tracker():

    __slots__ = ("projects", "activities", "start", "stop", "duration", "comment")

    def __init__(self):
        with open(PROJECTFILE, "r") as fp:
            self.projects = json.load(fp)
        with open(ACTIVITYFILE) as fp:
            self.activities = json.load(fp)

    def choose_project(self):
        print("These are your current projects.")
        choices = []
        for p in enumerate(self.projects):
            choices.append(p[0])
            print(p[0], ":", p[1]["name"])
        while True:
            choice = input("Please enter the project number, or type 'exit' or 'x' to quit: ")
            if not choice.isdigit():
                if choice in ("exit", "x"):
                    return choice
                else:
                    continue
            if int(choice) not in set(choices):
                print("What was that?")
                continue
            else:
                break
        return self.projects[int(choice)]["name"]

    def choose_activity(self):
        choices = []
        print("Activities:")
        for a in enumerate(self.activities):
            choices.append(a[0])
            print(a[0], ":", a[1])
        while True:
            choice = input("Please enter the actvity number: ")
            if not choice.isdigit():
                continue
            elif int(choice) not in set(choices):
                print("What was that?")
                continue
            else:
                break
        return self.activities[int(choice)]




