from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv

# Ruta correcta del controlador de Chrome
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")

username = driver.find_element(By.ID, 'session_key')
username.send_keys('EMAIL')

password = driver.find_element(By.ID, 'session_password')
password.send_keys('PASSWORD')

login_button = driver.find_element(By.CSS_SELECTOR, '.sign-in-form__submit-btn--full-width')
login_button.submit()
time.sleep(15)

with open('archivo.csv', 'r') as file: 
     reader = csv.reader(file)
     next(reader)
     for row in reader:
            link = row[0]
            print(link)
            driver.get(link)
            time.sleep(5)
            mas_button = driver.find_element(By.ID, 'ember338')

            select = Select(mas_button)

            select.select_by_visible_text("Conectar")
            
            wait = WebDriverWait(driver, 10)
            mas_button = wait.until(EC.visibility_of_element_located((By.ID, 'ember338')))
            button = driver.find_element(By.ID,'ember342')
            button.click()

            #connect_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "ember407")))
            # Haz clic en el botón "Conectar"
            #connect_button.click()
driver.quit()
    
