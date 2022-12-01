import json


class User:
    def __init__(self, **kwargs):
        self.name = "John Left" if "name" not in kwargs.keys() else kwargs["name"]
        self.email = "oko@gmail.com" if "email" not in kwargs.keys() else kwargs["email"]
        self.gender = "male" if "gender" not in kwargs.keys() else kwargs["gender"]
        self.status = "active" if "status" not in kwargs.keys() else kwargs["status"]

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
