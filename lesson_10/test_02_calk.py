import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.title("Проверка сложения 7 + 8 с задержкой на Slow Calculator")
@allure.description(
    "Тест проверяет работу калькулятора на странице slow-calculator.html: "
    "устанавливается задержку 45 сек, вводит выражение 7 + 8 =, "
    "ожидается результат 15."
)
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    calc_page = CalculatorPage(
        driver,
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html",
    )
    with allure.step("Открыть страницу калькулятора"):
        calc_page.open()

    with allure.step("Установить задержку в поле #delay на 45 секунд"):
        calc_page.set_delay()

    with allure.step("Ввести выражение 7 + 8 ="):
        calc_page.enter_expression()

    with allure.step("Получить и проверить результат"):
        result = calc_page.get_result()
        assert result == "15", f"Ожидался результат 15, но получено: {result}"
