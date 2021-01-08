from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    def generate_password(self):
        pwd=self.Box_password.currentText()       
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"        
        p =  "".join(random.sample(s,int(pwd )))
        self.label.setText(p)
    def generate_otp(self):
        otp=self.Box_otp.currentText()       
        s = "1234567890"        
        p =  "".join(random.sample(s,int(otp )))
        self.label.setText(p)    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 227)
        MainWindow.setStyleSheet("background-color: rgb(182, 102, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 261, 71))
        self.label.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.label.setText("Welcome to password and OTP generator::~")
        self.label.setObjectName("label")
        self.Box_password = QtWidgets.QComboBox(self.centralwidget)
        self.Box_password.setGeometry(QtCore.QRect(60, 130, 69, 22))
        self.Box_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(172, 116, 255);")
        self.Box_password.setObjectName("Box_password")
        self.Box_password.addItem("")
        self.Box_password.addItem("")
        self.Box_password.addItem("")
        self.Box_password.addItem("")
        self.Box_password.addItem("")
        self.Box_password.addItem("")
        self.Box_password.addItem("")
        self.Box_password.addItem("")
        self.Box_password.addItem("")
        self.password = QtWidgets.QPushButton(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(60, 160, 75, 23))
        self.password.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(47, 68, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(47, 68, 255);\n"
"}\n"
"")
        self.password.setObjectName("password")
        self.password.clicked.connect(self.generate_password)
        self.Box_otp = QtWidgets.QComboBox(self.centralwidget)
        self.Box_otp.setGeometry(QtCore.QRect(240, 130, 69, 22))
        self.Box_otp.setStyleSheet("background-color: rgb(226, 62, 255);\n"
"color: rgb(255, 255, 255);")
        self.Box_otp.setObjectName("Box_otp")
        self.Box_otp.addItem("")
        self.Box_otp.addItem("")
        self.Box_otp.addItem("")
        self.OTP = QtWidgets.QPushButton(self.centralwidget)
        self.OTP.setGeometry(QtCore.QRect(240, 160, 75, 23))
        self.OTP.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 11, 43);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 11, 43);\n"
"}")
        self.OTP.setObjectName("OTP")
        self.OTP.clicked.connect(self.generate_otp)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Box_password.setItemText(0, _translate("MainWindow", "16"))
        self.Box_password.setItemText(1, _translate("MainWindow", "15"))
        self.Box_password.setItemText(2, _translate("MainWindow", "14"))
        self.Box_password.setItemText(3, _translate("MainWindow", "13"))
        self.Box_password.setItemText(4, _translate("MainWindow", "12"))
        self.Box_password.setItemText(5, _translate("MainWindow", "11"))
        self.Box_password.setItemText(6, _translate("MainWindow", "10"))
        self.Box_password.setItemText(7, _translate("MainWindow", "9"))
        self.Box_password.setItemText(8, _translate("MainWindow", "8"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.Box_otp.setItemText(0, _translate("MainWindow", "6"))
        self.Box_otp.setItemText(1, _translate("MainWindow", "5"))
        self.Box_otp.setItemText(2, _translate("MainWindow", "4"))
        self.OTP.setText(_translate("MainWindow", "OTP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''

print(("\t\t\t\t\033[96m {}\033[00m" .format('Welcome to password generator::~ ')))

print(("\033[96m {}\033[00m" .format('Enter your password length: ')))
passlen = int(input())
p =  "".join(random.sample(s,passlen ))
print(p)
'''