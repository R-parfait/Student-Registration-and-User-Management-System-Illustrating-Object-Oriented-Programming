from PyQt5 import QtCore, QtGui, QtWidgets
from database import Db, RegistrationDb

class Ui_RegistrationForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("QLineEdit{\n"
            "background-color:rgb(173,216,230)\n"
            "}\n"
            "QLabel#label_Heading{\n"
            "font: 75 25pt \"Century Schoolbook L\";\n"
            "}\n"
            "QLabel{\n"
            "font: 75 italic 14pt \"Century Schoolbook L\";\n"
            "}\n"
            "QPushButton{\n"
            "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 255, 255, 147));\n"
            "color:rgb(255,255,255);\n"  # white text color
            "background-color:rgb(11, 110, 150); \n"  
            "border-radius: 5px;\n"
            "}\n"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_Heading = QtWidgets.QLabel(self.centralwidget)
        self.label_Heading.setGeometry(QtCore.QRect(40, 30, 721, 71))
        self.label_Heading.setObjectName("label_Heading")

        self.label_FirstName = QtWidgets.QLabel(self.centralwidget)
        self.label_FirstName.setGeometry(QtCore.QRect(40, 120, 181, 31))
        self.label_FirstName.setObjectName("label_FirstName")

        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_FirstName.setGeometry(QtCore.QRect(220, 120, 311, 31))
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")

        self.label_LastName = QtWidgets.QLabel(self.centralwidget)
        self.label_LastName.setGeometry(QtCore.QRect(40, 160, 181, 31))
        self.label_LastName.setObjectName("label_LastName")

        self.lineEdit_LastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_LastName.setGeometry(QtCore.QRect(220, 160, 311, 31))
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")

        self.label_DateOfBirth = QtWidgets.QLabel(self.centralwidget)
        self.label_DateOfBirth.setGeometry(QtCore.QRect(40, 200, 181, 31))
        self.label_DateOfBirth.setObjectName("label_DateOfBirth")

        self.dateEdit_DateOfBirth = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_DateOfBirth.setGeometry(QtCore.QRect(220, 200, 311, 31))
        self.dateEdit_DateOfBirth.setObjectName("dateEdit_DateOfBirth")
        self.dateEdit_DateOfBirth.setCalendarPopup(True)
        
        self.label_PlaceOfBirth = QtWidgets.QLabel(self.centralwidget)
        self.label_PlaceOfBirth.setGeometry(QtCore.QRect(40, 240, 181, 31))
        self.label_PlaceOfBirth.setObjectName("label_PlaceOfBirth")

        self.lineEdit_PlaceOfBirth = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PlaceOfBirth.setGeometry(QtCore.QRect(220, 240, 311, 31))
        self.lineEdit_PlaceOfBirth.setObjectName("lineEdit_PlaceOfBirth")

        self.label_Country = QtWidgets.QLabel(self.centralwidget)
        self.label_Country.setGeometry(QtCore.QRect(40, 280, 181, 31))
        self.label_Country.setObjectName("label_Country")

        self.lineEdit_Country = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Country.setGeometry(QtCore.QRect(220, 280, 311, 31))
        self.lineEdit_Country.setObjectName("lineEdit_Country")

      
        self.label_CourseAppliedFor = QtWidgets.QLabel(self.centralwidget)
        self.label_CourseAppliedFor.setGeometry(QtCore.QRect(40, 320, 181, 31))
        self.label_CourseAppliedFor.setObjectName("label_CourseAppliedFor")

        self.lineEdit_CourseAppliedFor = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_CourseAppliedFor.setGeometry(QtCore.QRect(220, 320, 311, 31))
        self.lineEdit_CourseAppliedFor.setObjectName("lineEdit_CourseAppliedFor")

        self.label_FathersName = QtWidgets.QLabel(self.centralwidget)
        self.label_FathersName.setGeometry(QtCore.QRect(40, 360, 181, 31))
        self.label_FathersName.setObjectName("label_FathersName")

        self.lineEdit_FathersName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_FathersName.setGeometry(QtCore.QRect(220, 360, 311, 31))
        self.lineEdit_FathersName.setObjectName("lineEdit_FathersName")

        self.label_MothersName = QtWidgets.QLabel(self.centralwidget)
        self.label_MothersName.setGeometry(QtCore.QRect(40, 400, 181, 31))
        self.label_MothersName.setObjectName("label_MothersName")

        self.lineEdit_MothersName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_MothersName.setGeometry(QtCore.QRect(220, 400, 311, 31))
        self.lineEdit_MothersName.setObjectName("lineEdit_MothersName")

        self.label_MeanGrade = QtWidgets.QLabel(self.centralwidget)
        self.label_MeanGrade.setGeometry(QtCore.QRect(40, 440, 181, 31))
        self.label_MeanGrade.setObjectName("label_MeanGrade")

        self.lineEdit_MeanGrade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_MeanGrade.setGeometry(QtCore.QRect(220, 440, 311, 31))
        self.lineEdit_MeanGrade.setObjectName("lineEdit_MeanGrade")

        # More fields can be added here

        self.btn_Register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Register.setGeometry(QtCore.QRect(220, 520, 131, 41))
        self.btn_Register.setObjectName("btn_Register")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_Register.clicked.connect(self.registerStudent)  # Connect the button to the registration function

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def registerStudent(self):
        name = self.lineEdit_FirstName.text()
        last_name = self.lineEdit_LastName.text()
        dob = self.dateEdit_DateOfBirth.date().toString(QtCore.Qt.ISODate)
        place_of_birth = self.lineEdit_PlaceOfBirth.text()
        country = self.lineEdit_Country.text()
        course_applied = self.lineEdit_CourseAppliedFor.text()
        father_name = self.lineEdit_FathersName.text()
        mother_name = self.lineEdit_MothersName.text()
        mean_grade = int(self.lineEdit_MeanGrade.text())

        # Create an instance of the RegistrationDb class
        reg_db = RegistrationDb()

        # Insert the data into the registration database
        data = (name, last_name, dob, place_of_birth, country, course_applied, father_name, mother_name, mean_grade)
        reg_db.insertRegistrationFormsTable(data)

        self.showMessage("Success", "Student registered successfully")

    def showMessage(self, title, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mount Kenya University Student Registration"))
        self.label_Heading.setText(_translate("MainWindow", "Student Application Form"))
        self.label_FirstName.setText(_translate("MainWindow", "First Name:"))
        self.label_LastName.setText(_translate("MainWindow", "Last Name:"))
        self.label_DateOfBirth.setText(_translate("MainWindow", "Date of Birth:"))
        self.label_PlaceOfBirth.setText(_translate("Mainwindow", "Place of Birth"))
        self.label_Country.setText(_translate("Mainwindow", "Country"))
        self.label_CourseAppliedFor.setText(_translate("Mainwindow", "Course Applied For"))
        self.label_FathersName.setText(_translate("Mainwindow", "Father's Name"))
        self.label_MothersName.setText(_translate("Mainwindow", "Mother's Name"))
        self.label_MeanGrade.setText(_translate("Mainwindow", "Mean Grade"))
        # More labels can be added similarly
        self.btn_Register.setText(_translate("MainWindow", "Register"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistrationForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
