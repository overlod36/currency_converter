from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, 
                             QMainWindow, QStyle, QVBoxLayout, QComboBox, QLineEdit)
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize()
        
    def initialize(self):
        self.setWindowTitle("Конвертор валют")
        self.setWindowIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_DirHomeIcon))
        self.setFixedSize(QSize(400, 300))

        self.conv_button = QPushButton("Конвертация")
        self.conv_button.setCheckable(True)
        self.conv_button.clicked.connect(self.button_clicked)
        
        self.get_button = QPushButton("Обновить")
        self.about_button = QPushButton("Справка")

        
        self.currency_from = QComboBox()
        self.currency_from.addItems(['1','2','3'])
        self.currency_from.currentTextChanged.connect( self.cf_choice )
        self.currency_from_choice = self.currency_from.currentText()
        self.currency_to = QComboBox()
        self.input_from = QLineEdit()
        self.input_to = QLineEdit()

        self.main_layout= QVBoxLayout()
        self.main_layout.addWidget(self.currency_from)
        self.main_layout.addWidget(self.input_from)
        self.main_layout.addWidget(self.currency_to)
        self.main_layout.addWidget(self.input_to)
        self.main_layout.addWidget(self.conv_button)
        self.main_layout.addWidget(self.get_button)
        self.main_layout.addWidget(self.about_button)

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)

        self.setCentralWidget(self.widget)
        self.show()
    
    def cf_choice(self, s):
        self.currency_from_choice = s

    def button_clicked(self):
        print(self.currency_from_choice)


app = QApplication([])

window = MainWindow()

app.exec()