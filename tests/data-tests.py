"""
Simple Time Tracker
Author: C. Cardea
Created 2022-02-12
"""
import unittest
import sttdata
from stt import TimeRecord

class DataTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        
        cls.data = sttdata.STTData(test=True)
        return ;

    def testGetActiveProjects(self):
        projects = self.data.getActiveProjects()
        self.assertIsInstance(projects, list)
        self.assertTrue(len(projects) == 3)
        return None

    def testGetActivities(self):
        activities = self.data.getActivities()
        self.assertIsInstance(activities, list)
        self.assertTrue(len(activities), 5)

    def testWriteRecord(self):
        record = TimeRecord();
        record.setStart();
        record.project = "Project 1";
        record.activity = "Activity 1";
        record.comment = "Short comment here";
        record.setStop();
        rowcount = self.data.writeRecord(record.copy());
        self.assertEqual(rowcount, 1);

if __name__ == "__main__":
    unittest.main()