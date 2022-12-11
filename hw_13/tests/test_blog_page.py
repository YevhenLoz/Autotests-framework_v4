import pytest


@pytest.mark.regression
def test_blog_title_visible(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.is_blog_title_visible() is False


@pytest.mark.skip('Skipped test')
def test_post_list_visible(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.is_post_list_visible() is True


@pytest.mark.skip('Skipped test')
def test_side_bar_visible(open_blog_page):
    open_blog = open_blog_page
    open_blog = open_blog.go_to_blog()
    assert open_blog.is_side_bar_visible() is True
