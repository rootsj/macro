import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDesktopWidget, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, QThread, QObject

import time

import pyautogui as pag
from PIL import ImageGrab

class App(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):

        # url 입력 칸        
        self.line_edit = QLineEdit(self)
        self.line_edit.setText("https://shop.bmw.co.kr/online/oom/OMG0822050")
        self.line_edit.resize(250, 30)
        self.line_edit.move(20,20)  

        #열기 버튼
        self.url_button = QPushButton(self)
        self.url_button.move(20, 100)
        self.url_button.setText('열기')
        self.url_button.clicked.connect(lambda:self.openWeb(self.line_edit.text()))


        #시작 버튼
        self.url_button = QPushButton(self)
        self.url_button.move(20, 140)
        self.url_button.setText('시작')
        self.url_button.clicked.connect(self.Mythread)

        # 닫기 버튼
        btn = QPushButton('Quit', self)
        btn.move(20, 250)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 기본 창 크기
        self.setWindowTitle('성공 기원')
        self.setWindowIcon(QIcon('static/icon.webp'))
        self.resize(400, 300)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button_event(self):
        text = self.line_edit.text() # line_edit text 값 가져오기
        self.text_label.setText(text) # label에 text 설정하기

    def openWeb(object, url):
        webbrowser.open(url)

    def Mythread(self):
        for i in range(1000000):
            thread = Ui_MainWindow.threadclass(self)
            thread.start()

class Macro():
    def detect():
        stop = pag.locateOnScreen("static/stop.jpg")

        if(stop is not None):
            getPos = pag.center(stop)
            pag.moveTo(getPos)
            pag.click()
            pag.hotkey('ctrl', 'r')



class ThreadClass(QThread):
    def __init__(self, parent = None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        try:
            print("test")
            # Macro.detect()
            time.sleep(1)
        except:
            print("except")
            time.sleep(1)

class Ui_MainWindow(QObject):
    def __init__(self, parent = None):
        self.threadclass = ThreadClass(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())