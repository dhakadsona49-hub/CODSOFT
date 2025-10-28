import tkinter as tk
from tkinter import messagebox

# Add Task Function
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Delete Task Function
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Update Task Function
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        updated_task = task_entry.get()
        if updated_task != "":
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated task!")
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x400")
root.config(bg="#dfe6e9")

# Heading
heading = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#dfe6e9")
heading.pack(pady=10)

# Task Entry Field
task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
update_btn = tk.Button(btn_frame, text="Update Task", width=12, command=update_task)
delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)

add_btn.grid(row=0, column=0, padx=5)
update_btn.grid(row=0, column=1, padx=5)
delete_btn.grid(row=0, column=2, padx=5)

# Listbox to show tasks
task_listbox = tk.Listbox(root, width=50, height=12, font=("Arial", 12))
task_listbox.pack(pady=10)

# Main Loop
root.mainloop()
