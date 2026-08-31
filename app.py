import tkinter as tk
from tkinter import messagebox
from task import Task
from storage import save_tasks, load_tasks

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = load_tasks()

        # Input row
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        tk.Button(root, text="Add Task", command=self.add_task).pack()

        # Listbox
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.pack(pady=5)

        # Buttons
        tk.Button(root, text="Mark Done", command=self.mark_done).pack()
        tk.Button(root, text="Delete Task", command=self.delete_task).pack()
        tk.Button(root, text="Clear All", command=self.clear_all).pack()
        tk.Button(root, text="Save", command=self.save).pack(pady=5)

        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            label = f"✓ {task.title}" if task.done else f"○ {task.title}"
            self.listbox.insert(tk.END, label)

    def add_task(self):
        title = self.entry.get()
        if title:
            self.tasks.append(Task(title))
            self.entry.delete(0, tk.END)
            self.refresh()

    def mark_done(self):
        i = self.listbox.curselection()
        if i:
            self.tasks[i[0]].mark_done()
            self.refresh()

    def delete_task(self):
        i = self.listbox.curselection()
        if i:
            self.tasks.pop(i[0])
            self.refresh()

    def clear_all(self):
        self.tasks = []
        self.refresh()

    def save(self):
        save_tasks(self.tasks)
        messagebox.showinfo("Saved", "Tasks saved!")