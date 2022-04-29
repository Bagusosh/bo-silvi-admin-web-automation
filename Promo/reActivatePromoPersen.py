import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import listXpath
import listIdPromo

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#untuk full screne
driver.maximize_window()
# Navigate to url
driver.get("https://cr-bo-silvi-admin.netlify.app")
# to enter search term, we need to locate the search textbox
driver.find_element_by_id("email").send_keys(listIdPromo.email)
driver.find_element_by_id("password").send_keys(listIdPromo.password)
#untuk click button masuk
driver.find_element_by_xpath(listXpath.buttonMasuk).click()

#page promo
time.sleep(5)
driver.find_element_by_xpath(listXpath.menuPromo).click()

#filter nama daftar restoran yang sudah status selesai
time.sleep(3)
driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[4]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath(listXpath.fiturFilter).click()
time.sleep(3)   
driver.find_element_by_xpath(listXpath.searchName).send_keys(listIdPromo.searchNameKeys)

#update promo
time.sleep(3)
driver.find_element_by_xpath(listXpath.buttonRincian).click()

driver.find_element_by_xpath(listXpath.buttonAturJadwal).click()