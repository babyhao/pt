from appium import webdriver

def get_driver():
    caps = {
        'platformName': 'Android',
        'platformVersion': '9.0',
        'deviceName': 'Phone_9.0_28',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    return webdriver.Remote('http://localhost:4723/wd/hub', caps)