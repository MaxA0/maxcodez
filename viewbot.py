from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver1 = webdriver.Chrome(executable_path="/Users/maxdocs/Downloads/chromedriver")
driver2 = webdriver.Chrome(executable_path="/Users/maxdocs/Downloads/chromedriver")
driver3 = webdriver.Chrome(executable_path="/Users/maxdocs/Downloads/chromedriver")

driver1.get("https://youtu.be/btDQoCQlKn8")
driver2.get("https://youtu.be/btDQoCQlKn8")
driver3.get("https://youtu.be/btDQoCQlKn8")

while True:
    sleep(60)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
