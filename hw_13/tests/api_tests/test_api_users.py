import json
from http import HTTPStatus

from hw_13.api_collections.users_api import UsersAPI
from hw_13.data_classes.user import User


def test_post_user():
    response = UsersAPI().create_user()
    assert response.status_code == HTTPStatus.CREATED


def test_get_use_by_id():
    response = UsersAPI().get_user_by_id(4817)
    assert response.status_code == HTTPStatus.OK


def test_person_data(create_person):
    expected_person = create_person
    response = UsersAPI().get_user_by_id(4817)
    user_data = json.loads(response.text)
    actual_person = User.from_json(**user_data)
    assert actual_person == expected_person


def test_delete_user_by_id():
    response = UsersAPI().delete_user_by_id(4817)
    assert response.status_code == HTTPStatus.NO_CONTENT
