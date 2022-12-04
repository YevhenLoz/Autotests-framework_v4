from hw_13.data_classes.user import User
from hw_13.utilities.api.BaseAPI import BaseAPI
import allure


class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = '/public/v2/users'

    @allure.step
    def get_user_by_id(self, user_id, headers=None):
        return self.get(f'{self.__url}/{user_id}', headers=headers)

    @allure.step
    def create_user(self, body=None):
        user_data = User()
        if body is not None:
            user_data.update_dict(**body)
        return self.post(self.__url, body=user_data.get_json())

    @allure.step
    def delete_user_by_id(self, user_id, headers=None):
        return self.delete(f'{self.__url}/{user_id}', headers=headers)

