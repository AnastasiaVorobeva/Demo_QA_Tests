from selene import have, be
from selene.support.shared import browser


def test_web_tables(given_student_registration_form_opened):
    # ACT
    browser.open('/webtables')
    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Anastasia')
    browser.element('#lastName').type('Vorobeva')
    browser.element('#userEmail').type('anastasia.test@gmail.com')
    browser.element('#age').type('25')
    browser.element('#salary').type('10')
    browser.element('#department').type('RnD')
    browser.element('#submit').click()

    # Assert
    browser.element('.rt-table').should(have.text('Anastasia'))
    browser.element('.rt-table').should(have.text('Vorobeva'))
    browser.element('.rt-table').should(have.text('25'))
    browser.element('.rt-table').should(have.text('anastasia.test@gmail.com'))
    browser.element('.rt-table').should(have.text('10'))
    browser.element('.rt-table').should(have.text('RnD'))

    # Update row
    browser.element('#edit-record-1').click()
    browser.element('#firstName').clear().type('Stacy')
    browser.element('#age').clear().type('20')
    browser.element('#submit').click()

    # Assert
    browser.element('.rt-table').should(have.text('Stacy'))
    browser.element('.rt-table').should(have.text('Vorobeva'))
    browser.element('.rt-table').should(have.text('20'))
    browser.element('.rt-table').should(have.text('anastasia.test@gmail.com'))
    browser.element('.rt-table').should(have.text('10'))
    browser.element('.rt-table').should(have.text('RnD'))

    # Delete row
    browser.element('#delete-record-3').click()






