import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import listXpath
import listIdPayment

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#untuk full screne
driver.maximize_window()
# Navigate to url
driver.get("https://cr-bo-silvi-admin.netlify.app")
# to enter search term, we need to locate the search textbox
driver.find_element_by_id("email").send_keys(listIdPayment.email)
driver.find_element_by_id("password").send_keys(listIdPayment.password)
#untuk click button masuk
driver.find_element_by_xpath(listXpath.buttonMasuk).click()

#payment method page
time.sleep(3)
driver.find_element_by_xpath(listXpath.menuPayment).click()
driver.find_element_by_xpath(listXpath.buttonBuatMetodeBayar).click()
time.sleep(3)
driver.find_element_by_xpath(listXpath.fieldNamaMetode).click()
driver.find_element_by_xpath(listXpath.fieldNamaMetode).send_keys(listIdPayment.namaMetodePembayaran)
driver.find_element_by_xpath(listXpath.buttonBuat).click()
time.sleep(2)
driver.find_element_by_xpath(listXpath.buttonSelesai).click()
time.sleep(2)
#filter nama payment method
driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath(listXpath.fiturFilter).click()
time.sleep(3)
driver.find_element_by_xpath(listXpath.fieldFilter).click()
driver.find_element_by_xpath(listXpath.fieldFilter).send_keys(listIdPayment.searchNameKeys)
time.sleep(3)
driver.find_element_by_xpath(listXpath.buttonToggle).click()
driver.find_element_by_xpath(listXpath.buttonSimpan).click()
time.sleep(3)
driver.find_element_by_xpath(listXpath.buttonYaUbah).click()
time.sleep(3)
driver.find_element_by_xpath(listXpath.buttonSelesai).click()