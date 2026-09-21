
# To-Do List Manager

## Overview

To-Do List Manager is a command-line Python application that helps 
users add, organize, and track their daily tasks. Each task has a 
description, priority level, and due date, and can be marked complete, 
edited, or deleted. Tasks are automatically saved to a local file, so 
nothing is lost between runs of the program. The project was built for 
the Introduction to Programming and Solving course to apply core 
programming concepts — functions, conditionals, loops, dictionaries, 
and file handling — in a complete, usable application.

## Features

- Add a new task with a description, priority (High/Medium/Low), and due date
- View all tasks in a numbered, readable list showing status
- Mark a task as complete
- Update a task's description, priority, or due date
- Delete a task
- Filter tasks by status (pending/completed only)
- Filter tasks by priority
- Sort tasks by due date
- View summary counts (total, completed, pending)
- All data is saved automatically to a local JSON file

## Technologies / Tools Used

- Python 3
- Built-in `json` module (for saving/loading task data)
- Built-in `os` module (for checking if the data file exists)
- Git & GitHub (for version control and submission)

## Steps to Install & Run

1. Make sure Python 3 is installed on your computer. Check by running:

python --version

2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the program:

python main.py

5. Use the on-screen numbered menu to add, view, update, delete, or 
   filter your tasks.

## Instructions for Testing

1. Run `python main.py`.
2. Choose option `1` to add a few tasks with different priorities and 
   due dates.
3. Choose option `2` to confirm the tasks appear correctly in the list.
4. Choose option `3` to mark a task complete or edit one, then view 
   the list again to confirm the change was saved.
5. Choose option `4` to delete a task, then view the list again to 
   confirm it's gone.
6. Choose option `5` to try each report/filter (pending only, 
   completed only, by priority, sorted by due date, summary counts).
7. Close the program and re-run it — confirm your previously added 
   tasks are still there (loaded from `tasks.json`).
8. Try an invalid input (e.g. a letter instead of a task number) to 
   confirm the program shows an error message instead of crashing.
   ## Screenshots
   <img width="1920" height="1080" alt="Screenshot (118)" src="https://github.com/user-attachments/assets/9365e10a-ba87-4af3-a1a6-614e83e8e6be" />
