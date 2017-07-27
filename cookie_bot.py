from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver = (webdriver.PhantomJS())

driver.get("https://www.hipchat.com/sign_in")

# enter email

email = driver.find_element_by_id("email")
email.send_keys('(hipchat registerd email)')
next = driver.find_element_by_id('signin')
next.click()

# enter pass

password = driver.find_element_by_id('password')
password.send_keys('(hipchatpassword)')
next = driver.find_element_by_id('signin')
next.click()

# proceed to web client

launch = driver.find_element_by_link_text('Launch the web app')
launch.click()

time.sleep(8)
# open room

# currently room must be in active hipchat rooms
hipchatroom_room = driver.find_element_by_xpath('//a[@aria-label="(room name)"]')
hipchat_room.click()

#cookie karma = profit 
input_text = driver.find_element_by_id('hc-message-input')


#infinte loop for karma gains
while True:
    input_text.send_keys('(cookie)++++++', Keys.ENTER)

