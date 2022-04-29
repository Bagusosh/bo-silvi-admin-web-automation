import time
from selenium import webdriver
import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import listXpath
import listIdDataResto

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#untuk full screne
driver.maximize_window()
# Navigate to url
driver.get("https://cr-bo-silvi-admin.netlify.app")
# to enter search term, we need to locate the search textbox
driver.find_element_by_id("email").send_keys(listIdDataResto.email)
driver.find_element_by_id("password").send_keys(listIdDataResto.password)
#untuk click button masuk
driver.find_element_by_xpath(listXpath.buttonMasuk).click()

#page restoran
time.sleep(5)
driver.find_element_by_xpath(listXpath.restoranMenu).click()

#page data restoran
time.sleep(3)
driver.find_element_by_xpath(listXpath.pageDataResto).click()
driver.find_element_by_id('search').click()
driver.find_element_by_id('search').send_keys(listIdDataResto.searchKeys)
time.sleep(3)
driver.find_element_by_xpath(listXpath.buttonLihatProfile).click()

#generate qr
time.sleep(3)
driver.find_element_by_xpath(listXpath.generateQrButton).click()

#generate stiker
time.sleep(3)
driver.find_element_by_xpath(listXpath.generateQrStickerButton).click()

time.sleep(10)
driver.close()