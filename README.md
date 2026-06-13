# Student Mark Analyzer System


The Student Mark Analyzer System is a Python-based desktop application designed to manage student academic records efficiently. It uses SQLite as a database for storing student information and Pandas for analyzing marks and generating results.

The system automates calculation of total marks, average marks, and grade assignment, reducing manual effort and improving accuracy in academic record handling.

### Key Features
### Login System

Secure admin authentication is implemented using a username and password stored in the database.

#### Add Student

Allows insertion of student details including name and subject-wise marks into the database.

#### View Students

Displays all student records with automatic calculation of total marks, average marks, and grades.

#### Search Student

Enables searching of student records using name-based matching for quick retrieval.

#### Automatic Grading

The system assigns grades based on average marks using predefined logic.


## Technologies Used
Python 3.x – Core programming language
SQLite – Lightweight database system
Pandas – Data analysis and table formatting
sqlite3 – Database connectivity module


## Project Structure

```
Student-Mark-Analyzer-System/
│
├── student_system.py
├── student_system.db (auto-generated)
└── README.md
```

## Installation & Setup
1. Clone or Download Project

Download the project files into your system.

2. Install Required Library

Run the following command:

pip install pandas

3. Run the Program

Execute the Python file using:

python student_system.py


##Default Login Credentials

- Username: admin
- Password: admin123


## Grade Calculation System
Average Marks	Grade
- 90 - 100	A+
- 75 - 89	A
- 60 - 74	B
- Below 60	C


## Developer Information :
Name - Shreya Sunil Palase

Python Developer

Internship project

GitHub : https://github.com/shreyapalase
