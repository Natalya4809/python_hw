from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    driver.maximize_window()

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Наталья")

    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_btn.click()

    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()