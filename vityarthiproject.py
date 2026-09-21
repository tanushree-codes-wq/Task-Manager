import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load the tasks list from the file, or start empty if it doesn't exist yet."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Write the tasks list back to the file so nothing is lost."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    """Ask the user for task details and add the new task to the list."""
    description = input("Enter task description: ")
    priority = input("Enter priority (High/Medium/Low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    new_task = {
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def print_task_list(tasks):
    """Shared helper: print a given list of tasks in numbered, readable form."""
    if not tasks:
        print("No tasks to show.\n")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['description']} | Priority: {task['priority']} "
              f"| Due: {task['due_date']} | Status: {status}")
    print()


def view_tasks(tasks):
    """Print every task in a numbered, readable list."""
    print_task_list(tasks)


def update_task(tasks):
    """Let the user mark a task complete or edit its details."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to update: "))
        task = tasks[task_num - 1]
    except (ValueError, IndexError):
        print("Invalid task number.\n")
        return

    print("1. Mark as complete")
    print("2. Edit description/priority/due date")
    choice = input("Choose an option: ")

    if choice == "1":
        task["completed"] = True
        print("Task marked as complete!\n")
    elif choice == "2":
        task["description"] = input("New description: ")
        task["priority"] = input("New priority (High/Medium/Low): ")
        task["due_date"] = input("New due date (YYYY-MM-DD): ")
        print("Task updated!\n")
    else:
        print("Invalid choice.\n")
        return

    save_tasks(tasks)


def delete_task(tasks):
    """Let the user remove a task from the list entirely."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['description']}\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def reports_menu(tasks):
    """Let the user filter or sort tasks in a few useful ways."""
    if not tasks:
        print("No tasks yet.\n")
        return

    print("--- Reports ---")
    print("1. Show pending tasks only")
    print("2. Show completed tasks only")
    print("3. Filter by priority")
    print("4. Sort by due date")
    print("5. Summary counts")
    choice = input("Choose an option: ")

    if choice == "1":
        pending = [t for t in tasks if not t["completed"]]
        print_task_list(pending)
    elif choice == "2":
        completed = [t for t in tasks if t["completed"]]
        print_task_list(completed)
    elif choice == "3":
        priority = input("Enter priority to filter by (High/Medium/Low): ")
        filtered = [t for t in tasks if t["priority"].lower() == priority.lower()]
        print_task_list(filtered)
    elif choice == "4":
        sorted_tasks = sorted(tasks, key=lambda t: t["due_date"])
        print_task_list(sorted_tasks)
    elif choice == "5":
        total = len(tasks)
        completed_count = len([t for t in tasks if t["completed"]])
        pending_count = total - completed_count
        print(f"Total tasks: {total}")
        print(f"Completed: {completed_count}")
        print(f"Pending: {pending_count}\n")
    else:
        print("Invalid choice.\n")


def main():
    tasks = load_tasks()

    while True:
        print("--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Reports / filters")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            reports_menu(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
