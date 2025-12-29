from PyQt5.QtWidgets import *
import sys

class ButtonBook(QWidget):
    def __init__(self, books_name, avtor, janr):
        super().__init__()
        self.setWindowTitle(books_name)
        self.setFixedSize(300, 200)

        layout = QVBoxLayout(self)
        label = QLabel(f'Книга: {books_name}\nАвтор: {avtor}\nЖанр: {janr}')
        layout.addWidget(label)

        self.show()

class Biblioteka(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Библиотека Дили')
        self.setFixedSize(300, 400)

        self.layout = QVBoxLayout(self)
        self.label = QLabel('Добро пожаловать в библиотеку!')
        self.layout.addWidget(self.label)

        # Кнопки книг
        button1 = QPushButton('Harry Potter')
        button1.clicked.connect(self.harry_info)
        self.layout.addWidget(button1)

        button2 = QPushButton('Hobbit')
        button2.clicked.connect(self.hobbit_info)
        self.layout.addWidget(button2)

        button3 = QPushButton('Vlastelin kolec')
        button3.clicked.connect(self.vlastelin_kolec)
        self.layout.addWidget(button3)

    # --- Методы для кнопок ---
    def harry_info(self):
        self.book_window = ButtonBook('Harry Potter', 'Joan Rowling', 'Fantasy')

    def hobbit_info(self):
        self.book_window = ButtonBook('Hobbit', 'J. R. R. Tolkien', 'Fantasy')

    def vlastelin_kolec(self):
        self.book_window = ButtonBook('Vlastelin kolec', 'J. R. R. Tolkien', 'Epic fantasy')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Biblioteka()
    window.show()
    sys.exit(app.exec_())
