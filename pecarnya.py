# 1) Клиенты (многоуровневое наследование)

# Customer — базовый: id, name, phone, email, created_at.

# RegisteredCustomer(Customer) — добавьте: loyalty_program (ссылка), points (int), метод add_points(int).

# VIPCustomer(RegisteredCustomer) — добавьте: персональная надбавка к скидке (например, +5%), приоритет уведомлений.

class Customer:

    def __init__(self,  name, phone, email, created_at, birth_day):
        self.name=name
        self.phone=phone
        self.email=email
        self.created_at=created_at
        self.birth_day=birth_day
        self.orders=[]


class RegisteredCustomer(Customer):
    def __init__(self, id, name, phone, email, created_at):
        super().__init__(id, name, phone, email, created_at)
        self.loyalty_program=None
        self.points=0
    def add_points(self, point):
        self.points+=point
    def discount_for(self):
        return 0.05
class VIPcustomer(RegisteredCustomer):
    def __init__(self, id, name, phone, email, created_at):
        super().__init__(id, name, phone, email, created_at)
    def nadbavka(self, razmer_skidki, razmer_nadbavki):
        return razmer_skidki+razmer_skidki/100*razmer_nadbavki
    def discount_for(self):
        return 0.10
    

class Order:
    all_orders=[]

    def __init__(self, customer, items,  date=datetime.now()):
        self.customer=customer
        self.items=items
        self.date=date
        Order.all_orders.append(self)
        Customer.orders.append(self)
         


#     Товары (многоуровневое наследование и полиморфизм)

# Product — базовый: sku, name, base_price, category ("bread"|"cake"|"cookie"|...).

# BakedGood(Product) — добавьте: fresh_until (дата), метод is_fresh(at_time).

# Cake(BakedGood) — добавьте: size ("mini"|"standard"|"large"), опциональные layers (int).

# CustomCake(Cake) — добавьте: message_on_top (надпись), design_fee (доплата), переопределите расчёт цены.
from datetime import datetime

class Product:
    def __init__(self, sku, name, base_price, category ):
        self.sku=sku
        self.name=name
        self.base_price=base_price
        self.category=category

class BakedGood(Product):
    def __init__(self, sku, name, base_price, category, fresh_until=None):
        super().__init__(sku, name, base_price, category)
        self.fresh_until=fresh_until
    def is_fresh(self, date):
            if self.fresh_until is None:
                return 'data svejesti ne zadana'
            if date<self.fresh_until:
                return 'vypechka eshe svejaya'
            else:
                return 'vypechka prosrochena' 
            


class Cake(BakedGood):
    def __init__(self, sku, name, base_price, category, size=None, layers=None):
        super().__init__(sku, name, base_price, category)
        self.size=size
        self.layers=layers

class CustomCake(Cake):
    def __init__(self, sku, name, base_price, category, size, layers, message_on_top=None, design_fee=0 ):
        super().__init__(sku, name, base_price, category , size, layers)
        self.message_on_top=message_on_top
        self.design_fee=design_fee
    def price(self):
        return self.base_price+self.design_fee
    

# ) Программы лояльности (иерархия стратегий)

# LoyaltyProgram — интерфейс/базовый класс: name, метод discount_for(customer, order) → % или абсолютная сумма.

# PointsProgram(LoyaltyProgram) — скидка зависит от накопленных баллов.

# BirthdayProgram(LoyaltyProgram) — скидка в день рождения (если добавите birth_date у клиента).

# TieredProgram(LoyaltyProgram) — ступенчатые уровни (Silver/Gold/Platinum) по сумме покупок за N дней.

# Полиморфизм скидок: Order.total() использует композицию (заказ → клиент → программа) для вычисления итоговой цены.

class LoyaltyProgram:
    def __init__(self, name):
        self.name=name
    def discount_for(self):
        return 0
class PointsProgram(LoyaltyProgram):
    def __init__(self, name):
        super().__init__(name)
    def discount_for(self, customer, order):
        return customer.points/100 
class BirthdayProgram(LoyaltyProgram):
    def __init__(self, name):
        super().__init__(name)
    def discout_for_birthday(self, order, customer):
        if customer.birth_day.day==order.date.day and  customer.birth_day.month==order.date.month:
            return 0.20


