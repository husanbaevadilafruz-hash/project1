from collections import defaultdict

class Item:
    def __init__(self, strihkod, name, purchase_price, sale_price):
        self.strihkod=strihkod
        self.name=name 
        self.purchase_price=purchase_price
        self.sale_price=sale_price
        
    def set_price(self, new_price):
        self.sale_price=new_price 
    def __str__(self):
        return f'Item({self.strihkod}, {self.name}, purchase={self.purchase_price}, sale={self.sale_price})'
    
mandarin=Item(8989088,'mandarin', 90, 99)

print(mandarin.strihkod)   
print(mandarin.name)