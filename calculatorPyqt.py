from PyQt5.QtWidgets import *
import requests
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(400, 300, 200, 400)

        self.url = "http://127.0.0.1:5000/reshenie"

        layout=QVBoxLayout()

        self.x = QLineEdit()
        self.x.setPlaceholderText('Введите первое число')
        layout.addWidget(self.x)

        self.plus = QPushButton('+')
        layout.addWidget(self.plus)

        self.minus = QPushButton('-')
        layout.addWidget(self.minus)

        self.multi = QPushButton('*')
        layout.addWidget(self.multi)

        self.devide = QPushButton('/')
        layout.addWidget(self.devide)

        self.y = QLineEdit()
        self.y.setPlaceholderText('Введите второе число')
        layout.addWidget(self.y)

        # связка кнопок
        self.plus.clicked.connect(self.slojenie)
        self.minus.clicked.connect(self.vychit)
        self.multi.clicked.connect(self.umnoj)
        self.devide.clicked.connect(self.delenie)

        self.output = QTextEdit()
        layout.addWidget(self.output)

        self.setLayout(layout)

    def slojenie(self):
        x = int(self.x.text())
        y = int(self.y.text())
        r = requests.post(self.url, json={'x': x, 'y': y, 'deistvie': 'plus'})
        self.output.append(str(r.json().get('otvet')))

    def vychit(self):
        x = int(self.x.text())
        y = int(self.y.text())
        r = requests.post(self.url, json={'x': x, 'y': y, 'deistvie': 'minus'})
        self.output.append(str(r.json().get('otvet')))

    def umnoj(self):
        x = int(self.x.text())
        y = int(self.y.text())
        r = requests.post(self.url, json={'x': x, 'y': y, 'deistvie': 'umnojenie'})
        self.output.append(str(r.json().get('otvet')))

    def delenie(self):
        x = int(self.x.text())
        y = int(self.y.text())
        r = requests.post(self.url, json={'x': x, 'y': y, 'deistvie': 'delenie'})
        self.output.append(str(r.json().get('otvet')))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
