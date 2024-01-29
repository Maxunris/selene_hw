import time
from selene import browser, be, have
import os
from selenium import webdriver

def test_registration():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"

    browser.config.driver_options = driver_options
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Max')
    browser.element('#lastName').type('Cheshire')
    browser.element('#userEmail').type('Maxcheshire1@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('7999123121')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="1"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1998"]').click()
    browser.element('.react-datepicker__day--026').click()
    browser.element('#subjectsInput').type('Ma').press_enter()
    browser.element('label[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/123.jpeg'))
    browser.element('#currentAddress').type('Pushkina-kolotushkina, Moscow, Russia')
    browser.element('#react-select-3-input').type('Utt').press_enter()
    browser.element('#react-select-4-input').type('Lu').press_enter()
    browser.element('#submit').execute_script('element.click()')
    browser.element('.table').all('td').even.should(have.texts(
    'Max Cheshire',
    'Maxcheshire1@gmail.com',
    'Male',
    '7999123121',
    '26 March,1998',
    'Maths',
    'Reading',
    '123.jpeg',
    'Pushkina-kolotushkina, Moscow, Russia',
    'Uttar Pradesh Lucknow'))

