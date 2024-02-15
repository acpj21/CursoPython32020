import sys
import time

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_myWidget


class Workder1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.Button1.clicked.connect(self.hardWork1)
        self.Button2.clicked.connect(self.hardWork2)
    
    def hardWork1(self):
        self.label1.setText('hardWorkd1 terminado')
    
    def hardWork2(self):
        time.sleep(5)
        self.label2.setText('2 terminado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()