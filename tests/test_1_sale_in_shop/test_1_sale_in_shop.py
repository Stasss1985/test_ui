import allure
import pytest


#@pytest.mark.repeat(3) запустит тест 3 раза
def test_01_sale_in_shop_product(login_page, lead_page, shop_sale_page, contract_сreate_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('krivko.su@codeagency.ru', 'DLNKsfd3214$%23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('https://erp-test.karman24.ru/')
    login_page.take_screenshot()
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход в магазин
    shop_sale_page.navigate_to_shop_page()
    shop_sale_page.take_screenshot()
    # Открытие фильтра справа и сортировка для продажи товаров (не ЮИ)
    shop_sale_page.filter_for_sale_product_in_shop()
    # Продажа товара из магазина (не ЮИ)
    shop_sale_page.sale_product_in_shop()
    # Печать документа
    contract_сreate_page.print_document()
    contract_сreate_page.take_screenshot()
    # Печать чека создания "догов потребит займа"
    contract_сreate_page.print_check()
    contract_сreate_page.take_screenshot()
    # Проверка статуса продажи товара (печати чека)
    contract_сreate_page.compare_text_status()
    contract_сreate_page.take_screenshot()
    # Переход в карточку товара из печати чека
    shop_sale_page.xref_go_to_product_id()
    shop_sale_page.take_screenshot()
    # Проверка статуса "Нет в наличии" в карточке товара
    shop_sale_page.compare_product_status_out_of_stock()
    shop_sale_page.take_screenshot()
    # Проверка состояния "Продан" в карточке товара
    shop_sale_page.compare_product_condition_sold()
    shop_sale_page.take_screenshot()
