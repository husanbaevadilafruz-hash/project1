from PyQt5.QtWidgets import *
from bank_opp import BankUI  # Import backend
import sys
import requests

#    VIEW-PYQT5 ГРАФИЧЕСКИЙ КЛИЕНТ

# Элементы управления(все кнопки запрашивают соответствующие эндпоинты)
#    .управления клиентами: поле ввода имени и кнопка регистрации нового клиента
#    .операций: выпадающий список (combobox) клиентов, ввода суммы, валюты, кнопки, пополнения и снятия
#    .конвертация: выпадающий список клиентов, выпадающий список валюты, поле ввода суммы (client, from currency, to currency, amount), и кнопка, которая делает конвертацию одной валюты на другую
#    .курса валют: поле ввода нового курса и кнопка применения изменений
#    .отображения: выпадающий список клиентов, кнопка запуска актуального баланса, текстовые метки с результатами для выбранного клиента
#    .список клиентов: кнопка и текстовые метки 

class Banking(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bank')
        self.setgeometry(400,300,400,300)

        layout=QVBoxLayout()
        self.funktion=QLabel('dobavlenie klienta')
        layout.addWidget(self.funktion)
        self.add=QLabel('vvedite ima klienta')
        self.new_klient=QLineEdit()
        layout.addWidget(self.add)
        layout.addWidget(self.new_klient)
        self.addButton=QPushButton('add klient')
        layout.addWidget(self.addButton)
        self.funktion2=QLabel('popolnenie shcheta klienta')
        layout.addWidget(self.funktion2)

        self.klients=QComboBox('klients')
        layout.addWidget(self.klients)
        self.currency=QLineEdit()
        layout.addWidget(self.currency)
        self.amount=QLineEdit()
        layout.addWidget(self.amount)
        self.popolnenie_btn=QPushButton('popolnit')
        self.funktion3=QLabel('konvertacia')
        layout.addWidget(self.funktion3)
        self.klients=QComboBox('klients')
        layout.addWidget(self.klients)
        self.from_currency=QComboBox('from_currency')
        layout.addWidget(self.from_currency)
        self.to_currency=QComboBox('to_currency')
        layout.addWidget(self.to_currency)
        self.text=QLabel('vvedine summu')
        layout.addWidget(self.text)
        self.amount=QLineEdit()
        layout.addWidget(self.amount)
        self.transfer=QPushButton('transfer')
        layout.addWidget(self.transfer)
        self.refresh_clients()
    def refresh_clients(self):
        r=requests.get(self.url+'/all')
        
        





        