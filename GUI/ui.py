from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

GLOBAL_STATE = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 380)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 500, 380))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border-radius: 15px;\n"
"	background-color: rgb(15, 15, 15);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_Title = QLabel(self.frame)
        self.label_Title.setObjectName(u"label_Title")
        self.label_Title.setGeometry(QRect(0, 0, 500, 75))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_Title.setFont(font)
        self.label_Title.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"} ")
        self.label_Title.setFrameShape(QFrame.NoFrame)
        self.label_Title.setFrameShadow(QFrame.Plain)
        self.label_Title.setLineWidth(5)
        self.label_Title.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_Length = QSlider(self.frame)
        self.horizontalSlider_Length.setObjectName(u"horizontalSlider_Length")
        self.horizontalSlider_Length.setGeometry(QRect(50, 200, 150, 30))
        self.horizontalSlider_Length.setStyleSheet(u"QSlider::groove {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(50, 60, 70);\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}")
        self.horizontalSlider_Length.setOrientation(Qt.Horizontal)
        self.horizontalSlider_Length.setMinimum(1)
        self.horizontalSlider_Length.setMaximum(64)
        self.horizontalSlider_Length.setSingleStep(1)
        self.horizontalSlider_Length.setValue(8)
        
        self.checkBox_Uppercase = QCheckBox(self.frame)
        self.checkBox_Uppercase.setObjectName(u"checkBox_Uppercase")
        self.checkBox_Uppercase.setGeometry(QRect(300, 135, 150, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.checkBox_Uppercase.setFont(font1)
        self.checkBox_Uppercase.setStyleSheet(u"QCheckBox{\n"
"	color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(189, 147, 249);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}")
        self.checkBox_Uppercase.setChecked(True)
        self.checkBox_Uppercase.setAutoExclusive(False)
        self.checkBox_Uppercase.setTristate(False)
        self.checkBox_Lowercase = QCheckBox(self.frame)
        self.checkBox_Lowercase.setObjectName(u"checkBox_Lowercase")
        self.checkBox_Lowercase.setGeometry(QRect(300, 170, 150, 30))
        self.checkBox_Lowercase.setFont(font1)
        self.checkBox_Lowercase.setStyleSheet(u"QCheckBox{\n"
"	color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(189, 147, 249);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}")
        self.label_Length = QLabel(self.frame)
        self.label_Length.setObjectName(u"label_Length")
        self.label_Length.setGeometry(QRect(50, 135, 150, 30))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        self.label_Length.setFont(font3)
        self.label_Length.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_Length.setAlignment(Qt.AlignCenter)
        self.checkBox_Lowercase.setChecked(True)
        self.checkBox_Lowercase.setAutoExclusive(False)
        self.checkBox_Lowercase.setTristate(False)
        self.checkBox_Numbers = QCheckBox(self.frame)
        self.checkBox_Numbers.setObjectName(u"checkBox_Numbers")
        self.checkBox_Numbers.setGeometry(QRect(300, 205, 150, 30))
        self.checkBox_Numbers.setFont(font1)
        self.checkBox_Numbers.setStyleSheet(u"QCheckBox{\n"
"	color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(189, 147, 249);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}")
        self.checkBox_Numbers.setChecked(True)
        self.checkBox_Numbers.setAutoExclusive(False)
        self.checkBox_Numbers.setTristate(False)
        self.checkBox_Symbols = QCheckBox(self.frame)
        self.checkBox_Symbols.setObjectName(u"checkBox_Symbols")
        self.checkBox_Symbols.setGeometry(QRect(300, 240, 150, 30))
        self.checkBox_Symbols.setFont(font1)
        self.checkBox_Symbols.setStyleSheet(u"QCheckBox{\n"
"	color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(189, 147, 249);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}")
        self.checkBox_Symbols.setChecked(True)
        self.checkBox_Symbols.setAutoExclusive(False)
        self.checkBox_Symbols.setTristate(False)
        self.pushButton_Generate = QPushButton(self.frame)
        self.pushButton_Generate.setObjectName(u"pushButton_Generate")
        self.pushButton_Generate.setGeometry(QRect(185, 300, 130, 50))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_Generate.setFont(font2)
        self.pushButton_Generate.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 25px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
" QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(249, 136, 2, 135))
        self.line.setStyleSheet(u"Line{\n"
"	background-color: rgb(189, 147, 249);\n"
"	border-radius: 1px;\n"
"}")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lineEdit_Password = QLineEdit(self.frame)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        self.lineEdit_Password.setGeometry(QRect(100, 75, 300, 30))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setFamily(u"Arial")
        self.lineEdit_Password.setFont(font4)
        self.lineEdit_Password.setStyleSheet(u"QLineEdit {\n"
"	color: white;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_Password.setAlignment(Qt.AlignCenter)
        self.lineEdit_Password.setDragEnabled(False)
        self.lineEdit_Password.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.pushButton_Close = QPushButton(self.frame)
        self.pushButton_Close.setObjectName(u"pushButton_Close")
        self.pushButton_Close.setGeometry(QRect(470, 15, 14, 14))
        self.pushButton_Close.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255,0,0);\n"
"}")
        self.pushButton_Maximize = QPushButton(self.frame)
        self.pushButton_Maximize.setObjectName(u"pushButton_Maximize")
        self.pushButton_Maximize.setGeometry(QRect(445, 15, 14, 14))
        self.pushButton_Maximize.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
"	background-color: rgb(0,255,0);\n"
"}")
        self.pushButton_Minimize = QPushButton(self.frame)
        self.pushButton_Minimize.setObjectName(u"pushButton_Minimize")
        self.pushButton_Minimize.setGeometry(QRect(420, 15, 14, 14))
        self.pushButton_Minimize.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255,255,0);\n"
"}")
        self.lineEdit_Length_Number = QLineEdit(self.frame)
        self.lineEdit_Length_Number.setObjectName(u"lineEdit_Length_Number")
        self.lineEdit_Length_Number.setGeometry(QRect(75, 170, 100, 30))
        self.lineEdit_Length_Number.setFont(font2)
        self.lineEdit_Length_Number.setStyleSheet(u"QLineEdit {\n"
"	color: white;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_Length_Number.setAlignment(Qt.AlignCenter)
        self.lineEdit_Length_Number.setMaxLength(5)
        self.lineEdit_Length_Number.setText('8')
        self.lineEdit_Length_Number.setReadOnly(True)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Title.setText(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.checkBox_Uppercase.setText(QCoreApplication.translate("MainWindow", u"Uppercase", None))
        self.checkBox_Lowercase.setText(QCoreApplication.translate("MainWindow", u"Lowercase", None))
        self.checkBox_Numbers.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.checkBox_Symbols.setText(QCoreApplication.translate("MainWindow", u"Symbols", None))
        self.pushButton_Generate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.lineEdit_Length_Number.setPlaceholderText("")
        self.label_Length.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.lineEdit_Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_Close.setText("")
        self.pushButton_Maximize.setText("")
        self.pushButton_Minimize.setText("")
    # retranslateUi

    def return_Status():
        return GLOBAL_STATE