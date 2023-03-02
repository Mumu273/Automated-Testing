from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe")

driver.get("https://github.com/login")



driver.find_element(By.NAME, "login").send_keys("ishratmumu607@gmail.com")

driver.find_element(By.NAME, "password").send_keys("Cse18-37832-2")


driver.find_element(By.NAME, "commit").submit()

print(driver.title)


input_title=driver.title
output_title="Stack Overflow - Where Developers Learn, Share, & Build Careers"
if input_title==output_title:
    print("Passed")
else:
    print("Failed")

