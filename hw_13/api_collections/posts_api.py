import json

from hw_13.data_classes.post import Post
from hw_13.utilities.api.BaseAPI import BaseAPI
import allure


class PostAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = '/public/v2/posts'
        self.__url2 = '/public/v2/users/141/posts'

    @allure.step
    def get_user_posts(self, headers=None):
        return self.get(f'{self.__url}', headers=headers)

    @allure.step
    def create_post(self, body=None):
        post_data = Post()
        if body is not None:
            post_data.update_dict(**body)
        return self.post(self.__url2, body=post_data.get_json())

    @allure.step
    def get_post_by_id(self, user_id, headers=None):
        return self.get(f'{self.__url}/{user_id}', headers=headers)
