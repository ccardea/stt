# Simple Time Tracker

*A lightweight Python script for recording time spent working on projects. It is designed for a single user on a Linux system.* 

## Motivation
It occurred to me that potential employers might want to know how much time I spent working on projects that I intend to use for demonstration purposes. I probably could have used one of the more than 10,000 time tracker projects listed on PyPi, but I also needed a project to refresh my SQL skills. Finally I wanted some example code that would be easy to download and run. Thus, Simple Time Tracker was born.

## Lightweight Features
- Single user.
- Runs in a separate terminal while you work.
- Doesn't require any external libraries.
- Uses a single database table.
- Easily configured and managed using two simple JSON files.
- Easy to install and run.

## Key Design Principles

STT follows three key design principles that contributed a great deal to the success of this project:
1. Separation of User Interface, Application, and Data layers
2. Unit tests using the unittest module
3. Simple configuration and administration

### Separate Layers
1. User Interface : sttuser.py
2. Application: stt.py
3. Data: sttdata.py

The application interfaces with both the user interface and the data layer. The user interface and data layer are completely separate. In theory this allows one layer to be modified without affecting the other layers. In practice, it works well. For example, to implement a graphical or web-based user interface would require only minor changes to the application, and none to the data layer.

### Unit Tests
Using unit tests from the outset had a great impact on the design of the code. I specifially designed each piece of code so that it could be automatically tested using the unittest module. This helped the development process and led to very clean and bug-free code.

Each module is tested separately and the application as a whole can be tested by passing `test=True` as a parameter to the startup code.

### Simple Configuration
Two of my objectives for this project were to keep it simple and to get it up and running quickly. Towards those ends, I decided that, instead of a full relational database with foreign keys and referential integrity, I would use a single database table for the time records, and JSON files for projects and activities. The JSON files are simple and flexible, and can be modified in any editor. For a project like this, the ease of administration far outweighs any potential loss of data integrity. For more details, please see README.md on the main project page. 

### Easy to Install and Run
Simple Time Tracker is very easy to install and run. I encourage everyone to give it a try. You can download or clone the project at https://www.github.com/ccardea/stt

### Development Time
9 days from concept to this point, including researching SQLite3 and SQLite syntax, which I had not used before, and learning a couple more modules that were new to me.