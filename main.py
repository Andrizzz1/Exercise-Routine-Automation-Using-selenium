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


weeks = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'[id^="day-group-"] ')))

total_booked = 0 
total_waitlisted = 0
Already_bookedORwaitlisted = 0


Title_list = []

for tuesday in weeks:
    target_date = tuesday.find_element(By.TAG_NAME,'h2').text.split(',')[1].replace(")","")
    if "Wed" in tuesday.text or "Thu" in tuesday.text:
        class_cards = tuesday.find_elements(By.CLASS_NAME,"ClassCard_cardHeader__D9pf3")
        for cards in class_cards:
            class_times = cards.find_elements(By.CSS_SELECTOR,'[id^="class-time-"]') 
            for time in class_times:
                if "6:00 PM" in time.text:
                    button = cards.find_element(By.CSS_SELECTOR,'button')
                    class_name = cards.find_element(By.CSS_SELECTOR,'[id^="class-name-"]').text
        
                    
                    if button.text == "Booked":
                        print(f"Already Booked:{class_name} on Tue, {target_date}")
                        Already_bookedORwaitlisted += 1
                        
                    elif button.text == "Waitlisted":
                        print(f"Already on waitlist:{class_name} on Tue, {target_date}")
                        Already_bookedORwaitlisted += 1
                        
                    elif button.text == "Book Class":
                        button.click()
                        print(f"Booked Class for:{class_name} on Tue, {target_date}")
                        total_booked +=1
                        Title_list.append(f"•[New Booking] {class_name} on {target_date}")
                    else:
                        button.click()
                        print(f"Joined waitlist for:{class_name} on Tue, {target_date}")
                        total_waitlisted +=1
                        Title_list.append(f"•[New Waitlist] {class_name} on {target_date}")

                    
totals = total_booked + total_waitlisted + Already_bookedORwaitlisted
print(f"""
            --- BOOKING SUMMARY ---
            Classes booked: {total_booked}
            Waitlists joined: {total_waitlisted}
            Already booked/waitlisted: {Already_bookedORwaitlisted}
            Total Tuesday 6pm classes processed: {totals}""")

print(f" --- DETAILED CLASS LIST ---")
for i in Title_list:
    print(i)


                    