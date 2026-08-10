from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

#Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")

#Установите cookie пользователя 1.
    driver.add_cookie({
        "name": "SESION",
        "value": "NzA0MGJjOTItODNjNi00MTU3LWFiYzEtOWFjZWEyNjQxZTI5",
        "domain": "gitflic.ru"
    })

#Обновите страницу.
    driver.refresh()

#Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/tatatu2343")

    sleep(5)

#Сохраните текущий URL.
    current_url = driver.current_url
#Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()
    driver.refresh()

    sleep(5)

#Установите cookie пользователя 2.
    driver.add_cookie({
        "name": "SESION",
        "value": "OGI4ZmRiZTgtNDQ1Zi00YzM3LTk4NzctOGJhZmU3NTc0YmFk",
        "domain": "gitflic.ru"
    })
#Обновите страницу.
    driver.refresh()
#Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/rapapa567")

    sleep(5)

    #Сохраните текущий URL.
    current_url = driver.current_url

#Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    url_user1 ! = url_user2

driver.quit()
