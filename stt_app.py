"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-12
"""
from encodings import normalize_encoding
import stt_data as data
import stt_user

class TimeRecord():

    __slots__ = ("project", "activity", "start", "stop", "duration", "comment")

    def __init__(self):
        self.project = None
        self.activity = None
        self.start = None
        self.stop = None
        self.duration = None
        self.comment = None
        return None

    def pause(self):
        self.start = None
        self.stop = None
        self.duration = None
        self.comment = None
        return None

    def export(self):
        return (self.project,self.activity,self.start,self.stop,self.duration,self.comment)

class SimpleTimeTracker():

    __slots__ = ("projects", "activities", "flags", "record", "user")

    def __init__(self, filename):
        data.Files = data.loadFiles(filename)
        self.projects = data.getActiveProjects()
        self.activities = data.getActivities()
        self.flags = 3
        self.record = TimeRecord()
        self.user = stt_user.TerminalUser()
        return None 

    def getProject(self):
        choice = self.user.chooseProject(self.projects)
        self.record.project = self.projects[choice]
        return choice
    