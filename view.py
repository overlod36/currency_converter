from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, 
                             QMainWindow, QStyle, QVBoxLayout, QComboBox, 
                             QLineEdit, QHBoxLayout)
from PyQt6.QtCore import QSize, Qt

import conv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()
        
    def initialize(self):
        self.setWindowTitle("Конвертор валют")
        self.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DirHomeIcon))
        self.setFixedSize(QSize(300, 150))

        self.conv_button = QPushButton("Конвертация")
        self.conv_button.setCheckable(True)
        self.conv_button.clicked.connect(self.conv_button_clicked)
        self.conv_button.setFixedSize(100, 30)
        
        self.get_button = QPushButton("Обновить")
        self.get_button.clicked.connect(self.upd_button_clicked)

        self.about_button = QPushButton("Справка")
        self.get_button.setFixedSize(80, 30)
        self.about_button.setFixedSize(70, 30)
        
        self.currency_from = QComboBox()
        self.currency_from.addItems(conv.CURRENCIES)
        self.currency_from.setMaximumWidth(60)
        self.currency_from.setCurrentIndex(conv.get_currency_index('USD'))
        self.currency_from.currentTextChanged.connect( self.cf_choice )
        self.currency_from_choice = self.currency_from.currentText()

        self.currency_to = QComboBox()
        self.currency_to.addItems(conv.CURRENCIES.keys())
        self.currency_to.setMaximumWidth(60)
        self.currency_to.setCurrentIndex(conv.get_currency_index('RUB'))
        self.currency_to.currentTextChanged.connect( self.ct_choice )
        self.currency_to_choice = self.currency_to.currentText()

        self.input_from = QLineEdit()
        self.input_from.setMaximumWidth(100)

        self.input_to = QLineEdit()
        self.input_to.setMaximumWidth(100)
        self.input_to.setReadOnly(True)

        self.conv_from_layout= QHBoxLayout()
        self.conv_from_layout.addWidget(self.input_from)
        self.conv_from_layout.addWidget(self.currency_from)

        self.conv_to_layout = QHBoxLayout()
        self.conv_to_layout.addWidget(self.input_to)
        self.conv_to_layout.addWidget(self.currency_to)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.conv_button)
        self.buttons_layout.addWidget(self.get_button)
        self.buttons_layout.addWidget(self.about_button)

        self.main_layout= QVBoxLayout()
        self.main_layout.addLayout(self.conv_from_layout)
        self.main_layout.addLayout(self.conv_to_layout)
        self.main_layout.addLayout(self.buttons_layout)
        

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)

        self.setCentralWidget(self.widget)
        self.show()
    
    def cf_choice(self, s):
        self.currency_from_choice = s
    
    def ct_choice(self, s):
        self.currency_to_choice = s

    def conv_button_clicked(self):
        self.input_to.setText(f'{conv.convertation(self.currency_from_choice + self.currency_to_choice, self.input_from.text()):.3f}')
        
    def upd_button_clicked(self):
        pass

if __name__ == '__main__':

    conv.CURRENCIES = conv.fill_currencies()
    conv.set_session()

    app = QApplication([])
    window = MainWindow()
    app.exec()