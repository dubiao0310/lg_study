from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver

desire_cap = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True  # 解决更新弹窗、登陆信息
}

# appium server http://127.0.0.1:4723
# /wd/hub 固定写法
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)

TouchAction(driver).tap(x=293, y=1401).perform()
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView")
el3.click()
