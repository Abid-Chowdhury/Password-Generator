import sys

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
        
        # clicker events
        self.UIMainwindow.pushButton_Close.clicked.connect(lambda: self.close())
        self.UIMainwindow.pushButton_Minimize.clicked.connect(lambda: self.showMinimized())
        self.UIMainwindow.pushButton_Generate.clicked.connect(lambda: UIFunctions.generate_Password(self, self.UIMainwindow.checkBox_Numbers.isChecked(), self.UIMainwindow.checkBox_Symbols.isChecked(), self.UIMainwindow.checkBox_Uppercase.isChecked(), self.UIMainwindow.checkBox_Lowercase.isChecked()))
        self.UIMainwindow.horizontalSlider_Length.valueChanged.connect(lambda: UIFunctions.update_Length(self))

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
