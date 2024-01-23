from selene import browser, be, have
import os



def test_registration():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Max')
    browser.element('#lastName').type('Cheshire')
    browser.element('[for="gender-radio-1"]')
    browser.element('#userNumber').type('+71231231212')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="1"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1998"]').click()
    browser.element('.react-datepicker__day--026').click()
    browser.element('..subjects-auto-complete__value-container').click()



