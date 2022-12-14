import pytest


@pytest.mark.smoke
def test_login(open_login_link, env):
    login_link = open_login_link
    login_link = login_link.login(env.email, env.password)
    assert login_link.is_logout_link_visible() is True



def test_login_empty_pass(open_login_link, env):
    login_link = open_login_link
    login_link = login_link.login_with_empty_password(env.email)
    assert login_link.is_required_password_visible() is True



def test_login_no_creds(open_login_link):
    login_link = open_login_link
    login_link = login_link.login_without_creds()
    assert login_link.is_required_password_visible() and login_link.is_required_email_visible() is True



def test_login_empty_email(open_login_link, env):
    login_link = open_login_link
    login_link = login_link.login_with_empty_email(env.password)
    assert login_link.is_required_email_visible() is True



def test_logout(open_login_link, env):
    login_link = open_login_link
    logout_link = login_link.logout(env.email, env.password)
    assert logout_link.is_logout_link_invisible() is True
