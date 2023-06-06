from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализираме Selenium WebDriver (в този случай използваме Chrome WebDriver)
driver = webdriver.Chrome()

# Отваряме уебсайта
driver.get("https://united-km.com")

# Намираме елементът за бутона "Обекти" и кликаме върху него
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Обекти')]"))
)
button.click()

# Проверяваме дали се е отворила правилната страница
expected_url = "https://united-km.com/%d0%be%d0%b1%d0%b5%d0%ba%d1%82%d0%b8"
actual_url = driver.current_url

result = ""
if actual_url == expected_url:
    result = f"Страницата '{expected_url}' е отворена успешно."
else:
    result = f"Страницата '{expected_url}' не се е отворила правилно. Текущата URL е '{actual_url}'."

with open("rezultat.txt", "w", encoding="utf-8") as file:
    file.write(result)

# Затваряме браузъра
driver.quit()
