# from PyQt5.QtWidgets import *
# import sys

# class Kafe_u_dili(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.layout = QVBoxLayout(self)

#         self.label_title = QLabel('kafeshka Dili 🍜')
#         self.layout.addWidget(self.label_title)

#         self.button1 = QPushButton("lagman")
#         self.layout.addWidget(self.button1)
#         self.button1.clicked.connect(self.lagmans_price)

#         self.button2 = QPushButton('shaurma')
#         self.layout.addWidget(self.button2)
#         self.button2.clicked.connect(self.shaurmas_price)
        
#         self.label_result=QLabel("")
#         self.layout.addWidget(self.label_result)


#         self.setWindowTitle("Kafe u Dili")
#         self.setFixedSize(300, 200)
#         self.show()

#     def lagmans_price(self):
#         self.label_result.setText('cena lagmana 5980 som 🍜')

#     def shaurmas_price(self):
#         self.label_result.setText('cena shaurmy 8900 som 🌯')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Kafe_u_dili()
#     app.exec_()





def longest_unique(s):
    current = ""
    longest = ""

    for ch in s:
        if ch in current:
            current = ch      # начинаем заново
        else:
            current += ch     # добавляем символ

        if len(current) > len(longest):
            longest = current

    return longest
def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0
    best_sub = ""

    for right in range(len(s)):
        # если символ уже есть — сдвигаем левую границу
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_sub = s[left:right + 1]

    return max_len, best_sub


print(longest_unique('cjdbsvosbdvsewdwiiifweoibgfevdiovw'))
print(longest_unique_substring('cjdbsvosbdvsewdwiiifweoibgfevdiovw'))