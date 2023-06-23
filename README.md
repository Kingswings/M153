# BuchManager
BuchManager is a Python project for managing tables and customers in a restaurant setting. It provides a command-line interface (CLI) for performing various operations, such as creating books, deleting books, creating autors, and deleting autors.

## Project Structure

The project directory has the following structure:

```
BookManager
├── cli
│   ├── __init__.py
│   ├── input.py
│   └── output.py
├── database
│   ├── __init__.py
│   ├── db.py
│   ├── models.py
│   └── queries.py  
├── venv
├── config.py
├── buchmanager.log
├── logger.py
└── main.py
```

- The `cli` directory contains modules for handling user input and output.
- The `database` directory contains modules for connecting to the database, defining database models, and performing database queries.
- The `logs` directory is used for storing log files.
- The `venv` directory is typically used for creating a virtual environment for the project.
- The `config.py` file contains configuration settings for the database connection.
- The `buchmanager.log` file is the log file for recording application logs.
- The `logger.py` module provides a logger for logging events and messages.
- The `main.py` file is the entry point of the application.

## Dependencies

The project has the following dependencies, which are listed in the `requirements.txt` file:

```
requests
flask
pandas
```

Make sure you have these dependencies installed before running the application. You can install them by running the following command:

```
pip install -r requirements.txt
```