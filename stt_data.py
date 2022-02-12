"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-11
"""
import sqlite3
import json

Files = {}

def loadFiles(filename):
    with open(filename,"r") as fp:
        data = json.load(fp)
    return data
    
def getActiveProjects():
    """
    Read projects from data store
    Returns: list
    """
    with open(Files['projects'],'r') as fp:
        projects = json.load(fp)
    active = []
    for p in projects:
        if p['status'] == "active":
            active.append(p["name"])
    return active

def getActivities():
    """
    Read activities from data store
    Returns: list
    """
    with open(Files['activities'], "r") as fp:
        activities = json.load(fp)
    return activities

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

