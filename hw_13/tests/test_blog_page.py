import pytest


@pytest.mark.regression
def test_blog_is_opened(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.is_blog_title_visible() is True


@pytest.mark.regression
def test_blog_is_opened(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.is_post_list_visible() is True


@pytest.mark.regression
def test_blog_is_opened(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.is_side_bar_visible() is True