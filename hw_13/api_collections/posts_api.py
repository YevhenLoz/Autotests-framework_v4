from hw_13.utilities.api.BaseAPI import BaseAPI
import allure


class PostAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = '/public/v2/users/3/posts'

    @allure.step
    def get_user_posts(self, headers=None):
        return self.get(f'{self.__url}', headers=headers)




