"""
Simple Test Tracker
Author C. Cardea
Created 02-10-2022
Tests for input functions,  unit tests might work here
"""

import tracker 

def test_choose_project():
    stt = tracker.Tracker()
    stt.choose_project()
    return None

def test_choose_activity():
    stt = tracker.Tracker()
    return stt.choose_activity()

if __name__ == "__main__":
    activity = test_choose_activity()
    print(activity)