from hw_13.db.mongoDB.base_db import BaseDb


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


if __name__ == '__main__':
    # Collection().insert_one('QA5', 'Ivan')
    # Collection().insert_one('QA1', 'Yevhen')
    # Collection().insert_one('QA4', 'Roman')
    # Collection().insert_many({'QA2': 'Iryna'}, {'QA3': 'Bogdan'})
    # cursor = list(Collection().find_all())
    # print(cursor)
    # cursor = list(Collection().find_one('QA1', 'Yevhen'))
    # print(cursor)
    # Collection().update_one('Viktor')
    # cursor = list(Collection().find_one('QA5', 'Viktor'))
    # print(cursor)
    # Collection().delete_one('QA1', 'Yevhen')
    # cursor = list(Collection().find_all())
    # print(cursor)
    # Collection().delete_many()
    cursor = list(Collection().find_all())
    print(cursor)
