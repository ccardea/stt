"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-11
"""
import sqlite3
import json
import os.path

class STTData():

    __slots__ = ("test", "dir");

    def __init__(self, test=False):
        self.test = test;
        self.dir = os.path.dirname(os.path.realpath(__file__));
        return;
    
    def getActiveProjects(self):
        """
        Read projects from data store
        Returns: list
        """
        if self.test:
            projectFile = os.path.join(self.dir, 'tests/data/projects.json');
        else:
            projectFile =os.path.join(self.dir, '__data__/projects.json');

        with open(projectFile,'r') as fp:
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
        if self.test:
            activityFile = os.path.join(self.dir, 'tests/data/activities.json');
        else:
            activityFile = os.path.join(self.dir, '__data__/activities.json');
        with open(activityFile, "r") as fp:
            activities = json.load(fp);
        return activities;

    def writeRecord(record):
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

