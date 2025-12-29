class Client():
    def __init__(self, id, name, balance ):
        self.id=id
        self.name=name
        self.__balance=balance
    def can_pay(self, amount):
        if amount<=0:
            return False
        if self.__balance>=amount:
            return True
    def debit(self, amount):
        if not self.can_pay:
            return 'nedostatochno stedstv'
        self.__balance-=amount
    def notify(self, text):
        self.inbox.append(text)

class Cargo():
    def __init__(self, id,  weight,  volume,  category,  owner ,current_location, weight_price, volume_price):
        self.id=id
        self.weigth=weight
        self.volume=volume
        self.category=category
        self.owner=owner
        self.status='created'
        self.current_location=current_location
        self.weigth_price=weight_price
        self.volume_price=volume_price
    def update_status(self, new_status):
        self.status=new_status
    def move_to(self, new_location):
        self.current_location=new_location
class Warehouse():
    def __init__(self,  id ,location ,capacity ):
        self.id=id
        self.location=location
        self.capacity=capacity
        self.stored_cargo_ids=set()
    def has_space(self):
        if len(self.stored_cargo_ids)<self.capacity:
            return True
    def store(self,kargo_id):
        if not self.has_space():
            return False
        if kargo_id not in self.stored_cargo_ids:
            self.stored_cargo_ids.add(kargo_id)
    def release(self, kargo_id):
        if kargo_id not in self.stored_cargo_ids:
            return False
        self.stored_cargo_ids.remove(kargo_id)


class Vehicle():
    def __init__(self,  id ,type , max_weight , max_volume ,current_location ,assigned_cargo_id, price, speed):
        self.id=id
        self.type=type
        self.max_weight=max_weight
        self.max_volume=max_volume
        self.current_location=current_location
        self.assigned_cargo_id=assigned_cargo_id
        self.price=price 
        self.speed=speed                        
    def can_load(self, cargo):
        if self.max_volume>=cargo.volume and self.max_weight>cargo.max_weight:
            return True
    def load(self,cargo):
        if not self.can_load():
            return False
        self.assigned_cargo_id=cargo.id
    def unload(self):
        if not self.assigned_cargo_id:
            return False
        else:
            self.assigned_cargo_id=None
class Driver():
    def __init__(self, id , name , licenses):
        self.id=id
        self.name=name
        self.licenses=licenses
        self.vehidle_id=None
        self.status='available'
        self.inbox=[]
    def assign_vehicle(self, vehicle):
        if self.vehidle_id is None:
            self.vehidle_id=vehicle.id
    def release(self):
        self.vehicle_id=None
    def notify(self, text):
        self.inbox.append(text)


class Route():
    def __init__(self, nodes):
        self.nodes=nodes
from datetime import datetime
class ShippingOrder():
    def __init__(self, id, cargo ,client ,route , current_node_index , vehicle ,driver):
        self.id=id
        self.cargo=cargo
        self.client=client
        self.route=route
        self.current_node_index=current_node_index
        self.vehicle=vehicle
        self.driver=driver
        self.status='created'
      
    def next_node(self):
        if not self.driver:
            return False
        self.current_node_index=self.current_node_index+1
    def complete(self):
        self.status='completed'

class DistanceMatrix():
    def __init__(self, distances):
        self.distances=distances
    def get_distance(self, a, b):
        try:
            return self.distances[a,b]
        except :
            print(' DistanceNotFoundException ')  

from datetime import timedelta
class PricingEngine():
    def __init__(self):
        self.distance=DistanceMatrix()
    def calculate_cost( self, order):
        order.cargo.weigh_price*order.cargo.weight+order.cargo.volume_price*order.cargo.volume+self.distance(order.route)*order.vehicle.price
class TimeEstimator():
    def __init__(self):
        self.distance=DistanceMatrix()
    def estimate(self, order):
        
        hours=order.vehicle.speed*self.distance.get_distance(order.route)
        return f'{hours} hours'

class CustomsDeclaration():
    def __init__(self, cargo,origin_country,destination_country):
        self.cargo=cargo
        self.origin_country=origin_country
        self.destination_country=destination_country
        self.status='pending'
    def clear(self):
        self.status='cleared'


class IncurancePolicy():
    def __init__(self, order, overage_amount, premium):
        self.order=order
        self.overage_anount=overage_amount
        self.premium=premium
    def is_active(self):
        if self.order.status=='created' or self.order.status=='in_transit':
            return True
        elif self.order.status=='completed ' or self.order.status=='frozen':
            return False
class Invoise():
    def __init__(self,order, tax, insurance):
        self.pricing=PricingEngine()
        self.order=order
        self.tax=tax
        self.incurance_price=insurance.premium
        self.shipping_cost=self.pricing(order)
        self.total=self.tax+self.incurance_price+self.shipping_cost  

class NotificationCenter():
    def __init__(self):
        pass
    def notify_client(self, client, text):
        client.notify(text)
    def notify_drivet(self, driver, text):
        driver.notify(text)
    
class AuditLog():
    def __init__(self):
        self.records=[]
    def record(self, event):
        self.records.append(event)
class LogisticMeneger():
    def __init__(self):

