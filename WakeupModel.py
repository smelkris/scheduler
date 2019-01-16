import json


class WakeupModel:
    def __init__(self, filename):
        self.filename = filename
        self.get_data()
        self._tasklist = None
        self._title = ''

    def get_data(self):
        with open(self.filename, 'r') as f:
            tree = json.load(f)
            self._tasklist = tree["TaskList"]
            self._title = tree["Title"]

    @property
    def tasklist(self):
        return self._tasklist

    @property
    def title(self):
        return self._title
