import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from functions import *
from ui import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UIMainwindow = Ui_MainWindow()
        self.UIMainwindow.setupUi(self)
        
        # make the window rouneded & removes background
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # functions
        self.UIMainwindow.pushButton_Close.clicked.connect(lambda: self.close())
        self.UIMainwindow.pushButton_Minimize.clicked.connect(lambda: self.showMinimized())
        self.UIMainwindow.pushButton_Generate.clicked.connect(lambda: UIFunctions.generate_Password(self, 5, self.UIMainwindow.checkBox_Numbers.isChecked(), self.UIMainwindow.checkBox_Symbols.isChecked(), self.UIMainwindow.checkBox_Uppercase.isChecked(), self.UIMainwindow.checkBox_Lowercase.isChecked()))
        
        # move window
        def move_Window(event):
            if Ui_MainWindow.return_Status() == 1:
                Ui_MainWindow.maximize_Restore(self)
        
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        
        self.UIMainwindow.label_Title.mouseMoveEvent = move_Window
                
        self.show()
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())