from selenium import webdriver
from time import sleep
import patreon_module as pm
import link_handler as lh

url = ""

driver = webdriver.Firefox()
pm.get_data_from_patreon(driver, url)
lh.get_data_from_links(driver)
driver.close()

