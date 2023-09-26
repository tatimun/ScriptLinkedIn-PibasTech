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
username.send_keys('INSERTE MAIL @gmail.com')

password = driver.find_element(By.ID, 'session_password')
password.send_keys('INSERTE CONTRASEÑA')

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
            # mas_button = driver.find_element(By.ID, 'ember338')

            # select = Select(mas_button)

            # select.select_by_visible_text("Conectar")
            
            element = driver.find_element("xpath", '//div[3]/div/div[2]/button')

            # Realizar acciones con el elemento encontrado
            element.click()
            time.sleep(10)
            print("hasta aca")
            element2 = driver.find_element("xpath", '//div[2]/div/div/ul/li[3]/div')
            element2.click()

            print("hasta aca2")
            time.sleep(15)
            element3 = driver.find_element("xpath", '//button[contains(., "Enviar")]')
            element3.click()
            # print("Se agrego a " + link)

driver.quit()
    
