# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pytesseract
from PIL import Image
import random
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 41))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("background: #221F1F; color: white;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 50, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(40)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: #221F1F; color: white; border: white solid 0px; border-radius: 5px")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 130, 1321, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(25)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background: white; color: #221F1F; border: 2px solid #221F1F;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(265, 200, 831, 61))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(40)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: #221F1F; color: white; border: white solid 0px; border-radius: 5px")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.func()
    def func(self):
        self.pushButton_2.clicked.connect(self.main_func)
        self.pushButton.clicked.connect(self.exit)
    def exit(self):
        exit()
    def main_func(self):
        img = Image.open(self.lineEdit.text())
        pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"
        custom_config = r"--oem 3 --psm 13"
        text = pytesseract.image_to_string(img, config=custom_config)
        with open(f"C:/Users/user/Desktop/image_to_text({random.randint(-999999999999999999999999999999999999,999999999999999999999999999999999999)}).txt", "w", encoding="utf-8") as file:
            file.write(text)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Images to Texts 0.0.1"))
        self.label.setText(_translate("MainWindow", "                                                                     Images to Texts"))
        self.pushButton.setText(_translate("MainWindow", "Close"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Write link and image..."))
        self.pushButton_2.setText(_translate("MainWindow", "Convert Image to texts"))
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
