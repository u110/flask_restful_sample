"""
"""

class TodoDao(object):

    __instance = None

    @classmethod
    def get(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self):
        self.todos = {
            "1": "開発",
            "2": "flask-restfulためし"
        }
