from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://united-km.com")

try:
    # Изчаква до 10 секунди, докато елементът стане видим
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Актуални Валутни Курсове')]"))
    )
    print("Елементът 'Актуални Валутни Курсове' съществува на страницата.")
except:
    print("Елементът 'Актуални Валутни Курсове' не съществува на страницата.")

driver.quit()
