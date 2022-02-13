"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-12
"""

import stt_app as app
import unittest
import random

class TimeRecordTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.record = app.TimeRecord()
        return None

    def setUp(self):
        self.record.project = "project 1"
        self.record.activity = "activity 1"
        self.record.start = "2022:02:12:07:00:00"
        self.record.stop = "2022:02:12:09:00:00"
        self.record.duration = "02:00:00.000"
        self.record.comment = "Coding coding coding"
        return None

    def testInit(self):
        self.record.__init__()
        self.assertIsNone(self.record.project)
        self.assertIsNone(self.record.activity)
        self.assertIsNone(self.record.start)
        self.assertIsNone(self.record.stop)
        self.assertIsNone(self.record.duration)
        self.assertIsNone(self.record.comment)

    def testPause(self):
        self.record.pause()
        self.assertIsNotNone(self.record.project)
        self.assertIsNotNone(self.record.activity)
        self.assertIsNone(self.record.start)
        self.assertIsNone(self.record.stop)
        self.assertIsNone(self.record.duration)
        self.assertIsNone(self.record.comment)
        return None

    def testExport(self):
        record = self.record.export()
        self.assertIsInstance(record,tuple)
        self.assertTrue(len(record), 6)
        
class MockUser():

    def chooseProject(self, choices):
        return random.randrange(len(choices))

class AppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        file = "/home/ccardea/repos/stt/tests/data/test_files.json"
        cls.App = app.SimpleTimeTracker(file)
        cls.App.user = MockUser()
        return None

    def testInit(self):
        projects = self.App.projects
        self.assertIsInstance(projects, list)
        self.assertTrue(len(projects), 3)
        activities = self.App.activities
        self.assertIsInstance(activities, list)
        self.assertTrue(len(activities), 5)
        flags = self.App.flags
        self.assertTrue(flags & 1)
        self.assertTrue(flags & 2)
        self.assertIsInstance(self.App.record, app.TimeRecord)
        self.assertIsInstance(self.App.user, MockUser)
        return None

    def testGetProject(self):
        choice = self.App.getProject()
        self.assertEqual(self.App.record.project, self.App.projects[choice])
        return

if __name__ == "__main__":
    unittest.main()