# Problem Statement

Students and individuals often forget tasks or struggle to prioritize 
their day correctly when managing to-dos mentally or on paper. There 
is no simple, distraction-free way to record a task once and reliably 
track its status, priority, and deadline over time without relying on 
a paid or overly complex tool. This project addresses that gap with a 
lightweight, command-line To-Do List Manager built in Python.

# Scope

The project covers three core operations: adding new tasks, managing 
existing tasks (viewing, updating, marking complete, and deleting), 
and generating simple reports or filtered views of the task list 
(pending only, completed only, by priority, sorted by due date, and 
summary counts). It is a console-based application with task data 
stored in a local JSON file, so tasks persist between runs. It does 
not cover reminders/notifications, a graphical interface, or 
multi-user accounts.

# Target Users

- Students managing assignments and deadlines
- Anyone who wants a lightweight, no-frills task tracker without 
  installing complex software

# High-Level Features

- Add a new task with description, priority (High/Medium/Low), and due date
- View all tasks in a numbered, readable list
- Mark a task as complete
- Update or delete an existing task
- Filter tasks by status (pending/completed) or priority
- View tasks sorted by due date
- View summary counts of total, completed, and pending tasks
- Data is saved automatically to a file so tasks persist after closing
