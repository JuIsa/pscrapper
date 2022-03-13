from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


twitter = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span'

def get_data_from_twitter(driver, tlink):
    # sleep(2)
    driver.get(tlink)
    sleep(1) #timer to load page
    driver.execute_script("window.scrollTo(0,300)")
    try:
        element = driver.find_element(By.XPATH, value=xpath)
    except:
        pass
    else:
        ActionChains(driver).move_to_element(element).click().perform()#click anyway
        sleep(1)
    followers = driver.find_element(By.XPATH, value=twitter)
    print(followers.text)