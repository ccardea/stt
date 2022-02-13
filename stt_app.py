"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-12
"""
from datetime import datetime
import stt_data as data
import stt_user

class TimeRecord():

    __slots__ = ("project", "activity", "start", "stop", "duration", "comment",)

    def __init__(self):
        self.project = None;
        self.activity = None;
        self.start = None;
        self.stop = None;
        self.duration = None;
        self.comment = None;
        return None;

    def setStart(self):
        self.start = datetime.now();
        return;

    def setStop(self):
        self.stop = datetime.now();
        self.duration = self.stop - self.start;
        return;

    def copy(self):
        temp = [self.project,self.activity,self.start,self.stop,self.duration,self.comment];
        return tuple(temp[:]);

class SimpleTimeTracker():

    __slots__ = ("projects", "activities", "flags", "record", "user", "previous");

    def __init__(self, filename):
        data.Files = data.loadFiles(filename);
        self.projects = data.getActiveProjects();
        self.activities = data.getActivities();
        self.flags = 3;
        self.record = TimeRecord();
        self.user = stt_user.TerminalUser();
        self.previous = None;
        return None;

    def getProject(self):
        choice = self.user.chooseProject(self.projects);
        self.record.project = self.projects[choice];
        return choice;

    def getActivity(self):
        choice = self.user.chooseActivity(self.activities);
        self.record.activity = self.activities[choice];
        return choice;

    def chooseStart(self):
        choices = ["Start Tracking", "Edit Project", "Edit Activity", "Exit Program"];
        text = {"Project": self.record.project, "Activity": self.record.activity}
        choice = self.user.chooseStart(choices, text);
        if choice == 0:
            self.record.setStart();
        if choice != 3:
            self.flags = choice;
        elif choice == 3:
            self.flags = 8;
        return choice;

    def chooseStop(self):
        choices = ["Stop"];
        choice = self.user.chooseStop(choices);
        self.record.setStop();
        data.writeRecord(self.record.copy());
        self.previous = self.record.copy();
        self.record.__init__();
        return;

    def chooseNext(self):
        choices = ["Resume previous activity", "New project", "New activity", "Exit program"];
        choice = self.user.chooseNext(choices);
        if choice == 0:
            self.flags = 0;
            self.record.project = self.previous[0];
            self.record.activity = self.previous[1];
        elif choice == 1:
            self.flags = 3;
        elif choice == 2:
            self.record.project = self.previous[0];
            self.flags = 2;
            self.record.project = self.previous[0];
        elif choice == 3:
            self.flags = 8;
        return choice;

    def getComment(self):
        self.record.comment = self.user.getComment();
        return;
        
    def track(self):
        while not self.flags & 8:
            if self.flags & 1:
                self.getProject();
            if self.flags & 2:
                self.getActivity();
            self.chooseStart();
            if self.flags != 0:
                continue;
            self.getComment();
            self.chooseStop();
            self.chooseNext();
        return;

if __name__ == "__main__":
    print("\nWelcome to Simple Time Tracker\n")
    stt = SimpleTimeTracker("/home/ccardea/repos/stt/tests/data/test_files.json");
    stt.track();
    print("Goodbye!")