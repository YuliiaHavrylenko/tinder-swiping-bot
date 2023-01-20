from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options = chrome_options

chromedriver_path = "/Users/volt/Development/chromedriver"
driver = webdriver.Chrome(chromedriver_path, chrome_options=chrome_options)
driver.get("https://tinder.com/")
sleep(5)


def login_tinder():
    login_button = driver.find_element(By.XPATH, '//html/body/div[1]/div[1]/div[1]/div[1]/main/div[1]/div[1]/div[1]/div[1]/div[1]/header/div[1]/div[2]/div[2]/a')
    login_button.click()
    login_facebook = driver.find_element(By.XPATH, '//html/body/div[2]/main/div[1]/div[1]/div[1]/div[1]/div[3]/span/div[2]/button')
    sleep(5)
    login_facebook.click()


login_tinder()
