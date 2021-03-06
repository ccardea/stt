## Simple Time Tracker

*A lightweight Python script for recording time spent working on projects. It is designed for a single user on a Linux system.* 

### Motivation
I wanted to track how much time I spend working on projects. I probably could have used one of the more than 10,000 time tracker projects listed on PyPi, but I also needed a project to get me started using SQL again. Finally I wanted some example code that would be easy to download and run. Thus, Simple Time Tracker was born.

### Lightweight Features
- Single user.
- Runs in a separate terminal while you work.
- Doesn't require any external libraries.
- Uses a single database table.
- Easily configured and managed using two simple JSON files.
- Easy to install and run.
- Thoroughly tested.

### Key Design Principles

STT follows three key design principles that contributed a great deal to the success of this project:
1. Separation of User Interface, Application, and Data layers
2. Unit tests using the unittest module
3. Simple configuration and administration

#### Separate Layers
1. User Interface : sttuser.py
2. Application: stt.py
3. Data: sttdata.py

Even on a project as small as STT, this design principle really helped the development process, making it much easier to make changes and test one layer without affecting the others.

#### Unit Tests
Using unit tests from the outset had a great impact on the design of the code. I specifially designed each piece of code so that it could be automatically tested using the unittest module. This helped the development process and led to very clean and bug-free code.

Each module is tested separately and the application as a whole can be tested by passing `test=True` as a parameter to the startup code.

#### Simple Configuration
Two of my objectives for this project were to keep it simple and to get it up and running quickly. Towards those ends, I decided that, instead of a full relational database with foreign keys and referential integrity, I would use a single database table for the time records, and JSON files for projects and activities. The JSON files are simple and flexible, and can be modified in any editor. For a project like this, the ease of administration far outweighs any potential loss of data integrity. For more details, please see README.md on the [main project page](https://www.github.com/ccardea/stt). 

### Easy to Install and Run
Simple Time Tracker is very easy to install and run. I encourage everyone to give it a try. You can download or clone the project from the [Github Repository](https://www.github.com/ccardea/stt).

### Reports
Creating reports from STT data is completely flexible and can be output in a variety of formats. No reports have been hard-coded into the program, but sample reports and the code to create them can be found in a Jupyter Notebook, which can be viewed in the repository or on [Google Colab](https://colab.research.google.com/drive/1Q1hwEd0YKXMVSqGoksvXiFHHt1b7UmYx?usp=sharing)

### Development Time
Application: 2022-02-11 - 2022-02-16: 6 days inclusive.
Sample Reports: 2022-02-27: 1 day.