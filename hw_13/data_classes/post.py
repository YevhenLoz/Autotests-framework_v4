import json


class Post:
    def __init__(self, **kwargs):
        self.title = "Test post" if "title" not in kwargs.keys() else kwargs["title"]
        self.body = "Hello my dear Friends!" if "body" not in kwargs.keys() else kwargs["body"]

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_dict(self):
        return self.__dict__

    def update_dict(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)
