# Simple Time Tracker

*A lightweight Python script for recording time spent working on projects. It is designed for a single user on a Linux system.* 

## What Does Lightweight Mean?
- Single user
- Runs in a terminal
- Doesn't require any external libraries
- Uses a single database table
- Easily configured and managed using two simple JSON files

## Key Design Features

STT follows three key design principles that contributed a great deal to the success of this project:
1. Separation of User Interface, Application, and Data layers
2. Unit tests using the unittest module
3. Simple configuration and administration

### Separate Layers
1. User Interface : sttuser.py
2. Application: stt.py
3. Data: sttdata.py

The application interfaces with the user interface and the data layer. The user interface and data layer never interface directly. In theory this allows one layer to be modified without affecting the other layers. In practice, it works reasonably well, although the application is tied fairly closely to the user interface.

### Unit Tests
Using unit tests from the outset had a great impact on the design of the code. I specifially designed each piece of code so that it could be automatically tested using the unittest module. The result is very clean and bug-free code.

Each module is tested separately and the application as a whole can be tested by passing `test=True` as a parameter to the startup code. The tests are contained in the `tests` folder along with some test data, but must be run from the same folder as the main program modules.

### Simple Configuration
One of my objectives for this project was to get it up and running quickly. Towards that end, I decided that, instead of a full relational database with foreign keys and referential integrity, I would use a single database table for the time records, and JSON files for projects and activities. The JSON files are simple and flexible, and can be modified in any editor. For a project like this, the ease of administration far outweighs any potential loss of data integrity.

Required files are:
- `projects.json`
- `activities.json`

#### Example Projects File
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
    },
]
```
The projects.json file is a list of dictionary objects. Each project to be tracked must have a dictionary in the list with "name" and "status" keys at a minimum. Only projects with "status" set to "active" are displayed to the user. For projects that the user doesn't want displayed, status can be set to anything other than "active". Projects can be added at will or deleted without affecting existing data. Additional keys can be added with no effect on the program or the data.

#### Example Activities File
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

Example files are located in the `tests/data` directory

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
In a terminal, enter "python3 local/path/stt.py"

### Use Simple Time Tracker
To use STT outside of test mode:
- Navigate to the directory where you installed Simple Time Tracker.
- At the terminal prompt, enter: "python3 setup.py"
- In the `__data__` directory, modify `projects.json` and `activities.json` to suit your needs.
- If you changed the test parameter in stt.py to `True`, change it back to `False`.
- Enjoy!

### Reports
At this time STT has not implemented any reports. It is a single table database file and you can easily create your own reports if you know SQL. STT uses the SQLite3 rdbms that is included with Python. See the createdb.py file for the table schema.
