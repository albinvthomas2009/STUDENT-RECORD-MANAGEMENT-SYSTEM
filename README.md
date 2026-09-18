# Student Record Management System

A Python-based **Student Record Management System** that uses **MySQL** to store and manage student and faculty information.

## Project Overview

This project provides a menu-driven command-line application for managing school records. It connects to a local MySQL database named `school` and provides options for adding, finding, sorting, updating, and deleting student and faculty records.

> **Current status:** The project is approximately 90% complete. The delete-record functionality is currently unfinished and is planned for a later update.

## Features

### Student Records
- Add student details
- Find students by admission number
- Find students by name
- Sort/filter students by class
- Sort/filter students by section
- Sort/filter students by stream
- Update student name
- Update student class
- Update student section
- Update student date of birth
- Delete student details *(planned)*

### Faculty Records
- Add faculty details
- Find faculty by ID
- Find faculty by name
- Find faculty by subject
- Update faculty name
- Update faculty subject
- Delete faculty details *(planned)*

### Authentication
The application includes a login system before accessing the record-management menu.

## Technologies Used

- **Python**
- **MySQL**
- **MySQL Connector/Python**

## Requirements

- Python 3.x
- MySQL Server
- A MySQL database named `school`
- The required database tables used by the program
- `mysql-connector-python`

Install the Python dependency with:

```bash
pip install -r requirements.txt
```

## Database Configuration

The program currently connects to a local MySQL server using:

- Host: `localhost`
- Database: `school`

The MySQL database should contain the tables expected by the program, including:

- `STUDENTS`
- `FACULTY`
- `STREAM`

Make sure your MySQL server is running before starting the program.

## Running the Project

1. Install Python 3.x.
2. Install MySQL Server.
3. Create/configure the `school` database and required tables.
4. Install the Python dependency:

```bash
pip install -r requirements.txt
```

5. Run the program:

```bash
python project.py
```

## Project Structure

```text
Student-Record-Management-System/
│
├── project.py
├── README.md
└── requirements.txt
```

## Future Improvements

Planned improvements include:

- Complete student deletion functionality
- Complete faculty deletion functionality
- Improve input validation
- Improve database query safety
- Improve error handling
- Separate database configuration from application code
- Improve the user interface
- Add more record-management features

## Note

This project is intended as an educational/student project demonstrating Python programming and MySQL database connectivity.
