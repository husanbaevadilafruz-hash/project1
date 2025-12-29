# client.py
from PyQt5.QtWidgets import *
import sys
import requests

class SalonUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Salon Diliachki')
        self.setGeometry(400, 300, 360, 420)
        self.url = "http://127.0.0.1:5000"

        layout = QVBoxLayout()

        # ---- Добавление клиента ----
        layout.addWidget(QLabel("Добавить клиента:"))
        self.add_client_text = QLineEdit()
        self.add_client_text.setPlaceholderText('введите имя клиента')
        self.addClient_btn = QPushButton('Добавить клиента')
        layout.addWidget(self.add_client_text)
        layout.addWidget(self.addClient_btn)

        # ---- ComboBox клиентов и мастеров ----
        layout.addWidget(QLabel("Выберите клиента:"))
        self.clients_combo = QComboBox()
        layout.addWidget(self.clients_combo)

        layout.addWidget(QLabel("Выберите мастера:"))
        self.masters_combo = QComboBox()
        layout.addWidget(self.masters_combo)

        # ---- Кнопки брони ----
        self.book_mesto_btn = QPushButton('Забронировать место (без ожидания)')
        self.book_mesto_wait_btn = QPushButton('Забронировать место (встать в очередь)')
        layout.addWidget(self.book_mesto_btn)
        layout.addWidget(self.book_mesto_wait_btn)

        # ---- Показ списков ----
        self.list_clients_btn = QPushButton('Показать список клиентов')
        self.list_masters_btn = QPushButton('Показать состояние мастеров')
        layout.addWidget(self.list_clients_btn)
        layout.addWidget(self.list_masters_btn)

        # ---- Finish master (освободить / переключить) ----
        layout.addWidget(QLabel("Имя мастера для finish:"))
        self.osvMastera = QLineEdit()
        self.osvMastera.setPlaceholderText('введите имя мастера')
        self.finish_master_btn = QPushButton('Finish master (следующий / свободен)')
        layout.addWidget(self.osvMastera)
        layout.addWidget(self.finish_master_btn)

        # ---- Вывод ----
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

        # Подключаем кнопки
        self.addClient_btn.clicked.connect(self.add_client)
        self.book_mesto_btn.clicked.connect(self.book_mesto)
        self.book_mesto_wait_btn.clicked.connect(self.book_mesto_wait)
        self.list_clients_btn.clicked.connect(self.show_clients)
        self.list_masters_btn.clicked.connect(self.show_masters)
        self.finish_master_btn.clicked.connect(self.finish_master)

        # внутренние данные мастеров (словарь от сервера)
        self.masters_data = {}

        # начальное заполнение
        self.refresh_clients()
        self.refresh_masters()

    # ---- network helpers ----
    def safe_get(self, path):
        try:
            r = requests.get(self.url + path, timeout=3)
            return r
        except Exception as e:
            self.output.append(f"Ошибка сети: {e}")
            return None

    def safe_post(self, path, json_data):
        try:
            r = requests.post(self.url + path, json=json_data, timeout=3)
            return r
        except Exception as e:
            self.output.append(f"Ошибка сети: {e}")
            return None

    # ---- refresh ----
    def refresh_clients(self):
        r = self.safe_get('/get_clients')
        if r and r.status_code == 200:
            clients = r.json().get('result', [])
            self.clients_combo.clear()
            if clients:
                self.clients_combo.addItems(clients)

    def refresh_masters(self):
        r = self.safe_get('/get_masters')
        if r and r.status_code == 200:
            masters = r.json().get('result', {})
            self.masters_data = masters  # сохраняем всю информацию (available, current, queue)
            self.masters_combo.clear()
            if masters:
                # показываем имена мастеров в комбобоксе (имя — всегда присутствует)
                self.masters_combo.addItems(list(masters.keys()))

    # ---- actions ----
    def add_client(self):
        name = self.add_client_text.text().strip()
        if not name:
            self.output.append("Введите имя клиента")
            return
        r = self.safe_post('/add_client', {'name': name})
        if r and r.status_code == 200:
            self.output.append(r.json().get('result', 'No result'))
            self.add_client_text.clear()
            self.refresh_clients()

    def book_mesto(self):
        client = self.clients_combo.currentText()
        master = self.masters_combo.currentText()
        if not client or not master:
            self.output.append("Выберите клиента и мастера")
            return
        r = self.safe_post('/book_mesto', {'client_name': client, 'master_name': master, 'wait': False})
        if r and r.status_code == 200:
            self.output.append(r.json().get('result', 'No result'))
            self.refresh_masters()

    def book_mesto_wait(self):
        client = self.clients_combo.currentText()
        master = self.masters_combo.currentText()
        if not client or not master:
            self.output.append("Выберите клиента и мастера")
            return
        r = self.safe_post('/book_mesto', {'client_name': client, 'master_name': master, 'wait': True})
        if r and r.status_code == 200:
            self.output.append(r.json().get('result', 'No result'))
            self.refresh_masters()

    def show_clients(self):
        r = self.safe_get('/get_clients')
        if r and r.status_code == 200:
            self.output.append("Клиенты: " + str(r.json().get('result', [])))

    def show_masters(self):
        r = self.safe_get('/get_masters')
        if r and r.status_code == 200:
            masters = r.json().get('result', {})
            # красивый вывод статусов мастеров
            lines = []
            for name, info in masters.items():
                avail = 'свободен' if info['available'] else f'занят ({info["current"]})'
                q = info.get('queue', [])
                lines.append(f"{name}: {avail}; очередь: {q}")
            self.output.append('\n'.join(lines))

    def finish_master(self):
        master_name = self.osvMastera.text().strip()
        if not master_name:
            self.output.append("Введите имя мастера для finish")
            return
        r = self.safe_post('/finish_master', {'master_name': master_name})
        if r and r.status_code == 200:
            self.output.append(r.json().get('result', 'No result'))
            self.refresh_masters()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SalonUI()
    window.show()
    sys.exit(app.exec_())
