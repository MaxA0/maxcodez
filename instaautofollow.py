from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="/Users/maxdocs/Downloads/chromedriver 2")
driver.get("https://instagram.com")
sleep(4)
driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys("username")
driver.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys("password")
driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()
sleep(4)
driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
sleep(3)

for i in range(5):
    driver.find_element_by_xpath('//button[text()="Follow"]')\
            .click()
    sleep(2)
driver.refresh()

