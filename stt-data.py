"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-11
"""
import sqlite3
import json

PROJECTFILE = "/home/ccardea/repos/stt/__data__/projects.json"
ACTIVITYFILE ="/home/ccardea/repos/stt/__data__/activities.json"

def getProjects(status):
    """
    Read projects from data store
    Parameters:
        status: string
    Returns: list
    """
    return

def getActivities():
    """
    Read activities from data store
    Returns: list
    """
    return

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
