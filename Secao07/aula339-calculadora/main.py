import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
# from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # label1 = QLabel('O meu texto')
    # label1.setStyleSheet('font-size: 150px;')
    # window.v_layout.addWidget(label1)
    # window.adjustFixedSize()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Buton


    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()