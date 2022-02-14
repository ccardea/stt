"""
Simple Time Tracker
Author: C. Cardea
Created 2022-02-12
"""
import unittest
import sttdata as data

class DataTestCase(unittest.TestCase):
    
    def setUp(self):
        file = "/home/ccardea/repos/stt/tests/data/test_files.json"
        data.Files = data.loadFiles(file)
        return None

    def testLoadFiles(self):
        self.assertIsInstance(data.Files, dict)
        self.assertTrue(len(data.Files) == 2)
        return None

    def testGetActiveProjects(self):
        projects = data.getActiveProjects()
        self.assertIsInstance(projects, list)
        self.assertTrue(len(projects) == 3)
        return None

    def testGetActivities(self):
        activities = data.getActivities()
        self.assertIsInstance(activities, list)
        self.assertTrue(len(activities), 5)

if __name__ == "__main__":
    unittest.main()