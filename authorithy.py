import logging
import time

import requests
from bs4 import BeautifulSoup

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

session = requests.Session()
main_url = "https://openweathermap.org/"
session.headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "openweathermap.org",
    "Origin": main_url,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Referer": main_url,
    "Upgrade-Insecure-Requests": "1",
}

url = "https://home.openweathermap.org/users/sign_in"

# Создаем сессию и указываем ему наш user-agent
response = session.get(url)
soup = BeautifulSoup(response.content)

csrfToken = soup.find("meta", {"name": "csrf-token"})
authenticity_token = csrfToken.get("content")
print(type(authenticity_token))

data = {
    "utf8": "✓",
    "authenticity_token": authenticity_token,
    "user[email]": "desoud.ck@gmail.com",  # Email
    "user[password]": "18283848Qw",  # Пароль
    "user[remember_me]": "0",
    "commit": "Submit",
    "user[student]": "",
}

# Получение токена
response = session.post(url, data)

time.sleep(2)  # Пауза 2 сек :)
html = response.text  # Авторизуемся. В html будет наш ответ после авторизации

if __name__ == "__main__":
    if (
        "Log Out" in html
    ):  # Если строка 'Log Out' есть в html, значит авторизация прошла успешно
        print("Login OK!")
    else:
        print("Login Error!")
