class User():
    def __init__(self, id, name, email, cart):
        self.id=id
        self.name=name
        self.email=email
        self.cart=cart 
        self.favorites=[]
        self.orders=[]
        self.inbox=[]
    def add_to_favorites(self, product):
        self.favorites.append(product)
    def remove_from_favorites(self, product):
        self.favorites.remove(product)
    def view_cart(self):
        return self.cart.list_items()
    def checkout(self):
        spisok=self.cart.list_items()
        for i in spisok:
            self.orders.append(i)
            self.spisok.remove(i)
    def receive_message(self, text):
        self.inbox.append(text)

class Vendor():
    def __init__(self,id, name):
        self.id=id
        self.name=name
        self.inbox=[]
    def add_product(self, marketplase, product):
        marketplase.products.append(product)
    def remove_product(self, marketplace, product):
        marketplace.remove_product(product)
    def update_product(self, marketplace, product, new_price, new_count):
        product.change_price(new_price)
        product.change_count(new_count)
        
        marketplace.notify.notify_all(f'dla {product} teper cena {new_price} and count {new_count}')
    def get_message(self, message):
        self.inbox.append(message)


        


class Product():
    def __init__(self, name, id,price, count, vendor, category):
        self.name=name
        self.id=id
        self.price=price
        self.count=count
        self.vendor=vendor
        self.category=category
    def update_price(self, new_price):
        self.price=new_price

    def update_count(self, new_count):
        self.count=new_count


class Order():
    def __init__(self, id, name, products:dict):
        self.id=id
        self.name=name
        self.products=products
        self.amount=0.0
        self.status='PENDING'
    def calculate_amount(self):
        for product, count in self.products.items.items():
            amount+=product.price*count
    def update_status(self, new_status):
        self.status=new_status

class Cart():
    def __init__(self, user, items:dict):
        self.user=user
        self.items=items
    def add_item(self, product, count):
        if product in self.items:
            self.item[product]+=count
        else:
            self.item[product]=count
    def get_total(self):
        total=0
        for product, count in self.items.items.items():
            total+=product.price*count
        return total
    def remove_item(self, item):
        if item not in self.items:
            return False
        del self.items[item]
    def clear_cart(self):
        for i in self.items.keys():
            del self.items[i]
    def list_items(self):
        list_items=[]
        for i in self.items.keys():
            list_items.uppend(i)
        return list_items




class MarketPlace():
    def __init__(self):
        self.users=[]
        self.vendors=[]
        self.products=[]
        self.orders=[]
        self.audit_log=[]
        self.notify=NotificationCenter()
    def register_user(self,id, name, email, cart):
        user=User(id, name, email, cart)
        self.users.append(user)
        self.notify.notify_student(user, 'vy uspeshno zaregistrirovany')
    def register_vendor(self, id, name):
        vendor=Vendor(id, name)
        self.vendors.append(vendor)
        self.notify.notify_vendor(vendor,'vy uspeshno zaregistrirovany')

    def remove_product(self, product):
        self.products.remove(product)
        self.notify_all(f'product{product} udalen')
    
    def place_order(self, user):
        user.checkout()
        self.notify_user(user, 'vse tovary v korzine kupleny')

class NotificationCenter():
    def __init__():
        pass
    def notify_user(self, user, message):
        user.get_message(message)
    def notify_vendor(self, vendor, message):
        vendor.get_message(message)
    def notify_all(self, marketplace, message):
        for i in marketplace.users:
            i.get_message('message')
        for j in marketplace.vendors:
            j.get_message('message')
        
