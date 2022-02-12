"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-11
"""
from socketserver import ThreadingUnixDatagramServer


def chooseProject(projects):
    """
    Choose a project from a list
    Parameters:
        projects: list
    Returns: integer
        index of projects list
    """
    print("Please choose a project:")
    return getInput(projects)

def chooseActivity(activities):
    """
    Choose an activity from a list
    Parameters:
        activities: list
    Returns: integer
        index of choices list
    """
    print("Please choose an activity:")
    return getInput(activities)

def chooseStart(choices):
    """
    Choose to start or exit
    Parameters:
        choices: list
    Returns: integer index of choices list
    """
    print("Please choose start to begin tracking.")
    return getInput(choices)

def chooseStop(choices):
    """
    Allows user to stop or pause recording the current activity
    Returns: integer index of choices list
    """
    print("Please choose stop to end or pause to return later")
    return getInput(choices)

def getComment():
    """
    Get comment from user input
    Returns: string
    """
    print("Please enter a comment (50 characters or less).")
    while True:
        comment = input(">>")
        if not validate(comment):
            print("Printable alphanumeric characters only please.")
            continue
        else:
            break
    if len(comment) <= 50:
        return comment
    else:
        return comment[0:50]

def validate(comment):
    words = comment.split()
    for word in words:
        if not word.isalnum() or not word.isprintable():
            return False
    return True 


def chooseResume(choices):
    """
    Allow user to resume previous activity or stop
    Parameters:
        choices: list
    Returns: integer index of choices list
    """
    print("Resume previous activity or stop")
    return getInput(choices)

def chooseNext(choices):
    """ 
    Choose next action (new activity, new project, quit program).
        Parameters:
            choices: list
        Returns: integer index of choices list
    """
    print("Where to next?")
    return getInput(choices)

def getInput(choices):
    """
    Get Input from user
    Parameters:
        choices: list
        prompt: string input prompt
    Returns: integer index of choices list
    """
    prompt = "Please enter the number that identifies your choice: "
    for a in enumerate(choices):
            print(a[0], ":", a[1])
    while True:
        choice = input(prompt)
        if not choice.isdigit():
            print("What was that?")
            continue
        elif int(choice) >= len(choices) or int(choice) < 0:
            print("What was that?")
            continue
        else:
            break
    return int(choice)