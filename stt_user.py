"""
Simple Time Tracker
Author C. Cardea
Created 2022-02-11
"""

class TerminalUser():

    def chooseProject(self, projects):
        """
        Choose a project from a list
        Parameters:
            projects: list
        Returns: integer
            index of projects list
        """
        print("Please choose a project:")
        return self.getInput(projects)

    def chooseActivity(self,activities):
        """
        Choose an activity from a list
        Parameters:
            activities: list
        Returns: integer
            index of choices list
        """
        print("Please choose an activity:")
        return self.getInput(activities)

    def chooseStart(self,choices,text):
        """
        Choose to start or exit
        Parameters:
            choices: list
            text: dictionary
                Contains project and activity as key:value pairs
        Returns: integer index of choices list
        """
        print("Please verify project and activity before continuing.")
        print("----------------------")
        for key in text:
            print(key,":", text[key]);
        print("----------------------")
        return self.getInput(choices);

    def chooseStop(self, choices):
        """
        Allows user to stop or pause recording the current activity
        Returns: integer index of choices list
        """
        print("Please choose Stop to end or pause tracking.")
        return self.getInput(choices)

    def validate(self, comment):
        words = comment.split()
        for word in words:
            if not word.isalnum() or not word.isprintable():
                return False
        return True 


    def chooseResume(self, choices):
        """
        Allow user to resume previous activity or stop
        Parameters:
            choices: list
        Returns: integer index of choices list
        """
        print("Resume previous activity or stop")
        return self.getInput(choices)

    def chooseNext(self, choices):
        """ 
        Choose next action (new activity, new project, quit program).
            Parameters:
                choices: list
            Returns: integer index of choices list
        """
        print("What would you like to do next?")
        return self.getInput(choices)

    def getInput(self, choices):
        """
        Get Input from user
        Parameters:
            choices: list
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
        print("-----------------------------------------------------\n");
        return int(choice)
    def getComment(self):
        """
        Get comment from user input
        Returns: string
        """
        print("Please enter a comment (50 characters or less).")
        while True:
            comment = input(">>")
            if not self.validate(comment):
                print("Printable alphanumeric characters only please.")
                continue
            else:
                break
        if len(comment) <= 50:
            return comment
        else:
            return comment[0:50]