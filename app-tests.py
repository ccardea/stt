"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-12
"""

import stt as app
import unittest
import random, datetime

class TimeRecordTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.record = app.TimeRecord()
        return None

    def testInit(self):
        self.record.__init__()
        self.assertIsNone(self.record.project)
        self.assertIsNone(self.record.activity)
        self.assertIsNone(self.record.start)
        self.assertIsNone(self.record.stop)
        self.assertIsNone(self.record.duration)
        self.assertIsNone(self.record.comment)
        return;

    def testSetStart(self):
        self.record.setStart();
        self.assertIsInstance(self.record.start, datetime.datetime);
        return;

    def testSetStop(self):
        self.record.start = datetime.datetime.now();
        self.record.setStop();
        self.assertIsInstance(self.record.stop, datetime.datetime);
        self.assertIsInstance(self.record.duration,datetime.timedelta);
        return;

    def testCopy(self):
        self.record.project = "project 1"
        self.record.activity = "activity 1"
        self.record.start = "2022:02:12:07:00:00"
        self.record.stop = "2022:02:12:09:00:00"
        self.record.duration = "02:00:00.000"
        self.record.comment = "Coding coding coding"
        record = self.record.copy()
        self.assertIsInstance(record,tuple)
        self.assertTrue(len(record), 6)
        
class MockUser():

    def __init__(self):
        self.chooseStartCalls =  0;
        self.chooseNextCalls = 0;

    def chooseProject(self, choices):
        return random.randrange(len(choices))

    def chooseActivity(self, choices):
        return random.randrange(len(choices))

    def chooseStart(self, choices,text):
        choice = self.chooseStartCalls;
        self.chooseStartCalls +=1;
        return choice;

    def chooseNext(self, choices, text):
        choice = self.chooseNextCalls;
        self.chooseNextCalls +=1;
        return choice;

    def chooseStop(self, choices):
        return 0;

    def getComment(self, text):
        return "comment";

class AppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file = "/home/ccardea/repos/stt/tests/data/test_files.json"
        cls.App = app.SimpleTimeTracker(cls.file)
        cls.App.user = MockUser()
        return None

    def setUp(self):
        self.App.flags = 3;

    def testInit(self):
        self.App.__init__(self.file);
        projects = self.App.projects;
        self.assertIsInstance(projects, list);
        self.assertTrue(len(projects), 3);
        activities = self.App.activities;
        self.assertIsInstance(activities, list);
        self.assertTrue(len(activities), 5);
        flags = self.App.flags;
        self.assertTrue(flags & 1);
        self.assertTrue(flags & 2);
        self.assertIsInstance(self.App.record, app.TimeRecord);
        self.assertIsNone(self.App.previous);
        
        return None;

    def testGetProject(self):
        choice = self.App.getProject()
        self.assertEqual(self.App.record.project, self.App.projects[choice])
        return

    def testGetActivity(self):
        choice = self.App.getActivity();
        self.assertEqual(self.App.record.activity, self.App.activities[choice])
        return 

    def testChooseStart(self):
        choice = self.App.chooseStart();
        self.assertEqual(choice, 0);
        self.assertEqual(choice, self.App.flags)
        self.assertIsNotNone(self.App.record.start)
        self.assertIsInstance(self.App.record.start, datetime.datetime)

        choice = self.App.chooseStart();
        self.assertEqual(choice, 1);
        self.assertTrue(self.App.flags & 1);
        self.assertFalse(self.App.flags & 2);
        self.assertFalse(self.App.flags & 8);

        choice = self.App.chooseStart();
        self.assertEqual(choice, 2);
        self.assertTrue(self.App.flags & 2);
        self.assertFalse(self.App.flags & 1);
        self.assertFalse(self.App.flags & 8);

        choice = self.App.chooseStart();
        self.assertEqual(choice, 3);
        self.assertTrue(self.App.flags & 8);
        return

    def testChooseNext(self):
        self.App.record.project = "Project 1";
        self.App.record.activity = "Activity 1";
        self.App.record.setStart();
        self.App.getComment()
        choice = self.App.chooseNext();
        self.assertEqual(choice, 0);
        self.assertEqual(self.App.record.project, self.App.previous[0])
        self.assertFalse(self.App.flags &1);
        self.assertFalse(self.App.flags &2);
        self.assertFalse(self.App.flags &8);

        choice = self.App.chooseNext();
        self.assertEqual(choice, 1);
        self.assertTrue(self.App.flags & 1);
        self.assertTrue(self.App.flags & 2);
        self.assertFalse(self.App.flags & 8);

        choice = self.App.chooseNext();
        self.assertEqual(choice, 2);
        self.assertFalse(self.App.flags & 1);
        self.assertTrue(self.App.flags & 2);
        self.assertFalse(self.App.flags & 8);

        choice = self.App.chooseNext();
        self.assertEqual(choice, 3);
        self.assertFalse(self.App.flags & 1);
        self.assertFalse(self.App.flags & 2);
        self.assertTrue(self.App.flags & 8);

    def testGetComment(self):
        self.App.getComment();
        self.assertIsNotNone(self.App.previous);
        self.assertIsInstance(self.App.previous[5], str);


if __name__ == "__main__":
    unittest.main()