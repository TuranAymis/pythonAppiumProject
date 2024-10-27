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

el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Chrome"]')
el.click()

time.sleep(2)

driver = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]').send_keys("Galatasaray")

time.sleep(2)

driver.quit()
