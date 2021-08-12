from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(executable_path="/Users/maxdocs/Downloads/chromedriver")

driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
sleep(3)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys("")
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(3)
driver.find_element_by_xpath('//input[@type="password"]').send_keys("")
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(5)
driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
sleep(4)
for i in range(20):
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    sleep(0.5)
    driver.find_element_by_class_name("vO").send_keys("maxabela@gmail.com")
    driver.find_element_by_class_name("aoT").send_keys("[SUB TO MAX CODEZ OR SUFFER]")
    sleep(0.5)
    driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys("insert meme response here!")
    sleep(0.5)
    driver.find_element_by_xpath("//div[text()='Send']").click()
    sleep(1)
