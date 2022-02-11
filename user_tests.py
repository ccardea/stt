"""
Simple Test Tracker
Author C. Cardea
Created 02-10-2022
Tests for input functions,  unit tests might work here
"""

import stt_user as user
import unittest

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.choices = ["option1", "option2","option3"]

    @unittest.skip("Skipped testGetInput")
    def testGetInput(self):   
        choice = user.getInput(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None

    def testChooseProject(self):
        choice = user.chooseProject(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None

    def testChooseActivity(self):
        choice = user.chooseActivity(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None
    
    def testChooseStart(self):
        choice = user.chooseStart(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None
    
    def testChooseStop(self):
        choice = user.chooseStop(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None
    
    def testChooseResume(self):
        choice = user.chooseResume(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None
    
    def testChooseNext(self):
        choice = user.chooseNext(self.choices)
        self.assertIsInstance(choice,int)
        self.assertTrue(choice < len(self.choices))
        return None
    
class UserTestCase2(unittest.TestCase):

    @unittest.skip("Skipped testGetComent")
    def testGetComment(self):
        comment = user.getComment()
        self.assertTrue(comment.isalnum)
        self.assertTrue(comment.isprintable)
        self.assertTrue(len(comment) <= 50)
        return None

    
if __name__ == "__main__":
    unittest.main()
