import os

import pytest
from selene import browser, have, be
from selenium import webdriver


@pytest.fixture(scope='function')
def config_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = webdriver.ChromeOptions()
    #browser.config.driver_options.add_argument('--headless=new')
    browser.config.driver_options.add_argument('--window-size=1920,1080')
    browser.config.timeout = 8
    yield
    browser.quit()


def test_registration_form(config_browser):
    browser.open('/automation-practice-form')



    # заполнение полей и проверки
    browser.element('#firstName').should(be.visible).should(be.clickable).type('Иван')
    browser.element('#lastName').should(be.visible).should(be.clickable).type('Иванов')
    browser.element('#userEmail').should(be.visible).should(be.clickable).type('ivanov@example.com')
    browser.all('.custom-radio').should(have.texts('Male', 'Female', 'Other'))
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.visible).should(be.clickable).type('7929100500')
    browser.element('#dateOfBirthInput').should(be.visible).should(be.clickable).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="10"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1986"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--025').click()
    browser.element('#subjectsInput').type('Math').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath('../test_data/test_image.png'))
    browser.element('#currentAddress').should(be.visible).should(be.clickable).type('Moscow, st.Lenina, 23')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').should(be.visible).should(be.clickable).click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    # проверка таблички
    browser.all('.table td').should(have.exact_texts(
        'Student Name', 'Иван Иванов',
        'Student Email', 'ivanov@example.com',
        'Gender', 'Male',
        'Mobile', '7929100500',
        'Date of Birth', '25 November,1986',
        'Subjects', 'Maths',
        'Hobbies', 'Sports',
        'Picture', 'test_image.png',
        'Address', 'Moscow, st.Lenina, 23',
        'State and City', 'NCR Delhi'
    ))






