from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random


def unlock_metamask(driver):
    driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
    pw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    pw.send_keys('xxxxxx')
    unlock_btn = driver.find_element(By.XPATH, '//button[normalize-space()="登录"]')
    unlock_btn.click()
    close_metamask_popup(driver)

# add new account
def add_new_account(driver):
    account_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        'button.mm-box:nth-child(2)')))
    account_btn.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
        '//button[normalize-space()="Add account or hardware wallet"]'))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
        '//button[normalize-space()="Add a new account"]'))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
        '//button[normalize-space()="创建"]'))).click()

    copy_addr_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        'button.mm-text:nth-child(1)')))
    copy_addr_btn.click()
