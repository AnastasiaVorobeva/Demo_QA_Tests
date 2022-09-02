import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def window_size():
    browser.open('https://google.com').driver.set_window_size(1920, 1080)
    yield
    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = 'chorme'
    browser.config.base_url = 'https://demoqa.com'


