# Simple Time Tracker

*A lightweight Python script for recording time spent working on projects. It is designed for a single user on a Linux system.* 

## Lightweight Features
- Single user.
- Runs in a separate terminal while you work.
- Doesn't require any external libraries.
- Uses a single database table.
- Easily configured and managed using two simple JSON files.
- Easy to install and run.

## Running the Program
- Download the files or clone from Github
- You must have Python installed on your system
- Tested with Python 3.8.10 on Ubuntu/Linux
- Not tested on Windows

### Take A Test Drive
If you just want to see how the program works, you can run it in test mode. Simply locate the following code in the stt.py file and change  `test=False` to `test=True`.
```
if __name__ == "__main__":
    stt = SimpleTimeTracker(test=False);
    stt.track();
    print("Goodbye!")
```
In a terminal, enter "python local/path/stt.py"

### Use Simple Time Tracker
To use STT outside of test mode:
- Navigate to the directory where you installed Simple Time Tracker.
- At the terminal prompt, enter: "python setup.py"
- In the `__data__` directory, modify `projects.json` and `activities.json` to suit your needs.
- If you changed the `test` parameter in stt.py to `True`, change it back to `False`.
- Enjoy!

### Example Projects File
```
[
    {
        "name": "Project 0", 
        "status": "active",
        "description":"Flyweight test project"
    },
    {
        "name": "Project 1",
        "status": "active",
        "description": "Lightweight test project"
    }
]
```
Each project to be tracked must have an entry with "name" and "status" keys. Only projects with "status" set to "active" are displayed to the user. For projects that the user doesn't want displayed, status can be set to anything other than "active". Projects can be added at will or deleted without affecting existing data. Additional keys can be added with no effect on the program or the data.

### Example Activities File
```
[
    "activity 0",
    "activity 1",
    "activity 2",
    "activity 3",
    "activity 4"
]
```
The activities.json file is just a list. It can be modified at any time without affecting the program operation or existing data.

### Reports
Creating reports from STT data is completely flexible and can be output in a variety of formats. No reports have been hard-coded into the program, but sample reports and the code to create them can be found in stt-reports.ipynb, which can be viewed in this repository or on [Google Colab](https://colab.research.google.com/drive/1Q1hwEd0YKXMVSqGoksvXiFHHt1b7UmYx?usp=sharing)

### Note To Developers
Tests are located in the tests folder, but must run in the root directory.