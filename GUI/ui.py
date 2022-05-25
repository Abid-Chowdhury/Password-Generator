# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designkemhaM.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


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
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 500, 75))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"} ")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(5)
        self.label.setAlignment(Qt.AlignCenter)
        self.horizontalSlider = QSlider(self.frame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(50, 200, 150, 30))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove {\n"
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
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(300, 135, 150, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.checkBox_4.setFont(font1)
        self.checkBox_4.setStyleSheet(u"QCheckBox{\n"
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
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setAutoExclusive(False)
        self.checkBox_4.setTristate(False)
        self.checkBox_5 = QCheckBox(self.frame)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(300, 170, 150, 30))
        self.checkBox_5.setFont(font1)
        self.checkBox_5.setStyleSheet(u"QCheckBox{\n"
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
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setAutoExclusive(False)
        self.checkBox_5.setTristate(False)
        self.checkBox_6 = QCheckBox(self.frame)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(300, 205, 150, 30))
        self.checkBox_6.setFont(font1)
        self.checkBox_6.setStyleSheet(u"QCheckBox{\n"
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
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setAutoExclusive(False)
        self.checkBox_6.setTristate(False)
        self.checkBox_7 = QCheckBox(self.frame)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(300, 240, 150, 30))
        self.checkBox_7.setFont(font1)
        self.checkBox_7.setStyleSheet(u"QCheckBox{\n"
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
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setAutoExclusive(False)
        self.checkBox_7.setTristate(False)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(185, 300, 130, 50))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 135, 150, 30))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 170, 150, 30))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 75, 300, 30))
        font4 = QFont()
        font4.setPointSize(12)
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 15, 14, 14))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255,0,0);\n"
"}")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(445, 15, 14, 14))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
"	background-color: rgb(0,255,0);\n"
"}")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(420, 15, 14, 14))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255,255,0);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Uppercase", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Lowercase", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Symbols", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

