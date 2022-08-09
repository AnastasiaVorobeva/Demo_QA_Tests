from selene.support.shared import browser
from selene import be, have


def test_positive_result(window_size):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_negative_result(window_size):
    browser.element('[name="q"]').type('fgiauldjnms').press_enter()
    browser.element('#res').should(have.text('ничего не найдено'))
