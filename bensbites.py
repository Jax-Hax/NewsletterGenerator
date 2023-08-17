from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

# Create a WebDriver instance
driver = webdriver.Firefox()

# Open the login page
driver.get("https://bensbites.beehiiv.com/")
driver.find_element(By.CSS_SELECTOR, "a.group.flex.h-full.w-full.border.transition-all.group-hover:brightness-110.rounded-lg.flex-col").click()
time.sleep(2)
# Find the username and password input fields and enter your credentials
username_input = driver.find_element(By.CSS_SELECTOR, '[name="lastName"]')
password_input = driver.find_element(By.CSS_SELECTOR, '[name="firstName"]')

username_input.send_keys("Bulbrook")
password_input.send_keys("Jackson")
# Find the select element
select_element = driver.find_element(By.ID, 'dob_month')

# Create a Select object
select = Select(select_element)

# Select an option by value
select.select_by_value("09")
# Find the select element

select_element = driver.find_element(By.ID, 'dob_day')

# Create a Select object
select = Select(select_element)

# Select an option by value
select.select_by_value("19")
# Find the select element
select_element = driver.find_element(By.ID, 'dob_year')

# Create a Select object
select = Select(select_element)

# Select an option by value
select.select_by_value("2007")
# Find and click the login button
login_button = driver.find_element(By.CSS_SELECTOR, '[onclick="loginSubmit()"]')
login_button.click()

# Wait for the website to load after login
wait = WebDriverWait(driver,2000)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
while True:
    wait.until(EC.presence_of_element_located((By.ID, "ButtonTwo")))

    # Now you are signed in and can run your desired script on the website

    # Find the button with ID "conv" and wait for it to become clickable
    button = wait.until(EC.element_to_be_clickable((By.ID, "ButtonTwo")))
    print("Next screen")
    # Click on the button
    driver.execute_script("arguments[0].scrollIntoView();", button)
    time.sleep(1)
    button.click()