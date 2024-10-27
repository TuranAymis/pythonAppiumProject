import time

from appium import *
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'UIAutomator2',
    'deviceName': 'Android',
}

url = 'http://localhost:4724'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Monster Notebook"]')
el.click()
time.sleep(3)
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Hesabım']").click()
time.sleep(2)
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='GİRİŞ YAP / ÜYE OL']").click()
time.sleep(2)
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@content-desc='eposta']").send_keys("turan.aymis@monsternotebook.com")
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@content-desc='password']").send_keys("test123")
time.sleep(2)
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='GİRİŞ YAP']").click()
driver.quit()
