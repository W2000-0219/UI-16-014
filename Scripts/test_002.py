from selenium import webdriver as web
from appium import webdriver as app
import allure

class Test003:

    def setup_class(self):
        # web
        self.web_driver = web.Chrome()
        self.web_driver.get("http://www.baidu.com")

        # app
        # server  启动参数
        desired_caps = {
            'platfromName': "Android",
            'platfromVersion': "5.1",
            'deviceName': 'sanxing',
            'appPackage': 'com.android.settings',
            'appActivity': '.Settings'
        }

        # 声明我们的driver对象
        self.app_driver = app.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        self.web_driver.quit()
        self.app_driver.quit()

    def test_001_appium(self):
        allure.attach(self.app_driver.get_screenshot_as_png(), "spp-截图",allure.attachment_type.PNG)

    def test_002_selenium(self):
        allure.attach(self.app_driver.get_screenshot_as_png(), "spp-截图",allure.attachment_type.PNG)