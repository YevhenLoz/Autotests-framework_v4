import pytest


@pytest.mark.smoke
def test_forgot_password_link_present(open_login_link):
    login_link = open_login_link
    login_link = login_link.go_to_login()
    assert login_link.is_forgot_password_present() is True


@pytest.mark.regression
def test_go_to_forgot_password_page(open_login_link):
    login_link = open_login_link
    forgot_password_page = login_link.go_to_forgot_password()
    assert forgot_password_page.is_forgot_password_page_title_visible() is True


def test_forgot_password_confirm(open_login_link, env):
    login_link = open_login_link
    forgot_password_page = login_link.go_to_forgot_password().forgot_password_confirm(env.email)
    assert forgot_password_page.is_success_message_visible() is True


def test_confirm_forgot_password_empty_email(open_login_link):
    login_link = open_login_link
    forgot_password_page = login_link.go_to_forgot_password().forgot_password_confirm_empty_email()
    assert forgot_password_page.is_validation_message_visible() is True


def test_confirm_forgot_password_invalid_email(open_login_link, env):
    login_link = open_login_link
    forgot_password_page = login_link.go_to_forgot_password().forgot_pass_confirm_invalid_email(env.invalid_email)
    assert forgot_password_page.is_validation_email_visible() is True
