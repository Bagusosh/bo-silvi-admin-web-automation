import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import listXpath
import listIdAkuisisi

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#untuk full screne
driver.maximize_window()
# Navigate to url
driver.get("https://cr-bo-silvi-admin.netlify.app")
# to enter search term, we need to locate the search textbox
driver.find_element_by_id("email").send_keys(listIdAkuisisi.email)
driver.find_element_by_id("password").send_keys(listIdAkuisisi.password)
#untuk click button masuk
driver.find_element_by_xpath(listXpath.buttonMasuk).click()

#restoran menu
time.sleep(5)
driver.find_element_by_xpath(listXpath.restoranMenu).click()

#Akuisisi Page
time.sleep(5)
driver.find_element_by_xpath(listXpath.pageAkuisisi).click()

#searchbar
time.sleep(5)
driver.find_element_by_id('search').click()
time.sleep(5)
driver.find_element_by_id('search').send_keys(listIdAkuisisi.searchKeys)
time.sleep(5)
driver.find_element_by_xpath(listXpath.buttonCekDataAkuisisi).click()
time.sleep(5)
driver.find_element_by_id('jumlahMejaRestoran').send_keys(Keys.TAB + Keys.ENTER + Keys.ESCAPE)
