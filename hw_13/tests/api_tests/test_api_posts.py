import json
from http import HTTPStatus
from hw_13.api_collections.posts_api import PostAPI


def test_create_post():
    response = PostAPI().create_post()
    assert response.status_code == HTTPStatus.CREATED


def test_get_posts():
    response = PostAPI().get_user_posts()
    assert response.status_code == HTTPStatus.OK





