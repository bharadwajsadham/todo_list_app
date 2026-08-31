class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {"title": self.title, "done": self.done}

    def from_dict(self, data):
        self.title = data["title"]
        self.done = data["done"]