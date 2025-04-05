import allure
import pytest


# @pytest.mark.skip('Не проходит тест из за ГИИС, мы его скипаем')
def test_create_old_lead_gold_cash_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('krivko.su@codeagency.ru', 'DLNKsfd3214$%23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('https://erp-test.karman24.ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    # Выбор клиента из базы
    lead_page.chose_old_client_to_lead()
    lead_page.take_screenshot()
    # Добавление продукта
    product_page.add_product_gold()
    product_page.take_screenshot()
    # Выбор тарифа
    contract_сreate_page.contract_tariff_chose_1()
    contract_сreate_page.take_screenshot()
    # Создание договора
    contract_сreate_page.create_operation_create_contract()
    contract_сreate_page.take_screenshot()
    # Печать документа
    contract_сreate_page.print_document()
    contract_сreate_page.take_screenshot()
    # Печать чека
    contract_сreate_page.print_check()
    contract_сreate_page.take_screenshot()
    # Проверка статуса создания сделки
    contract_сreate_page.compare_text_status()


# @pytest.mark.skip('Не проходит тест из за ГИИС, мы его скипаем')
def test_create_old_lead_silver_cash_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('krivko.su@codeagency.ru', 'DLNKsfd3214$%23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('https://erp-test.karman24.ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    # Выбор клиента из базы
    lead_page.chose_old_client_to_lead()
    lead_page.take_screenshot()
    # Добавление продукта
    product_page.add_product_silver()
    product_page.take_screenshot()
    # Выбор тарифа
    contract_сreate_page.contract_tariff_chose_1()
    contract_сreate_page.take_screenshot()
    # Создание договора
    contract_сreate_page.create_operation_create_contract()
    contract_сreate_page.take_screenshot()
    # Печать документа
    contract_сreate_page.print_document()
    contract_сreate_page.take_screenshot()
    # Печать чека создания "догов потребит займа"
    contract_сreate_page.print_check()
    contract_сreate_page.take_screenshot()
    # Проверка статуса создания сделки (печати чека)
    contract_сreate_page.compare_text_status()
    contract_сreate_page.take_screenshot()


def test_create_old_lead_laptop_cash_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('krivko.su@codeagency.ru', 'DLNKsfd3214$%23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('https://erp-test.karman24.ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    # Выбор клиента из базы
    lead_page.chose_old_client_to_lead()
    lead_page.take_screenshot()
    # Добавление продукта
    product_page.add_product_laptop()
    product_page.take_screenshot()
    # Выбор тарифа
    contract_сreate_page.contract_tariff_chose_2()
    contract_сreate_page.take_screenshot()
    # Создание договора
    contract_сreate_page.create_operation_create_contract()
    contract_сreate_page.take_screenshot()
    # Печать документа
    contract_сreate_page.print_document()
    contract_сreate_page.take_screenshot()
    # Печать чека создания "догов потребит займа"
    contract_сreate_page.print_check()
    contract_сreate_page.take_screenshot()
    # Проверка статуса создания сделки (печати чека)
    contract_сreate_page.compare_text_status()
    contract_сreate_page.take_screenshot()


'''@pytest.mark.skip('еще не готов тест')'''


def test_create_new_client_gold_cash_contract(login_page, lead_page, product_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('krivko.su@codeagency.ru', 'DLNKsfd3214$%23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('https://erp-test.karman24.ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    # Добавление нового клиента
    lead_page.add_new_client_to_lead()
    lead_page.take_screenshot()
    # Добавление продукта
    product_page.add_product_gold()
    product_page.take_screenshot()
    # Выбор тарифа
    contract_сreate_page.contract_tariff_chose_1()
    contract_сreate_page.take_screenshot()
    # Создание договора
    contract_сreate_page.create_operation_create_contract()
    contract_сreate_page.take_screenshot()
    # Печать документа
    contract_сreate_page.print_document()
    contract_сreate_page.take_screenshot()
    # Печать чека
    contract_сreate_page.print_check()
    contract_сreate_page.take_screenshot()
    # Проверка статуса создания сделки
    contract_сreate_page.compare_text_status()
