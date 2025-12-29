import sys
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

API_URL = "http://127.0.0.1:5000"

class BankApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bank Client - PyQt5")
        self.setGeometry(300, 100, 600, 600)

        main_layout = QVBoxLayout()

        # ------------------------------
        # 1. Регистрация клиента
        # ------------------------------
        group_register = QGroupBox("Регистрация клиента")
        layout_r = QHBoxLayout()
        self.reg_name_input = QLineEdit()
        btn_reg = QPushButton("Добавить клиента")
        btn_reg.clicked.connect(self.add_client)
        layout_r.addWidget(self.reg_name_input)
        layout_r.addWidget(btn_reg)
        group_register.setLayout(layout_r)

        # ------------------------------
        # 2. Операции: пополнение / снятие
        # ------------------------------
        group_ops = QGroupBox("Операции со счетом")
        layout_ops = QGridLayout()

        self.ops_client = QComboBox()
        self.ops_currency = QComboBox()
        self.ops_currency.addItems(["usd", "kgs"])
        self.ops_amount = QLineEdit()

        btn_pop = QPushButton("Пополнить")
        btn_pop.clicked.connect(self.popolnenie)

        btn_snyatie = QPushButton("Снять")
        btn_snyatie.clicked.connect(self.snyatie)

        layout_ops.addWidget(QLabel("Клиент:"), 0, 0)
        layout_ops.addWidget(self.ops_client, 0, 1)
        layout_ops.addWidget(QLabel("Валюта:"), 1, 0)
        layout_ops.addWidget(self.ops_currency, 1, 1)
        layout_ops.addWidget(QLabel("Сумма:"), 2, 0)
        layout_ops.addWidget(self.ops_amount, 2, 1)
        layout_ops.addWidget(btn_pop, 3, 0)
        layout_ops.addWidget(btn_snyatie, 3, 1)

        group_ops.setLayout(layout_ops)

        # ------------------------------
        # 3. Конвертация валют
        # ------------------------------
        group_conv = QGroupBox("Конвертация валют")
        layout_conv = QGridLayout()

        self.conv_client = QComboBox()
        self.conv_from = QComboBox()
        self.conv_to = QComboBox()
        self.conv_from.addItems(["usd", "kgs"])
        self.conv_to.addItems(["usd", "kgs"])
        self.conv_amount = QLineEdit()

        btn_convert = QPushButton("Конвертировать")
        btn_convert.clicked.connect(self.convert_money)

        layout_conv.addWidget(QLabel("Клиент:"), 0, 0)
        layout_conv.addWidget(self.conv_client, 0, 1)
        layout_conv.addWidget(QLabel("Из:"), 1, 0)
        layout_conv.addWidget(self.conv_from, 1, 1)
        layout_conv.addWidget(QLabel("В:"), 2, 0)
        layout_conv.addWidget(self.conv_to, 2, 1)
        layout_conv.addWidget(QLabel("Сумма:"), 3, 0)
        layout_conv.addWidget(self.conv_amount, 3, 1)
        layout_conv.addWidget(btn_convert, 4, 0, 1, 2)

        group_conv.setLayout(layout_conv)

        # ------------------------------
        # 4. Установка курса валют
        # ------------------------------
        group_rate = QGroupBox("Установка курса валют")
        layout_rate = QHBoxLayout()

        self.rate_usd_to_kgs = QLineEdit()
        self.rate_kgs_to_usd = QLineEdit()
        btn_rate = QPushButton("Изменить курс")
        btn_rate.clicked.connect(self.update_rate)

        layout_rate.addWidget(QLabel("USD → KGS:"))
        layout_rate.addWidget(self.rate_usd_to_kgs)
        layout_rate.addWidget(QLabel("KGS → USD:"))
        layout_rate.addWidget(self.rate_kgs_to_usd)
        layout_rate.addWidget(btn_rate)

        group_rate.setLayout(layout_rate)

        # ------------------------------
        # 5. Показывать баланс
        # ------------------------------
        group_balance = QGroupBox("Баланс клиента")
        layout_bal = QVBoxLayout()

        self.balance_client = QComboBox()
        btn_balance = QPushButton("Показать баланс")
        btn_balance.clicked.connect(self.show_balance)

        self.balance_label = QLabel("Баланс будет здесь")

        layout_bal.addWidget(self.balance_client)
        layout_bal.addWidget(btn_balance)
        layout_bal.addWidget(self.balance_label)

        group_balance.setLayout(layout_bal)

        # ------------------------------
        # 6. Список клиентов
        # ------------------------------
        group_list = QGroupBox("Список клиентов")
        layout_list = QVBoxLayout()

        btn_list = QPushButton("Показать всех клиентов")
        btn_list.clicked.connect(self.show_all_clients)

        self.list_label = QLabel("Пока пусто")

        layout_list.addWidget(btn_list)
        layout_list.addWidget(self.list_label)

        group_list.setLayout(layout_list)

        # Добавление всех секций
        main_layout.addWidget(group_register)
        main_layout.addWidget(group_ops)
        main_layout.addWidget(group_conv)
        main_layout.addWidget(group_rate)
        main_layout.addWidget(group_balance)
        main_layout.addWidget(group_list)

        self.setLayout(main_layout)
        self.load_clients()

    # ------------------------------
    # Функции API
    # ------------------------------

    def add_client(self):
        name = self.reg_name_input.text()
        if not name:
            return
        requests.post(f"{API_URL}/add_customer", json={'name': name})
        self.load_clients()

    def popolnenie(self):
        client = self.ops_client.currentText()
        currency = self.ops_currency.currentText()
        amount = float(self.ops_amount.text())
        requests.post(f"{API_URL}/popolnenie", json={
            'customer': client,
            'currency': currency,
            'amount': amount
        })

    def snyatie(self):
        client = self.ops_client.currentText()
        currency = self.ops_currency.currentText()
        amount = float(self.ops_amount.text())
        requests.post(f"{API_URL}/snyatie", json={
            'name': client,
            'currency': currency,
            'amount': amount
        })

    def convert_money(self):
        client = self.conv_client.currentText()
        f = self.conv_from.currentText()
        t = self.conv_to.currentText()
        amount = float(self.conv_amount.text())
        requests.post(f"{API_URL}/convert", json={
            'name': client,
            'from': f,
            'to': t,
            'amount': amount
        })

    def update_rate(self):
        usd_kgs = float(self.rate_usd_to_kgs.text())
        kgs_usd = float(self.rate_kgs_to_usd.text())
        requests.post(f"{API_URL}/set_rate", json={
            'usd_to_kgs': usd_kgs,
            'kgs_to_usd': kgs_usd
        })

    def show_balance(self):
        name = self.balance_client.currentText()
        r = requests.get(f"{API_URL}/zapros", json={'name': name})
        data = r.json()
        self.balance_label.setText(f"USD: {data['balanceUSD']} | KGS: {data['balanceKGS']}")

    def show_all_clients(self):
        r = requests.get(f"{API_URL}/all_customers")
        data = r.json()
        self.list_label.setText(", ".join(data['customers']))

    def load_clients(self):
        r = requests.get(f"{API_URL}/all_customers")
        if r.status_code != 200:
            return
        clients = r.json().get('customers', [])

        self.ops_client.clear()
        self.conv_client.clear()
        self.balance_client.clear()

        self.ops_client.addItems(clients)
        self.conv_client.addItems(clients)
        self.balance_client.addItems(clients)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BankApp()
    win.show()
    sys.exit(app.exec_())
