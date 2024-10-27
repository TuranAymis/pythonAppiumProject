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

#el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Phone"]')
#el.click()

time.sleep(2)

#driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="key pad").click()
#driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='1']").click()
#driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='2']").click()
#driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='3']").click()
time.sleep(2)

driver.quit()
