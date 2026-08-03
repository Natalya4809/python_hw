from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")  # Найти все ссылки

    for link in links:
        assert link.is_displayed()

    assert len(links) == 10

    assert "1" in len[0].text

    driver.quit()