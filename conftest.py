import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def window_size():
    browser.open('https://google.com').driver.set_window_size(1920, 1080)
    yield
    browser.quit()



