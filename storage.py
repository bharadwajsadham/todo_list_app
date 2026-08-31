import json
from task import Task

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump([t.to_dict() for t in tasks], f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            tasks = []
            for item in data:
                t = Task(item["title"])
                t.done = item["done"]
                tasks.append(t)
            return tasks
    except FileNotFoundError:
        return []