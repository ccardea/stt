"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-11
"""
import sqlite3
import json
import os.path
from createdb import create

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

    def dbExists(self):
        if os.path.exists(self.files["db"]):
            return True;
        else:
            return False;
    
    def createDb(self):
        create(self.files["db"]);
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
        sql = """
            INSERT INTO records (
                project, activity, start, stop, duration, comment
            )
            VALUES (?,?,?,?,?,?)
        """
        conn = sqlite3.connect(self.files["db"]);
        cur = conn.cursor();
        cur.execute(sql, record);
        conn.commit();
        conn.close();
        return cur.rowcount;

    def queryAll(self):
        """
        Simple Select.
            Returns a list of rows.
            
        """
        sql = """
            SELECT * FROM records
        """
        conn = sqlite3.connect(self.files["db"]);
        cur = conn.cursor();
        cur.execute(sql);
        conn.commit();
        results = cur.fetchall();
        conn.close();
        return results;

    def deleteAll(self):
        """
        Deletes all rows from the records table.
        Used for testing purposes
        """
        sql = """
        DELETE FROM records
        """
        conn = sqlite3.connect(self.files["db"]);
        cur = conn.cursor();
        cur.execute(sql);
        conn.commit();
        conn.close();
        return;

