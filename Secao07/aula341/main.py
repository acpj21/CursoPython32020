import sys
import time

from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_myWidget


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.Button1.clicked.connect(self.hardWork1)
        self.Button2.clicked.connect(self.hardWork2)
    
    def hardWork1(self):
        time.sleep(5)
        self.label1.setText('hardWorkd1 terminado')
    
    def hardWork2(self):
        time.sleep(5)
        self.label2.setText('2 terminado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()