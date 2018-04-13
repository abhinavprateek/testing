from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import time
import xlrd
driver=webdriver.PhantomJS()
driver.get('https://app.autogradr.com/assignment/273/project/515')
driver.save_screenshot('screen.png')
elem = driver.find_element_by_xpath("//input[@placeholder='you@example.com']")
elem.send_keys("abhinav@skillspeed.com")
elem = driver.find_element_by_xpath("//input[@placeholder='password']")
elem.send_keys("coolman123")
elem.send_keys(Keys.RETURN)
time.sleep(30)
driver.save_screenshot('screen1.png')
elem = driver.find_element_by_xpath("//div[contains(@class, 'ag-link') and contains(., 'browse')]")
print elem
elem.send_keys("/root/solution_fail.zip")

