import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def window_size():
    browser.open('https://google.com')


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1920
    browser.config.window_height = 1000

    yield

    browser.quit()


@pytest.fixture(scope='function')
def given_student_registration_form_opened(browser_management):
    browser.config.base_url = 'https://demoqa.com'

    yield



