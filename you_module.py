from time import sleep
from selenium.webdriver.common.by import By



def get_data_from_youtube(driver, ylink):
    driver.get(ylink)
    followers = driver.find_element(By.XPATH, value= '//*[@id="subscriber-count"]')
    nums = followers.text.split()
    print(nums[0])
