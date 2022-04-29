import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
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

#jika menggunakan find_elements_by_xpath, diakhiri dengan array
#button create promo
time.sleep(5)
driver.find_element_by_xpath(listXpath.buttonCreatePromo).click()

#Input data Create Promo
time.sleep(3)
driver.find_element_by_id("nama_promo").send_keys(listIdPromo.namaPromoKeys)
driver.find_element_by_id("deskripsi_promo").send_keys(listIdPromo.deskripsiPromoKeys)
driver.find_element_by_id("budget_allocation").send_keys(listIdPromo.budgetAllocationKeys)
driver.find_element_by_xpath(listXpath.toggleDiskon).click()
driver.find_element_by_id("kode_promo").send_keys(listIdPromo.kodePromoKeys)
driver.find_element_by_id("jumlah_diskon").click()
driver.find_element_by_id("jumlah_diskon").send_keys(Keys.BACKSPACE)
driver.find_element_by_id("jumlah_diskon").send_keys(listIdPromo.jumlahDiskonKeys)
driver.find_element_by_id("minTransaksi").click()
driver.find_element_by_id("minimum_value").send_keys(listIdPromo.minimumValueKeys)
driver.find_element_by_id("maxPotongan").click()
driver.find_element_by_id("maximum_discount").send_keys(listIdPromo.maximumDiscountKeys)


driver.find_element_by_id('tanggalBerlaku').click()
driver.find_element_by_id('tanggalBerlaku').send_keys(listIdPromo.tanggalBerlakuKeys)
driver.find_element_by_id('tanggalBerakhir').click()
driver.find_element_by_id('tanggalBerakhir').send_keys(listIdPromo.tanggalBerakhirKeys)

#togle atur jam
driver.find_element_by_xpath(listXpath.toggleJam).click()
time.sleep(2)
driver.find_element_by_id("waktuBerlaku").click()
time.sleep(2)
driver.find_element_by_id("waktuBerlaku").send_keys(listIdPromo.waktuBerlakuKeys)
time.sleep(2)
driver.find_element_by_id("waktuBerakhir").click()
time.sleep(2)
driver.find_element_by_id("waktuBerakhir").send_keys(listIdPromo.waktuBerakhirKeys)

#id payment methods

driver.find_element_by_id(listIdPromo.qris).click()
driver.find_element_by_id(listIdPromo.flickpay).click()
driver.find_element_by_id(listIdPromo.debit).click()

#list filter Kota
driver.find_element_by_xpath(listXpath.buttonFilter).click()
time.sleep(2)
driver.find_element_by_id(listIdPromo.bandung).click()
time.sleep(2)
driver.find_element_by_id(listIdPromo.surabaya).click()
time.sleep(2)
driver.find_element_by_id(listIdPromo.tangerang).click()

#search merchant
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() #untuk escape dari pop up
driver.find_element_by_id('search').click()
time.sleep(4)
driver.find_element_by_id('search').send_keys(listIdPromo.searchKey)
time.sleep(4)
driver.find_element_by_id('select_all').click()

#button submit
driver.find_element_by_xpath(listXpath.buttonSimpan).click()

#untuk close web
time.sleep(5)
driver.close()