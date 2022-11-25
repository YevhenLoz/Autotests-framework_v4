import pytest

from hw_13.utilities.read_configs import ReadConfig


# login tests
@pytest.mark.smoke
def test_login(open_login_link):
    login_link = open_login_link
    login_link = login_link.login(ReadConfig.get_email(), ReadConfig.get_password())
    assert login_link.is_visible() is True


@pytest.mark.smoke
def test_login_empty_pass(open_login_link):
    login_link = open_login_link
    login_link = login_link.login_with_empty_password(ReadConfig.get_email())
    assert login_link.required_password_visible() is True


@pytest.mark.smoke
def test_login_no_creds(open_login_link):
    login_link = open_login_link
    login_link = login_link.login_without_creds()
    assert login_link.required_password_visible() and login_link.required_email_visible() is True


@pytest.mark.smoke
def test_login_empty_email(open_login_link):
    login_link = open_login_link
    login_link = login_link.login_with_empty_email(ReadConfig.get_password())
    assert login_link.required_email_visible() is True


@pytest.mark.smoke
def test_logout(open_login_link):
    login_link = open_login_link
    logout_link = login_link.logout(ReadConfig.get_email(), ReadConfig.get_password())
    assert logout_link.is_invisible() is True


# account page tests
@pytest.mark.regression
def test_edit_contact_info_visible(open_login_link):
    login_link = open_login_link
    account_page = login_link.account(ReadConfig.get_email(), ReadConfig.get_password())
    assert account_page.contact_edit_visible() is True


@pytest.mark.regression
def test_welcome_message_visible(open_login_link):
    login_link = open_login_link
    account_page = login_link.account(ReadConfig.get_email(), ReadConfig.get_password())
    assert account_page.welcome_message_visible() is True


@pytest.mark.regression
def test_edit_account_title_visible(open_login_link):
    login_link = open_login_link
    account_page = login_link.account(ReadConfig.get_email(), ReadConfig.get_password()).edit_account()
    assert account_page.edit_account_title_visible() is True


@pytest.mark.regression
def test_edit_address_page_opened(open_login_link):
    login_link = open_login_link
    account_page = login_link.account(ReadConfig.get_email(), ReadConfig.get_password()).edit_account()
    assert account_page.edit_account_title_visible() is True


@pytest.mark.regression
def test_edit_account_title_visible(open_login_link):
    login_link = open_login_link
    account_page = login_link.account(ReadConfig.get_email(), ReadConfig.get_password()).edit_account()
    assert account_page.edit_account_title_visible() is True


# create account page tests
@pytest.mark.regression
def test_go_to_create_account_page(open_login_link):
    login_link = open_login_link
    create_account_page = login_link.go_to_create_account()
    assert create_account_page.create_account_title_visible() is True


@pytest.mark.regression
def test_back_to_login_page(open_login_link):
    login_link = open_login_link
    create_account_page = login_link.go_to_create_account().go_back_to_login()
    assert create_account_page.login_page_title_visible() is True


@pytest.mark.regression
def test_name_required(open_login_link):
    login_link = open_login_link
    create_account_page = login_link.go_to_create_account().submit_without_name()
    assert create_account_page.name_required() is True


@pytest.mark.regression
def test_name_field_visible(open_login_link):
    login_link = open_login_link
    create_account_page = login_link.go_to_create_account()
    assert create_account_page.name_field_visible() is True


# forgot password tests
@pytest.mark.smoke
def test_forgot_password_link_present(open_login_link):
    login_link = open_login_link
    login_link = login_link.go_to_login()
    assert login_link.forgot_password_is_present() is True


@pytest.mark.regression
def test_go_to_forgot_password_page(open_login_link):
    login_link = open_login_link
    forgot_password_page = login_link.go_to_forgot_password()
    assert forgot_password_page.forgot_password_page_title_visible() is True


@pytest.mark.regression
def test_forgot_password_confirm(open_login_link):
    login_link = open_login_link
    forgot_password_page = login_link.go_to_forgot_password().forgot_password_confirm(ReadConfig.get_email())
    assert forgot_password_page.success_message_visible() is True


@pytest.mark.smoke
def test_confirm_forgot_password_empty_email(open_login_link):
    login_link = open_login_link
    forgot_password_page = login_link.go_to_forgot_password().forgot_password_confirm_empty_email()
    assert forgot_password_page.validation_message_visible() is True


@pytest.mark.smoke
def test_confirm_forgot_password_invalid_email(open_login_link):
    login_link = open_login_link
    forgot_password_page = login_link.go_to_forgot_password().forgot_pass_confirm_invalid_email(
        ReadConfig.get_invalid_email())
    assert forgot_password_page.validation_email_visible() is True


# blog page tests
@pytest.mark.regression
def test_blog_is_opened(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.blog_title_is_visible() is True


@pytest.mark.regression
def test_blog_is_opened(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.post_list_is_visible() is True


@pytest.mark.regression
def test_blog_is_opened(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.side_bar_is_visible() is True
