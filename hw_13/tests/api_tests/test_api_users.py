import json
from http import HTTPStatus
from hw_13.api_collections.users_api import UsersAPI
from hw_13.data_classes.user import User
import pytest


@pytest.mark.regression
def test_post_user():
    response = UsersAPI().create_user()
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.regression
def test_get_all_users():
    response = UsersAPI().get_all_users()
    assert response.status_code == HTTPStatus.OK


@pytest.mark.regression
def test_get_user_by_id():
    response = UsersAPI().get_all_users()
    data = json.loads(response.text)
    id_list = []
    for s in data:
        users_id = s['id']
        id_list.append(users_id)
    user_id = id_list[0]
    response2 = UsersAPI().get_user_by_id(user_id)
    c = 0
    assert response2.status_code == HTTPStatus.OK


@pytest.mark.smoke
def test_user_data(create_user):
    expected_person = create_user
    response = UsersAPI().get_all_users()
    data = json.loads(response.text)
    id_list = []
    for s in data:
        users_id = s['id']
        id_list.append(users_id)
    user_id = id_list[0]
    response2 = UsersAPI().get_user_by_id(user_id)
    user_data = json.loads(response2.text)
    actual_person = User.from_json(**user_data)
    assert actual_person == expected_person


def test_delete_user_by_id():
    response = UsersAPI().get_all_users()
    data = json.loads(response.text)
    id_list = []
    for s in data:
        users_id = s['id']
        id_list.append(users_id)
    user_id = id_list[1]
    response2 = UsersAPI().delete_user_by_id(user_id)
    assert response2.status_code == HTTPStatus.NO_CONTENT
