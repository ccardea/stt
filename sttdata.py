"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-11
"""
import sqlite3
import json
import os.path

class STTData():

    __slots__ = ("files");

    def __init__(self, test=False):
        dir = os.path.dirname(os.path.realpath(__file__));
        self.files = {};
        if test:
            self.files["projects"] = os.path.join(dir, "tests/data/projects.json");
            self.files["activities"] = os.path.join(dir, "tests/data/activities.json");
            self.files["db"] = os.path.join(dir, "tests/data/stt.db");
        else:
            self.files["projects"] = os.path.join(dir, "__data__/projects.json");
            self.files["activities"] = os.path.join(dir, "__data__/activities.json");
            self.files["db"] = os.path.join(dir, "__data__/stt.db");
        return;
    
    def getActiveProjects(self):
        """
        Read projects from data store
        Returns: list
        """
        
        with open(self.files["projects"],'r') as fp:
            projects = json.load(fp)
        active = []
        for p in projects:
            if p['status'] == "active":
                active.append(p["name"])
        return active

    def getActivities(self):
        """
        Read activities from data store
        Returns: list
        """
        with open(self.files["activities"], "r") as fp:
            activities = json.load(fp);
        return activities;

    def writeRecord(self, record):
        """
        Write record to database
        Parameters:
            record: tuple of values to write
        Returns: Success or Failure?
        """
        return

    def getRecords(project=None,range=None):
        """
        Parameters:
            range: list?
                range of data to choose from
        Returns: list of rows?
        """
        return

