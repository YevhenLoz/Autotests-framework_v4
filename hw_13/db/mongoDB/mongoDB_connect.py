import pymongo

from hw_13.configurations.config_file import MYCOL


class BaseDb:

    def __init__(self, host: str, port: int, database: str):
        self.host = host
        self.database = database
        self.port = port
        self._client = pymongo.MongoClient(
            f'{self.host}:{self.port}/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1'
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


class Collection(BaseDb):
    def __init__(self):
        super().__init__(host='mongodb://127.0.0.1',
                         port=27017,
                         database='qa_team2'
                         )

    def update_one(self, new_name):
        update = {'QA5': 'Ivan'}
        query = {'$set': {'QA5': f'{new_name}'}}
        self._collection.update_one(update, query)


Collection().insert_one('QA5', 'Ivan')
Collection().insert_one('QA1', 'Yevhen')
Collection().insert_one('QA4', 'Roman')
Collection().insert_many('QA2', 'Iryna', 'QA3', 'Bogdan')
cursor = list(Collection().find_all())
print(cursor)
cursor = list(Collection().find_one('QA1', 'Yevhen'))
print(cursor)
Collection().update_one('Viktor')
cursor = list(Collection().find_one('QA5', 'Viktor'))
print(cursor)
Collection().delete_one('QA1', 'Yevhen')
cursor = list(Collection().find_all())
print(cursor)
Collection().delete_many()
cursor = list(Collection().find_all())
print(cursor)
