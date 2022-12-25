import pymongo

from hw_13.configurations.config_file import MYCOL, CONNECT_URL


class BaseDb:

    def __init__(self, host: str, port: int, database: str):
        self.host = host
        self.database = database
        self.port = port
        self._client = pymongo.MongoClient(
            f'{self.host}:{self.port}/{CONNECT_URL}'
        )
        self._db = self._client[self.database]
        self._collection = self._db[MYCOL]

    def insert_one(self, key: str, value: str):
        self._collection.insert_one({key: value})

    def insert_many(self, key1: str, value1: str, key2: str, value2: str):
        self._collection.insert_many([{key1: value1}, {key2: value2}])

    def find_all(self):
        result = self._collection.find({})
        return result

    def find_one(self, key: str, value: str):
        result = self._collection.find({key: value})
        return result

    def delete_one(self, key: str, value: str):
        self._collection.delete_one({key: value})

    def delete_many(self):
        self._collection.delete_many({})


