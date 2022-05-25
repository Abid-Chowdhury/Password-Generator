import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from password_Generator_GUI import *
from ui import *

class UIFunctions(MainWindow):
    
    def generate_Password(self, length, include_Numbers, include_Symbols, include_Uppercase, include_Lowercase):
        print(length, include_Numbers, include_Symbols, include_Uppercase, include_Lowercase)