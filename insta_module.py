from time import sleep
from selenium.webdriver.common.by import By


def get_data_from_instagram(driver, ilink):
    driver.get(ilink)
    sleep(2)
    followers = driver.find_element(By.XPATH, value='/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span')
    print(followers.text)
