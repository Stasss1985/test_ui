import allure
import pytest


@pytest.mark.skip('Для примера тест, мы его скипаем')
@allure.feature('Positive')
def test_login_admin2(login_page):
    login_page.open_page()
    try:
        with allure.step('enter correct login and password'):
            login_page.fill_login_form_good('')
        with allure.step('Check correct url'):
            login_page.check_expected_url()
    except Exception as e:
        login_page.take_screenshot()
        raise e  # Повторно вызываем исключение


@pytest.mark.skip('Для примера тест, мы его скипаем')
@allure.feature('Negative')
def test_login_short_password2(login_page):
    login_page.open_page()
    try:
        login_page.fill_login_form(')
        login_page.check_error_alert_is('Пароль не может быть ')
    except Exception as e:
        login_page.take_screenshot()
        raise e  # Повторно вызываем исключение


@pytest.mark.smoke('smoke test')
@allure.feature('Positive')
def test_login_admin(login_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('')
    with allure.step('Check correct url'):
        login_page.check_expected_url('https://erp-test)
    login_page.take_screenshot()


@allure.feature('Negative')
def test_login_short_password(login_page):
    login_page.open_page()
    login_page.fill_login_form()
    login_page.check_error_alert_is(
        'Пароль не может быть короче 6 символов')


@allure.feature('Negative')
def test_login_incorrect(login_page):
    login_page.open_page()
    login_page.fill_login_form(')
    login_page.check_error_alert_is(
        'Ошибка при авторизации')


@allure.feature('Negative')
def test_login_password_incorrect(login_page):
    login_page.open_page()
    login_page.fill_login_form(')
    login_page.check_error_alert_is(
        'Неверные логин или пароль.')


@allure.feature('Negative')
def test_login_password_end_login_incorrect(login_page):
    login_page.open_page()
    login_page.fill_login_form('')
    login_page.check_error_alert_is(
        'Ошибка при авторизации')


@allure.feature('Negative')
@allure.story('Empty fields')
def test_login_password_end_login_empty(login_page):
    login_page.open_page()
    login_page.fill_login_form('', '')
    login_page.check_error_alert_is(
        'Это обязательное поле')


@allure.feature('Negative')
@allure.story('Empty fields')
def test_login_password_end_login_spase(login_page):
    login_page.open_page()
    login_page.fill_login_form(' ', ' ')
    login_page.check_error_alert_is(
        'Это обязательное поле')

# @pytest.mark.skip('Тесты с параметризацией, не стабилны, пропускаем их')
# @allure.feature('Negative')
# @pytest.mark.parametrize("login, password, expected_error", [
# (, 'Пароль не может быть короче 6 символов'),
# ('', 'Ошибка при авторизации'),
# ('', 'Неверные логин или пароль.'),
# ('', 'Ошибка при авторизации'),
# ('', '', 'Это обязательное поле'),
# (' ', ' ', 'Это обязательное поле')
# ])
# def test_login_password_mark_parametrize(login_page, login, password, expected_error):
# login_page.open_page()
# login_page.fill_login_form(login, password)  # Передаем логин и пароль
# login_page.check_error_alert_is(expected_error)  # Проверяем ожидаемую ошибку
