"""
Simple Time Tracker tests for genData.py
Author C. Cardea
Created 2022-02-23
"""
import unittest
import random
import gen_data
from datetime import datetime

class TestDataBuilder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.builder = gen_data.DataBuilder()

    def testBuildDateTime(self):
        starts = self.builder.starts
        stops = self.builder.stops
        self.assertIsInstance(starts, list)
        self.assertIsInstance(stops, list)
        self.assertEqual(len(starts), len(stops))

    def testProjects(self):
        projects = self.builder.projects;
        self.assertIsInstance(projects,list);
        self.assertEqual(len(projects), 3);

    def testActivities(self):
        activities = self.builder.activities;
        self.assertIsInstance(activities,list);
        self.assertEqual(len(activities),5);

    def testTimes(self):
        record = gen_data.MockTimeRecord();
        record.setStart(self.builder.starts[0]);
        self.assertIsInstance(record.start, datetime);
        record.setStop(self.builder.stops[0]);
        self.assertIsInstance(record.stop, datetime);
        self.assertIsInstance(record.duration, float);

    def testBuildData(self):
        self.builder.buildData();
        records = self.builder.records
        self.assertIsInstance(records, list);
        self.assertEqual(len(records), len(self.builder.starts));
        choice = records[random.randrange(len(records))]
        self.assertIsInstance(choice, tuple);
        self.assertEqual(len(choice), 6)
        return;

    def testGenRecord(self):
        generator = self.builder.genRecord()
        record = generator.__next__()
        self.assertIsInstance(record,tuple)
        self.assertEqual(len(record), 6)

    def testInsert(self):
        self.builder.insertData();
        data = self.builder.getAll();
        self.assertIsInstance(data,list)

    @classmethod
    def tearDownClass(cls):
        cls.builder.deleteAll();

if __name__ == "__main__":
    unittest.main()