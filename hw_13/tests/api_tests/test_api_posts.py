from http import HTTPStatus
from hw_13.api_collections.posts_api import PostAPI
import json

from hw_13.data_classes.post import Post
import pytest


@pytest.mark.regression
def test_create_post():
    response = PostAPI().create_post()
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.regression
def test_get_posts():
    response = PostAPI().get_user_posts()
    assert response.status_code == HTTPStatus.OK


@pytest.mark.smoke
def test_get_post_by_id():
    response = PostAPI().get_user_posts()
    data = json.loads(response.text)
    id_list = []
    for s in data:
        users_id = s['id']
        id_list.append(users_id)
    user_id = id_list[0]
    response2 = PostAPI().get_post_by_id(user_id)
    assert response2.status_code == HTTPStatus.OK


@pytest.mark.smoke
def test_posts_data(create_post):
    expected_post = create_post
    response = PostAPI().get_user_posts()
    data = json.loads(response.text)
    id_list = []
    for s in data:
        users_id = s['id']
        id_list.append(users_id)
    user_id = id_list[0]
    response2 = PostAPI().get_post_by_id(user_id)
    user_data = json.loads(response2.text)
    actual_post = Post.from_json(**user_data)
    assert actual_post == expected_post
