from time import sleep
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import listXpath
import listIdDisbursement

driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
#untuk full screne
driver.maximize_window()
# Navigate to url
driver.get("https://cr-bo-silvi-admin.netlify.app")
# to enter search term, we need to locate the search textbox
driver.find_element_by_id("email").send_keys(listIdDisbursement.email)
driver.find_element_by_id("password").send_keys(listIdDisbursement.password)
#untuk click button masuk
driver.find_element_by_xpath(listXpath.buttonMasuk).click()

#page disbursement
time.sleep(3)
driver.find_element_by_xpath(listXpath.menuDisbursement).click()

time.sleep(2)
driver.find_element_by_xpath(listXpath.biayaAdminField).click()
driver.find_element_by_xpath(listXpath.biayaAdminField).send_keys(Keys.CONTROL + Keys.SHIFT + Keys.ARROW_LEFT + Keys.BACKSPACE)
driver.find_element_by_xpath(listXpath.biayaAdminField).send_keys(listIdDisbursement.biayaAdminFieldKeys)

driver.find_element_by_xpath(listXpath.minimumNominalDisbursement).click()
driver.find_element_by_xpath(listXpath.minimumNominalDisbursement).send_keys(Keys.CONTROL + Keys.SHIFT + Keys.ARROW_LEFT + Keys.BACKSPACE)
driver.find_element_by_xpath(listXpath.minimumNominalDisbursement).send_keys(listIdDisbursement.minimumNominalDisbursementKeys)

# driver.find_element_by_xpath(listXpath.buttonSimpan).click()