from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

test_email = "John@test.com"
test_password = "John123"

user_data_dir = os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(chrome_options)
driver.get("https://appbrewery.github.io/gym/")


button = driver.find_element(By.ID,'login-button')
button.click()

wait = WebDriverWait(driver, 10)
Create_Account = wait.until(EC.presence_of_element_located((By.ID,'toggle-login-register')))
Create_Account.click()


Name = wait.until(EC.presence_of_element_located((By.ID,'name-input')))
Name.send_keys("John")

email =driver.find_element(By.ID,'email-input')
email.send_keys(test_email)

password = driver.find_element(By.ID,'password-input')
password.send_keys(test_password)

Submit_button = driver.find_element(By.ID,'submit-button')
Submit_button.click()

User_already_exist =wait.until(EC.presence_of_element_located((By.ID,'error-message')))

if User_already_exist.text:
    login_button = driver.find_element(By.ID,'toggle-login-register')
    login_button.click()



Submit_button =  wait.until(EC.presence_of_element_located((By.ID,'submit-button')))
Submit_button.click()



find_tuesday =  wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'[id*="day-group-tue"] .ClassCard_cardHeader__D9pf3')))

for i in find_tuesday:
    locate_tue = i.text.split()
    if locate_tue[3] == '7:00' and locate_tue[4] == 'PM':
        sched_button = driver.find_element(By.XPATH,'//*[@id="book-button-spin-2026-02-03-1800"]')
        print("Booked: Spin Class on Tue, Aug 12")
        sched_button.click()


        

