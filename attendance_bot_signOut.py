from selenium import webdriver
from time import sleep

from secrets import username, password, portal, attnportal

class AttendanceBot():
    def __init__(self):
        self.driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

    def markAttendance(self):
        self.driver.get(portal)

        sleep(2)

        username_in = self.driver.find_element_by_xpath('/html/body/app-root/uas-portal/div/div[2]/main/div/o-auth/section/div/app-login/section/div/div/form/div[1]/gt-icon-input/div/input')
        username_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('/html/body/app-root/uas-portal/div/div[2]/main/div/o-auth/section/div/app-login/section/div/div/form/div[2]/gt-icon-input/div/input')
        password_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/app-root/uas-portal/div/div[2]/main/div/o-auth/section/div/app-login/section/div/div/form/div[3]/button/h6')
        login_btn.click()

        sleep(8)

        attendence_tab = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[4]/a')
        attendence_tab.click()

        CurWin = self.driver.current_window_handle

        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(attnportal)

        signOut_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/div/div[1]/div/table/tbody/tr[5]/td/button[2]')
        signOut_btn.click()

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        logout_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/ul[2]/li[3]/a')
        logout_btn.click()

        sleep(2)

        self.driver.close()

bot = AttendanceBot()
bot.markAttendance()