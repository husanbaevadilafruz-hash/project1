class Client():
    def __init__(self, id, name, phone,email):
        self.id=id
        self.name=name
        self.phone=phone
        self.email=email
        self.orders=[]
        self.reseivations=[]
        self.inbox=[]
    def reseive_message(self, message):
        self.inbox.append(message)
    def add_order(self, order):
        self.orders.append(order)
    def add_reseivaition(self, reseivation):
        self.reseivations.append(reseivation)
class Table():
    def __init__(self, number,capacity):
        self.number=number
        self.capacity=capacity
        self.is_available=True
        self.current_order=None
        self.waiter=None
    def assign_order(self, order):
        self.current_order=order
    def free_table(self):
        self.is_available=True

class Reservation():
    def __init__(self, client, table, date, time):
        self.client=client
        self.table=table
        self.date=date
        self.time=time
        self.status='active'
    def cancel(self):
        self.status='cancelled'
    def complete(self):
        self.status='completed'

class MenuCategory():
    def __init__(self, name):
        self.name=name
        self.items=[]
    def addItem(self, item):
        self.items.append(item)
class MenuItem():
    def __init__(self, id, name, price, category):
        self.id=id
        self.name=name
        self.price=price
        self.cateegory=category
        self.is_able=True
    def disable(self):
        self.is_able=True
    def enable(self):
        self.is_able=False
class Order():
    def __init__(self, id, client, waiter, table):
        self.id=id
        self.client=client
        self.waiter=waiter
        self.status='open'
        self.total_price=0.0
        self.items=[]
        self.table=table
    def add_item(self, orderItem):
        self.items.append(orderItem)
    def calculate_total(self):
        for i in self.items:
            self.total_price+=i.menu_item.price*i.quantity
       
    def close(self):
        self.status='closed'
class OrderItem():
    def __init__(self, menuItem, quantity):
        self.menuItem=menuItem 
        self.quantity=quantity
        self.status='ordered'
    def mark_ready(self):
        self.status='ready'
class Waiter():
    def __init__(self, id, name):
        self.id=id
        self.name=name
        self.tables=[]
        self.orders=[]
        self.inbox=[]
    def assign_table(self,table):
        self.tables.append(table)
    def take_order(self, order):
        self.orders.append(order)
    def notify(self, text):
        self.inbox.append(text)

class Kitchen():
    def __init__(self):
        self.active_orders=[]
        self.inbox=[]
    def accept_order(self,order):
        self.active_orders.append(order)
    def mark_item_ready(self, orderItem):
        orderItem.mark_ready()
    def complete_order(self, order):
        order.close()
        self.active_orders.remove(order)
    def get_notification(self, text):
        self.inbox.append(text)
    
class Payment():
    def __init__(self, id, order, method):
        self.id=id
        self.order=order
        self.method=method
        self.amount=order.total_price+order.total_price/100*15
        status='pending'
    def pay(self):
        self.status='paid'
        self.order.status='paid'
from datetime import datetime
class Receipt():
    def __init__(self, payment):
        self.payment=payment
        self.date=datetime.now()
    def print(self):
        return f' {id: {self.payment.id},
                   order: {self.payment.order},
                   method: {self.payment.method},
                   amount: {self.payment.amount},
                   table:{self.payment.order.table}}'
    
class NotificationCenter():
    def __init__(self):
        pass
    def notify_client(self,client, message):
        client.reseive_message(message)
    def notify_waiter(self, waiter, message):
        waiter.notify(message)
    def notify_kitchen(self, kitchen, message):
        kitchen.get_notification(message)        
    


class RestourantMeneger():
    def __init__(self, kitchen, notifier, audit_log):
        self.clients=[]
        self.tables=[]
        self.menu=[]
        self.waiters=[]
        self.orders=[]
        self.kitchen=kitchen
        self.notifier=notifier
        self.audit_log=audit_log
    def add_client(self, id, name,phone,email):
        client=Client(id, name,phone,email)
        self.clients.append(client)
        self.audit_log.add_record(f'client {name} dobavlen')
    def add_menu_item(self, id, name, price, category ):
        menu_item=MenuItem( id, name, price, category)
        self.menu.append(menu_item)
        self.audit_log.add_record(f'bludo {menu_item} dobavlen')
    def create_reservation(self,  client, table, date, time):
        reservation=Reservation( client, table, date, time)
        client.add_reservaition(reservation)
        self.audit_log.add_record(f'stol {table} zabronirovan')
    def create_order(self, id, client, waiter, table ):
        order=Order( id, client, waiter, table)
        self.orders.append(order)
        table.is_available=False
        table.assign_order(order)
        client.add_order(order)
        waiter.take_order(order)
        
        self.notifier.notify_client(client, 'vash zakaz oformlen')
       
        self.notifier.notify_waiter(waiter, 'primite zakaz')
        self.audit_log.add_record('zakaz dobavlen')
    def assign_waiter(self, waiter, table):
        waiter.assign_table(table)
        table.waiter=waiter
        self.notifier.notify_waiter(waiter, f'vy naznacheny na srol {table}')
        self.audit_log.add_record(f'{waiter} naznachen na {table}')
    def send_to_kitchen(self, order):
        self.kitchen.accept_order(order)
        self.notifier.notify_kithen(self.kitchen, 'primite zakaz')
        self.kitchen.accept_order(order)
        self.audit_log.add_record(f'{order} otpravlen na kuhnu')
    def process_payment(self,id,  order, method):
        payment=Payment(id, order, method )
        payment.pay()
        receipt=Receipt(payment)
        return receipt.print








class AuditLog():
    def __init__(self):
        self.records=[]
    def add_record(self, text):
        self.records.append(text)