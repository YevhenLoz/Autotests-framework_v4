import pytest


@pytest.mark.regression
def test_go_to_create_account_page(open_login_link):
    login_link = open_login_link
    create_account_page = login_link.go_to_create_account()
    assert create_account_page.is_create_account_title_visible() is True


@pytest.mark.skip('Skipped test')
def test_back_to_login_page(open_login_link):
    login_link = open_login_link
    create_account_page = login_link.go_to_create_account().go_back_to_login()
    assert create_account_page.is_login_page_title_visible() is True


@pytest.mark.skip('Skipped test')
def test_name_required(open_login_link):
    login_link = open_login_link
    create_account_page = login_link.go_to_create_account().submit_without_name()
    assert create_account_page.is_name_required_visible() is True


@pytest.mark.skip('Skipped test')
def test_name_field_visible(open_login_link):
    login_link = open_login_link
    create_account_page = login_link.go_to_create_account()
    assert create_account_page.is_name_field_visible() is True
