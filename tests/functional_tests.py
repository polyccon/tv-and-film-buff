import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    return webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture
def setup_and_teardown(browser):
    browser.get("http://localhost:8000")
    yield
    browser.quit()


def test_text_in_browser_title(browser, setup_and_teardown):
    assert "Congratulations" in browser.title
