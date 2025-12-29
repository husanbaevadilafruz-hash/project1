import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel 
from PyQt5.QtGui import QFont 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ASIA")
        self.setGeometry

        label=QLabel('Hello', self)
        label.setFont(QFont('Arial', 20))
        label.setGeometry(0,0, 500, 100)
        label.setStyleSheet('color:blue;'
                             'background-color:black;'
                             'font-weight:bold;'
                             )
    

def main():
    app=QApplication([])
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
