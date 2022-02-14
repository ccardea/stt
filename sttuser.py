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
            text: tuple
                Contains project and activity names
        Returns: integer index of choices list
        """
        print("Please verify project and activity before continuing.")
        print("----------------------")
        print(text[0])
        print(text[1])
        print("----------------------")
        return self.getInput(choices);

    def chooseNext(self, choices, text):
        """ 
        Choose next action (new activity, new project, quit program).
            Parameters:
                choices: list
                text: tuple containing project and activity names and duration
            Returns: integer index of choices list
        """
        print("----------------------------------------")
        print("Finished tracking", text[0], text[1]);
        print("Time recorded:", str(text[2]))
        print("-----------------------------------------")
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
    def getComment(self, text):
        """
        Get comment from user input
        Parameters:
            text: tuple
                Contains project and activity names
        Returns: string
        """
        print("Tracking:", text[0], text[1]);
        print("Please type a short comment and press enter to stop tracking.")
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

    def validate(self, comment):
        words = comment.split()
        for word in words:
            if not word.isalnum() or not word.isprintable():
                return False
        return True