import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import listXpath
import listIdPengumuman

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#untuk full screne
driver.maximize_window()
# Navigate to url
driver.get("https://cr-bo-silvi-admin.netlify.app")
# to enter search term, we need to locate the search textbox
driver.find_element_by_id("email").send_keys(listIdPengumuman.email)
driver.find_element_by_id("password").send_keys(listIdPengumuman.password)
#untuk click button masuk
driver.find_element_by_xpath(listXpath.buttonMasuk).click()

#page pengumuman
time.sleep(2)
driver.find_element_by_xpath(listXpath.menuPengumuman).click()
driver.find_element_by_id('title').send_keys(listIdPengumuman.titleKeys)
driver.find_element_by_id('message').send_keys(listIdPengumuman.messageKeys)

#atur jadwal
driver.find_element_by_xpath(listXpath.buttonAturJadwal).click()
time.sleep(2)
driver.find_element_by_id('hariTanggal').send_keys(listIdPengumuman.hariTanggalKeys)
driver.find_element_by_id('jam').send_keys(listIdPengumuman.jamKeys)
driver.find_element_by_xpath(listXpath.buttonSimpanJadwal).click()