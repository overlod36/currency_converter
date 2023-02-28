from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Конвертор валют")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)

        self.setFixedSize(QSize(400, 300))

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)
    
    def button_clicked(self):
        print(1)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()