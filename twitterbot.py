from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
driver = webdriver.Chrome(executable_path="/Users/maxdocs/Downloads/chromedriver")
driver.get("https://twitter.com/")
sleep(3)
driver.find_element_by_name('session[username_or_email]').send_keys("yeet")
driver.find_element_by_name('session[password]').send_keys("yeet")
sleep(2)
driver.find_element_by_name('session[password]').send_keys(Keys.RETURN)
sleep(3)
links = ["https://youtu.be/hC153EaOWE4", "https://youtu.be/kaYWC2Vsq24", "https://youtu.be/jBxRGcDmfWA", "https://youtu.be/el1b7AgsShw", "https://youtu.be/Wpjc4ZCvKRU"]
tags = ["#programming", "#coding", "#programmer", "#developer", "#python", "#bot", "#code", "#devlogs", "#unity", "#programmerlife", "#coder", "#thisistotallynotautomated"]

while True:
    driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
    sleep(1)
    body = random.choice(links) + " " + random.choice(tags)+ " " + random.choice(tags)+ " " + random.choice(tags)
    driver.find_element_by_class_name("notranslate").click()
    sleep(1)
    driver.find_element_by_class_name("notranslate").send_keys(body)
    sleep(1)
    driver.find_element_by_class_name("notranslate").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
    sleep(2)

