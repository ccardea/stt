"""
Simple Time Tracker Test Data
Create test data for db admin and queries
Author: C. Cardea
2022-02-23
"""
import sqlite3
import os.path
from datetime import datetime
import random
import json


class MockTimeRecord():

    __slots__ = ("project", "activity", "start", "stop", "duration", "comment",)

    def __init__(self):
        self.project = None;
        self.activity = None;
        self.start = None;
        self.stop = None;
        self.duration = None;
        self.comment = None;
        return None;

    def setStart(self, time):
        self.start = datetime(time["year"],time["month"],day=time["day"],hour=time["hour"]);
        return;

    def setStop(self,time):
        self.stop = datetime(time["year"],time["month"],day=time["day"],hour=time["hour"]);
        temp = self.stop - self.start;
        self.duration = temp.total_seconds();
        return;

    def copy(self):
        temp = [self.project,self.activity,self.start,self.stop,
            self.duration, self.comment];
        return tuple(temp[:]);

class DataBuilder():

    __slots__ = (
        "dir",
        "starts",
        "stops",
        "activities",
        "projects",
        "records"
    )

    def __init__(self):
        self.dir = os.path.dirname(os.path.realpath(__file__));
        times = self.buildDateTime();
        self.starts = times[0]
        self.stops = times[1]
        self.activities = self.getActivities();
        self.projects = self.getActiveProjects();

    def getActiveProjects(self):
            """
            Read projects from data store
            Returns: list
            """
            path = os.path.join(self.dir, "projects.json")
            with open(path,'r') as fp:
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
        path = os.path.join(self.dir, "activities.json")
        with open(path, "r") as fp:
            activities = json.load(fp);
        return activities;

    def buildDateTime(self):
        startTimes = []
        endTimes = []
        for i in range(1, 29, 1):
            for j in range(8, 18, 2):
                start = {"year":2022, "month":2}
                end = {"year":2022,"month":2}
                start["day"] = i
                end["day"] = i
                start["hour"] = j
                end["hour"] = j + 2
                startTimes.append(start)
                endTimes.append(end)
        return(startTimes, endTimes)

    def buildData(self):
        self.records = []
        for i in range(len(self.starts)):
            record = MockTimeRecord()
            record.project = random.choice(self.projects);
            record.activity = random.choice(self.activities);
            record.setStart(self.starts[i]);
            record.setStop(self.stops[i]);
            record.comment = "no comment";
            self.records.append(record.copy());
        return;

    def genRecord(self):
        for record in self.records:
            yield record;

    def insertData(self):
        sql = """
        insert into records (project, activity, start, stop, duration, comment)
        values (?,?,?,?,?,?);
        """
        path = os.path.join(self.dir, "stt.db");
        if not os.path.exists(path):
            raise Exception("Database file not found")
        conn = sqlite3.connect(path);
        cur = conn.cursor();
        cur.executemany(sql, self.genRecord());
        conn.commit();
        conn.close();

    def getAll(self):
        sql = """
            SELECT * FROM records
        """
        path = os.path.join(self.dir, "stt.db");
        conn = sqlite3.connect(path);
        cur = conn.cursor();
        cur.execute(sql);
        conn.commit();
        results = cur.fetchall();
        conn.close();
        return results;

    def deleteAll(self):
        path = os.path.join(self.dir, "stt.db");
        sql = """
        DELETE FROM records
        """
        conn = sqlite3.connect(path);
        cur = conn.cursor();
        cur.execute(sql);
        conn.commit();
        conn.close();
        return;



    