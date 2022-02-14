"""
Simple Test Tracker
Author C. Cardea
Created 02-10-2022
Tests for input functions,  unit tests might work here
"""

import sttuser
import unittest

class UserTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = stt_user.TerminalUser()
        return None

    def setUp(self):
        self.choices = ["option1", "option2","option3"]
        print("\n")

    # @unittest.skip("Skipped testGetInput")
    def testGetInput(self):   
        choice = self.user.getInput(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None

    def testChooseProject(self):
        choice = self.user.chooseProject(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None

    def testChooseActivity(self):
        choice = self.user.chooseActivity(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None
    
    def testChooseStart(self):
        text = ("Project 1", "Activity 1")
        choice = self.user.chooseStart(self.choices, text)
        self.assertIsInstance(choice,int);
        self.assertTrue(choice < len(self.choices))
        return None
    
    def testChooseNext(self):
        text = ("Project 1", "Activity 1", "00:30:29.000")
        choice = self.user.chooseNext(self.choices, text)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None
    
class UserTestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = stt_user.TerminalUser()
        return None

    # @unittest.skip("Skipped testGetComent")
    def testGetComment(self):
        text = ("Project 1", "Activity 1")
        comment = self.user.getComment(text)
        self.assertIsInstance(comment, str)
        self.assertTrue(comment.isprintable())
        self.assertTrue(len(comment) <= 50)
        return None

    
if __name__ == "__main__":
    unittest.main()
