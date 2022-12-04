import json
from http import HTTPStatus
from hw_13.api_collections.users_api import UsersAPI
from hw_13.data_classes.user import User
import pytest


def test_post_user():
    response = UsersAPI().create_user()
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_get_use_by_id():
    response = UsersAPI().get_user_by_id(6562)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.skip('Skipped test')
def test_person_data(create_user):
    expected_user = create_user
    response = UsersAPI().get_user_by_id(6580)  # add id of newly created user manually
    user_data = json.loads(response.text)
    actual_user = User.from_json(**user_data)
    assert actual_user == expected_user


@pytest.mark.skip('Skipped test')
def test_delete_user_by_id():
    response = UsersAPI().delete_user_by_id(6546)
    assert response.status_code == HTTPStatus.NO_CONTENT
