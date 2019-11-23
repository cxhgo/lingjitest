from appium import webdriver

des_leidian = {
                "platformName": "Android",
                "deviceName": "2103fc06",
                "platformVersion": "6.0.1",
                "appPackage": "com.mmc.linghit.internal",
                "appActivity": "com.hule.dashi.home.guide.WelcomeActivity",
                "noReset": True,
                "udid": "2103fc06",   # 识别手机唯一标识
                'unicodeKeyboard': True,   # appium自带键盘
                'resetKeyboard': True,     # 解决中文乱码问题
                'noSign': True,
                # "automationName": "Uiautomator2",  # toast 必须用Uiautomator2
                "autoGrantPermissions": True
                }

des_yeshen = {
                "platformName": "Android",
                "deviceName": "2103fc06",
                "platformVersion": "6.0.1",
                "appPackage": "com.mmc.feelsowarm",
                "appActivity": "com.mmc.feelsowarm.WelcomeActivity",
                "noReset": True,
                "udid": "2103fc06",   # 识别手机唯一标识
                "automationName": "Uiautomator2",  # toast 必须用Uiautomator2
                "autoGrantPermissions": True,
                'unicodeKeyboard': True,   # appium自带键盘
                'resetKeyboard': True,     # 解决中文乱码问题
                }


def start_app(deviceName="leidian", port=4723):
    '''启动app'''
    if deviceName == "leidian":
        des = des_leidian
    elif deviceName == "yeshen":
        des = des_yeshen
    else:
        des = des_leidian
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % port, des)
    return driver
if __name__ == '__main__':
    driver = start_app()