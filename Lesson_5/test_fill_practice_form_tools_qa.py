from selene import be
from selene.support.shared import browser


def test_fill_form_tools_qa(browser_management):
    # Переход на страницу
    browser.open('/automation-practice-form')

    # Личные данные
    browser.element('#firstName').should(be.blank).type('Anastasia')
    browser.element('#lastName').should(be.blank).type('Vorobeva')
    browser.element('#userEmail').should(be.blank).type('anastasia.ev97@gmail.com')
    browser.element('#gender-radio-2+label').click()

    # Выбор даты рождения
    browser.element('[class="react-datepicker__input-container"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1997"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="7"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--014"]').click()

    # Дополнительная информация
    browser.element('#subjectsInput').type('maths').press_enter()
    browser.element('#hobbies-checkbox-1+label').click()
    browser.element('#currentAddress').type('Moscow, Obrazcova st, 4')
    browser.element('#state').scroll_to().click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    # Ввод номера телфона и отпрака формы
    browser.element('#userNumber').should(be.blank).type('9277548529').press_enter()



