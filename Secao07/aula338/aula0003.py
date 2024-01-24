# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')
# botao.show()

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')
# botao2.show()

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')
# botao2.show()

central_widget = QWidget()

# layout = QVBoxLayout()
# layout = QHBoxLayout()
layout = QGridLayout()
central_widget.setLayout(layout)

# layout.addWidget(botao)
# layout.addWidget(botao2)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2)

central_widget.show()  #Central widget entre

app.exec()  #O loop da aplicação