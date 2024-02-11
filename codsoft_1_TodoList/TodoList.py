import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks.curselection()
    if selected_task_index:
        tasks.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def update_task():
    selected_task_index = tasks.curselection()
    updated_task = entry.get()

    if selected_task_index and updated_task:
        tasks.delete(selected_task_index)
        tasks.insert(selected_task_index, updated_task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task to update and enter a new task.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.resizable(False,False)
root.config(bg='black')

font_style = ("Comic Sans MS",20,"bold")

# Create and pack widgets
tasks = tk.Listbox(root, selectmode=tk.SINGLE, bg="#24586a",fg="#ffffff", width=40, height=10,font=font_style)
tasks.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=tasks.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=30,font=font_style)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#b1a13c",fg="#ffffff",font=font_style)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#723cb1",fg="#ffffff",font=font_style)
remove_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task, bg="#b15b3c",fg="#ffffff",font=font_style)
update_button.pack()

# Start the Tkinter event loop
root.mainloop()
