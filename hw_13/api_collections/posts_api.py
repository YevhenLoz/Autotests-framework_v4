from hw_13.data_classes.post import Post
from hw_13.utilities.api.BaseAPI import BaseAPI


class PostAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = '/public/v2/users/3/posts'

    def get_user_posts(self, headers=None):
        return self.get(f'{self.__url}', headers=headers)

    def create_post(self, body=None):
        post_data = Post()
        if body is not None:
            post_data.update_dict(**body)
        return self.post(self.__url, body=post_data.get_json())


