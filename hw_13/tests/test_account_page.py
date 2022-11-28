import pytest


@pytest.mark.regression
def test_edit_contact_info_visible(open_login_link, env):
    login_link = open_login_link
    email = env.email
    password = env.password
    account_page = login_link.account(email, password)
    assert account_page.is_contact_edit_visible() is True


@pytest.mark.regression
def test_welcome_message_visible(open_login_link, env):
    login_link = open_login_link
    email = env.email
    password = env.password
    account_page = login_link.account(email, password)
    assert account_page.is_welcome_message_visible() is True


@pytest.mark.regression
def test_edit_account_title_visible(open_login_link, env):
    login_link = open_login_link
    email = env.email
    password = env.password
    account_page = login_link.account(email, password).edit_account()
    assert account_page.is_edit_account_title_visible() is True


@pytest.mark.regression
def test_edit_address_page_opened(open_login_link, env):
    login_link = open_login_link
    email = env.email
    password = env.password
    account_page = login_link.account(email, password).edit_account()
    assert account_page.is_edit_address_title_visible() is True


@pytest.mark.regression
def test_edit_account_title_visible(open_login_link, env):
    login_link = open_login_link
    email = env.email
    password = env.password
    account_page = login_link.account(email, password).edit_account()
    assert account_page.is_edit_account_title_visible() is True
