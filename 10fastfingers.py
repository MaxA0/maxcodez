from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path="/Users/maxdocs/Downloads/chromedriver")
driver.get("https://10fastfingers.com/advanced-typing-test/english")

delay = 10
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'CybotCookiebotDialogBodyLevelButtonAccept')))

driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonAccept").click()

sleep(3)
word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
sleep(2)
words = word_list.split('|')

for i in range(len(words)):
    driver.find_element_by_id("inputfield").send_keys(words[i] + " ")
    sleep(0.15)

print(words)
