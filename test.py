from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import sys
from PyQt5.QtQuickWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, QObject
from PyQt5 import uic
import threading
import webbrowser

UserUI = uic.loadUiType('autobuy.ui')[0]

class AutoBuy(QMainWindow, UserUI):
    def __init__(self, *args, **kwargs):
        super(AutoBuy, self).__init__(*args, **kwargs)
        UserUI.__init__(self)
        self.setupUi(self)
        self.ID = '*******'
        self.PASSWORD = '********'
        self.HOMEPAGE = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
        self.ITEMURL = "https://smartstore.naver.com/aer-shop/products/4722827602"
        self.lineEdit.setText(self.HOMEPAGE)
        self.lineEdit_2.setText(self.ITEMURL)
        self.lineEdit_3.setText(self.ID)
        self.lineEdit_4.setText(self.PASSWORD)
        self.pushButton.clicked.connect(self.Mythread)
        self.pushButton_2.clicked.connect(self.End)
        self.pushButton_3.clicked.connect(self.Login)
        self.pushButton_4.clicked.connect(self.test)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)

  #클립보드에 input을 복사한 뒤
    #해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
    def copy_input(self, xpath, input):
        pyperclip.copy(input)
        self.driver.find_element_by_xpath(xpath).click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)

    def Login(self):
        self.HOMEPAGE = self.lineEdit.text()
        self.ITEMURL = self.lineEdit_2.text()
        self.ID = self.lineEdit_3.text()
        self.PASSWORD = self.lineEdit_4.text()
        self.driver.get(self.HOMEPAGE)
        self.copy_input('//*[@id="id"]', self.ID)
        time.sleep(1)
        self.copy_input('//*[@id="pw"]', self.PASSWORD)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.find_element_by_xpath('//a[@id="new.save"]').click()
        self.driver.get(self.ITEMURL)

    def Buy(self):
        try:
            self.driver.get(self.ITEMURL)
            self.driver.find_element_by_xpath('//div[@class="selectbox-label"]').click()
            self.driver.find_element_by_xpath('//div[@class="selectbox-list"]').click()
            self.driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[4]").text
            self.driver.find_element_by_xpath('//span[@class="mask2"]').click()
            self.driver.find_element_by_xpath('//a[@class="_responsive_scrap_button_click(nmp.front.sellershop.toggleKeep(4722827602)) _stopDefault _productPreLaunch N=a:pcs.mylist"]').click()
            time.sleep(1)
        except:
            self.driver.get(self.ITEMURL)
            self.driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[4]").text
            self.driver.find_element_by_xpath('//span[@class="mask2"]').click()
            self.driver.find_element_by_xpath('//a[@class="_responsive_scrap_button_click(nmp.front.sellershop.toggleKeep(4722827602)) _stopDefault _productPreLaunch N=a:pcs.mylist"]').click()
            time.sleep(1)

    def End(self):
        sys.exit()

    def test(self):
        pass

    def Mythread(self):
        for i in range(1000000):
            thread = Ui_MainWindow.threadclass(self)
            thread.start()

class ThreadClass(QThread):
    def __init__(self, parent = None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        try:
            self.driver.get(self.ITEMURL)
            self.driver.find_element_by_xpath('//div[@class="selectbox-label"]').click()
            self.driver.find_element_by_xpath('//div[@class="selectbox-list"]').click()
            self.driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[4]").text
            self.driver.find_element_by_xpath('//span[@class="mask2"]').click()
            self.driver.find_element_by_xpath('//a[@class="_responsive_scrap_button_click(nmp.front.sellershop.toggleKeep(4722827602)) _stopDefault _productPreLaunch N=a:pcs.mylist"]').click()
            time.sleep(1)
        except:
            self.driver.get(self.ITEMURL)
            self.driver.find_element_by_xpath("/html/body/div[2]/div/ul/li[4]").text
            self.driver.find_element_by_xpath('//span[@class="mask2"]').click()
            self.driver.find_element_by_xpath('//a[@class="_responsive_scrap_button_click(nmp.front.sellershop.toggleKeep(4722827602)) _stopDefault _productPreLaunch N=a:pcs.mylist"]').click()
            time.sleep(1)

class Ui_MainWindow(QObject):
    def __init__(self, parent = None):
        self.threadclass = ThreadClass(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoBuy()
    window.show()
    app.exec_()