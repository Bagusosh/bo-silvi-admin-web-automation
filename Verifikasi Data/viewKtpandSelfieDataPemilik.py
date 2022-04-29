import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import listXpath
import listIdVerifData

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#untuk full screen
driver.maximize_window()
# Navigate to url
driver.get("https://cr-bo-silvi-admin.netlify.app")
# to enter search term, we need to locate the search textbox
driver.find_element_by_id("email").send_keys(listIdVerifData.email)
driver.find_element_by_id("password").send_keys(listIdVerifData.password)
#untuk click button masuk
driver.find_element_by_xpath(listXpath.buttonMasuk).click()

#page restoran
time.sleep(5)
driver.find_element_by_xpath(listXpath.restoranMenu).click()

#page verifikasi data
time.sleep(3)
driver.find_element_by_xpath(listXpath.pageVerifikasi).click()
driver.find_element_by_id('search').click()
driver.find_element_by_id('search').send_keys(listIdVerifData.searchKeys)
time.sleep(3)
driver.find_element_by_xpath(listXpath.buttonCekData).click()
time.sleep(3)
driver.find_element_by_xpath(listXpath.buttonLihatKtpAndSelfie).click()