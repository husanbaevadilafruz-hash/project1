from PyQt5.QtWidgets import *
import sys
import requests

class Chatic(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WhatsApp guys')
        self.setGeometry(400, 300, 360, 420)
        self.url = "http://127.0.0.1:5000"
        layout=QVBoxLayout()
        self.online_now=QLineEdit('vvedite ima')
        layout.addWidget(self.online_now)
        self.polzovateli=QComboBox()
        layout.addWidget(self.polzovateli)
        self.sms=QLineEdit('vvedite sms')
        layout.addWidget(self.sms)
        self.send_btn=QPushButton('send')
        layout.addWidget(self.send_btn)
        self.vhodashie=QTextEdit()
        layout.addWidget(self.vhodashie)
        self.setLayout(layout)
        self.refresh_users()
        self.send_btn.clicked.connect(self.send_sms)
    def refresh_clients(self):
        name=self.online_now.text()
        sms=self.sms.text()
        to_client=self.polzovateli.currentText()
        r=requests.get(self.url['/list_of_clients'])
        users = r.json().get('result', {})
         
        self.polzovateli.clear()
        self.polzovateli.addItems(users)
    
    def send_message(self):
        name=self.online_now.text()
        sms=self.sms.text()
        to_client=self.polzovateli.currentText()
        if name==to_client:
            self.vhodashie.append(sms)
            
        
          

        