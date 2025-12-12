import time

import pytest
from selene import browser, be, have, by

browser.open('https://ya.ru')
browser.element('[name="text"]').should(be.blank).type('qa.guru').press_enter()

time.sleep(1)

if browser.element('[title="Нет, спасибо"]').matching(be.visible):
    browser.element('[title="Нет, спасибо"]').click()

time.sleep(1)

browser.element('html').should(have.text('Курсы тестировщиков - обучение... | '))

# browser.element('[id="search"]').should(have.text('QA.GURU: Курсы тестировщиков'))
