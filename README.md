# To-Do List App

A simple desktop To-Do List application built using Python and Tkinter.

This is my first Python project. I created this project while learning Python and wanted to build something simple that I could actually use. The application provides a basic graphical interface where tasks can be added, completed, deleted, and cleared. The tasks are also stored in a JSON file so that they can be loaded again when the application is opened.

## Features

- Add new tasks
- Mark selected tasks as completed
- Delete selected tasks
- Clear all tasks
- Save tasks to a JSON file
- Load saved tasks when the application starts
- Simple desktop graphical interface

## Technologies Used

- Python
- Tkinter
- JSON

## Project Structure

    todo_list_app/
    │
    ├── main.py       # Starts the application
    ├── app.py        # Main GUI and application logic
    ├── task.py       # Handles the Task class
    ├── storage.py    # Handles saving and loading tasks
    ├── tasks.json    # Stores task data
    └── README.md     # Project documentation

## How It Works

The application starts from `main.py`, which launches the Tkinter application.

The main interface and user actions are handled in `app.py`. Tasks are represented using the `Task` class in `task.py`. The `storage.py` file is responsible for saving and loading the task information, while `tasks.json` is used to store the saved tasks.

This structure keeps different parts of the application separated instead of putting everything into one Python file.

## How to Run

### Requirements

- Python 3.x
- Tkinter

Tkinter is normally included with a standard Python installation.

### Steps

1. Clone this repository:

       git clone https://github.com/bharadwajsadham/todo_list_app.git

2. Open the project folder:

       cd todo_list_app

3. Run the application:

       python main.py

The To-Do List window will open and the application is ready to use.

## What I Learned

This project helped me understand the basics of building a Python desktop application. While working on it, I learned about:

- Python classes and objects
- Tkinter and GUI development
- Buttons, input fields, and list-based interfaces
- Handling user actions
- Reading and writing JSON files
- Organizing a project into multiple Python files
- Using Git and GitHub for version control

## Future Improvements

I would like to continue improving this project as I learn more. Some features I may add in the future include:

- Editing existing tasks
- Adding task priorities
- Adding due dates
- Searching and filtering tasks
- Adding task categories
- Improving the user interface
- Adding better input validation
- Adding more options for managing tasks

## Project Status

This project is currently a simple beginner-level To-Do List application. It was created mainly as a learning project and as my first step into building and publishing a Python application.

## Author

Bharadwaj Sadham

This is my first Python project, and I plan to keep improving my programming skills by building more projects.

## License

This project is available for learning and personal use.