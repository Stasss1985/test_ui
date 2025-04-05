import allure
import pytest
import time
from selenium.webdriver.common.by import By


def test_add_gold_no_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('.ru', '23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    time.sleep(4)
    # Добавление продукта
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_gold()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()


def test_add_gold_qr_no_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('ru', '23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    time.sleep(4)
    # Добавление продукта
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_gold_QR()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()


def test_add_silver_no_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('ru', '23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    time.sleep(4)
    # Добавление продукта
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_silver()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()


def test_add_laptop_no_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('ru', '23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    #time.sleep(4)
    # Добавление продукта
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_laptop()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()


def test_add_car_no_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('ru', '23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_krasnix_partisan()
    lead_page.take_screenshot()
    # Пополнение кассы
    # lead_page.add_cash_in_cash_register(5000)
    # lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    time.sleep(4)
    # Добавление товара
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_car()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()
    time.sleep(5)
