from selene import be, have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss


def given_opened_form():
    browser.open('/automation-practice-form')
    (
        ss('[id^=google_ads][id$=container__]').with_(timeout=5)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )


def test_fill_form_tools_qa(browser_management):
    if browser.element('google_ads').is_displayed():
        given_opened_form()
    else:
        browser.open('/automation-practice-form')

    # Личные данные
    browser.element('#firstName').should(be.blank).type('Anastasia')
    browser.element('#lastName').should(be.blank).type('Vorobeva')
    browser.element('#userEmail').should(be.blank).type('anastasia.test@gmail.com')
    browser.element('#gender-radio-2+label').click()
    browser.element('#userNumber').should(be.blank).type('9111111111')

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
    browser.element('#currentAddress').type('Moscow')
    browser.element('#state').scroll_to().click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').perform(command.js.click)

    browser.element('.table-responsive').all("table tr")[1].should(have.text('Anastasia Vorobeva'))
    browser.element('.table-responsive').all("table tr")[2].should(have.text('anastasia.test@gmail.com'))
    browser.element('.table-responsive').all("table tr")[3].should(have.text('Female'))
    browser.element('.table-responsive').all("table tr")[4].should(have.text('9111111111'))
    browser.element('.table-responsive').all("table tr")[5].should(have.text('14 August,1997'))
    browser.element('.table-responsive').all("table tr")[6].should(have.text('Maths'))
    browser.element('.table-responsive').all("table tr")[7].should(have.text('Sports'))
    browser.element('.table-responsive').all("table tr")[9].should(have.text('Moscow'))
    browser.element('.table-responsive').all("table tr")[10].should(have.text('Haryana Karnal'))
