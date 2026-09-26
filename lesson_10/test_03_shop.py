import allure
import pytest
from selenium import webdriver
from shop_page import ShopPage, CartPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Оформление заказа в интернет‑магазине")
@allure.title("Проверка оформления заказа и итоговой суммы")
@allure.description(
    "Тест проверяет авторизацию, добавление товара в корзину, "
    "прохождение чекаута и корректность итоговой суммы заказа"
)
@allure.severity("critical")
def test_shop(driver):
    shop_page = ShopPage(driver, "https://www.saucedemo.com/")

    with allure.step("Открыть страницу магазина и авторизоваться"):
        shop_page.open()
        shop_page.authorization()

    with allure.step("Добавить товар в корзину"):
        shop_page.get_add_product()

    cart_page = CartPage(driver)

    with allure.step("Проверить содержимое корзины "
                     "и начать оформление заказа"):
        cart_page.get_shopping_card()
        cart_page.get_checkout()

    with allure.step("Заполнить форму данных покупателя "
                     "и продолжить оформление"):
        cart_page.get_form()
        cart_page.get_continue()

    total = cart_page.get_total()
    result = cart_page.get_result()

    allure.attach(
        f"Total: {total}, Result: {result}",
        name="Фактические значения",
        attachment_type=allure.attachment_type.TEXT
    )
    assert result == "Total: $58.29", (f"Ожидаемая сумма не совпала. "
                                       f"Получено: '{result}'")
