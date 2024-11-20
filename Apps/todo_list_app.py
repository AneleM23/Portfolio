import tkinter as tk
from tkinter import messagebox
import json

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Update the listbox
def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        listbox.insert(tk.END, f"{task['description']} [{status}]")

# Add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"description": task, "completed": False})
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty.")

# Mark a task as complete
def mark_complete():
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")

# Delete a task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")

# Exit the app
def exit_app():
    save_tasks()
    root.destroy()

# Main Program
tasks = load_tasks()

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Task entry
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Task listbox
listbox = tk.Listbox(root, width=50, height=15)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Mark complete button
complete_button = tk.Button(root, text="Mark Complete", command=mark_complete)
complete_button.grid(row=2, column=0, padx=10, pady=5)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=5)

# Exit button
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Initialize the task list
update_task_list()

# Run the app
root.mainloop()
