from PyQt5 import QtCore, QtGui, QtWidgets
from registration_form import Ui_RegistrationForm  # Import the Ui_RegistrationForm class

class Ui_WelcomePage(object):
    def setupUi(self, WelcomePage):
        WelcomePage.setObjectName("WelcomePage")
        WelcomePage.setFixedSize(800, 600)
        WelcomePage.setStyleSheet("QPushButton{\n"
            "background-color:qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
            "color:rgb(255, 255, 255)\n"
            "}\n"
            "QPushButton{\n"
            "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 255, 255, 147));\n"
            "color:rgb(255,255,255);\n"  # white text color
            "background-color:rgb(11, 110, 150); \n"  
            "border-radius: 5px;\n"
            "}\n"
            "QLabel{\n"
            "font: 75 italic 14pt \"Century Schoolbook L\";\n"
            "\n"
            "}\n"
        )
        self.centralwidget = QtWidgets.QWidget(WelcomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_Welcome.setGeometry(QtCore.QRect(40, 60, 721, 71))
        self.label_Welcome.setObjectName("label_Welcome")
        
        self.btn_RegisterStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_RegisterStudent.setGeometry(QtCore.QRect(220, 200, 331, 41))
        self.btn_RegisterStudent.setObjectName("btn_RegisterStudent")
        self.btn_RegisterStudent.clicked.connect(self.openRegistrationForm)

        WelcomePage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WelcomePage)
        self.statusbar.setObjectName("statusbar")
        WelcomePage.setStatusBar(self.statusbar)

        self.retranslateUi(WelcomePage)
        QtCore.QMetaObject.connectSlotsByName(WelcomePage)

    def retranslateUi(self, WelcomePage):
        _translate = QtCore.QCoreApplication.translate
        WelcomePage.setWindowTitle(_translate("WelcomePage", "Mount Kenya University"))
        self.label_Welcome.setText(_translate("WelcomePage", "Welcome to Mount Kenya University Registration System"))
        self.btn_RegisterStudent.setText(_translate("WelcomePage", "Click Here To Register a Student"))

    def openRegistrationForm(self):
        self.registrationWindow = QtWidgets.QMainWindow()
        self.registrationForm = Ui_RegistrationForm()
        self.registrationForm.setupUi(self.registrationWindow)
        self.registrationWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QMainWindow()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
from registration_form import Ui_RegistrationForm  # Import the Ui_RegistrationForm class

class Ui_WelcomePage(object):
    def setupUi(self, WelcomePage):
        WelcomePage.setObjectName("WelcomePage")
        WelcomePage.setFixedSize(800, 600)
        WelcomePage.setStyleSheet("QPushButton{\n"
            "background-color:qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
            "color:rgb(255, 255, 255)\n"
            "}\n"
            "QPushButton{\n"
            "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 255, 255, 147));\n"
            "color:rgb(255,255,255);\n"  # white text color
            "background-color:rgb(11, 110, 150); \n"  
            "border-radius: 5px;\n"
            "}\n"
        )
        self.centralwidget = QtWidgets.QWidget(WelcomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_Welcome.setGeometry(QtCore.QRect(40, 60, 721, 71))
        self.label_Welcome.setObjectName("label_Welcome")
        
        self.btn_RegisterStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_RegisterStudent.setGeometry(QtCore.QRect(220, 200, 331, 41))
        self.btn_RegisterStudent.setObjectName("btn_RegisterStudent")
        self.btn_RegisterStudent.clicked.connect(self.openRegistrationForm)

        WelcomePage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WelcomePage)
        self.statusbar.setObjectName("statusbar")
        WelcomePage.setStatusBar(self.statusbar)

        self.retranslateUi(WelcomePage)
        QtCore.QMetaObject.connectSlotsByName(WelcomePage)

    def retranslateUi(self, WelcomePage):
        _translate = QtCore.QCoreApplication.translate
        WelcomePage.setWindowTitle(_translate("WelcomePage", "Welcome to Mount Kenya University"))
        self.label_Welcome.setText(_translate("WelcomePage", "Welcome to Mount Kenya University Registration System"))
        self.btn_RegisterStudent.setText(_translate("WelcomePage", "Click Here To Register a Student"))

    def openRegistrationForm(self):
        self.registrationWindow = QtWidgets.QMainWindow()
        self.registrationForm = Ui_RegistrationForm()
        self.registrationForm.setupUi(self.registrationWindow)
        self.registrationWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomePage = QtWidgets.QMainWindow()
    ui = Ui_WelcomePage()
    ui.setupUi(WelcomePage)
    WelcomePage.show()
    sys.exit(app.exec_())
