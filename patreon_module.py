from time import sleep
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

xlinks = []

def button_clicker(driver,local_xpath):
    try:
        element = driver.find_element(By.XPATH, value=local_xpath)
    except:
        pass
    else:
        ActionChains(driver).move_to_element(element).click().perform()
        sleep(1)

def get_patreon_tiers(driver):
    card_classes = 'eDtzLP'
    cards = driver.find_elements(By.CLASS_NAME, value=card_classes)
    for card in cards:
        print(card.text)

def get_patreon_money(driver):
    money_classes = 'kIeXgk'
    moneys = driver.find_elements(By.CLASS_NAME, value=money_classes)
    for money in moneys:
        print(money.text) 

def get_patreon_links(driver):
    link_classes = 'FmiUF'
    links = driver.find_elements(By.CLASS_NAME, value=link_classes)
    for link in links:
        xlinks.append(link.get_attribute('href'))

def get_links():
	return xlinks

def get_data_from_patreon(driverx, url):
	driver = driverx
	patreon_cookie_x = '/html/body/div[1]/div/div/div/div/div[1]/button'
	older = '/html/body/div[2]/div/div[3]/div[5]/div/div[2]/div/div/div/div/div[3]/div/button'
	more = '/html/body/div[2]/div/div[3]/div[3]/div[2]/div[3]/div/div[2]/div[3]/div[2]/button'
	driver.get(url)
	sleep(4)
	button_clicker(driver,patreon_cookie_x)
	button_clicker(driver,older)
	driver.execute_script("window.scrollTo(0,700)")
	button_clicker(driver,more)
	get_patreon_tiers(driver)
	get_patreon_money(driver)
	get_patreon_links(driver)
	print('-----patreon is done-----')