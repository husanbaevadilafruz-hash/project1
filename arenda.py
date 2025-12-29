class User():
    def __init__(self, name, id, balance):
        self.name=name
        self.id=id
        self.balance=balance
        self.status='ACTIVE'
        self.notifications=[]
    def block(self):
        self.status='BLOCKED'
    def unblock(self):
        self.status='ACTIVE'
    def get_message(self, message):
        self.notifications.uppend(message)

from abc import ABC, abstractmethod
class Recourse(ABC):
    def __init__(self,id):
        self.id=id
        self.status='available'
    @abstractmethod
    def mark_in_use(self):
        self.status='in_use'
    def available(self):
        self.status='available'
class Bike(Recourse):
    def __init__(self):
        super().__init__()
    def mark_in_use(self):
        return super().mark_in_use()
    def available(self):
        return super().available()
class Scooter (Recourse):
    def __init__(self):
        super().__init__()
    def mark_in_use(self):
        return super().mark_in_use()
    def available(self):
        return super().available()
class Workspace(Recourse):
    def __init__(self):
        super().__init__()
    def mark_in_use(self):
        return super().mark_in_use()
    def available(self):
        return super().available()
from time import datetime
class Rental(): 
    def __init__(self, user, recourse):
        self.user=user
        self.recourse=recourse
        self.start_time=datetime.now()
        self.end_time=None
        self.status='active'
        self.notifier=NotificationCenter()
        self.recourse.mark_in_use()
       
        self.logger=Logger()
    def finish(self):
        self.end_time=datetime.now()
        self.status='finished'
        self.notifier.notify(self.user, 'vasha arenda zakonchena')
        self.recourse.available()
        self.logger.add_to_history(f'{self.user} finished using {self.recourse}')
    def cancel(self):
        self.end_time=datetime.now()
        self.status='cancelled'
        self.notifier.notify(self.user, 'vasha arenda otmenena')
        self.recourse.available()


      
    




class PaymantPolicy():
    def __init__(self):
        self.prices={}
        self.skidki={}
        self.shtrafy={}
    def calculate_cost(self, rental):
        cost=(rental.end_time-rental.start_time)*self.prices[rental.recourse]
        return cost
class PaymentServise():
    def __init__(self):
       self.history=[]
       
       
    def snatiye_deneg(self, rental):
        if rental.user.balance<PaymantPolicy(self).calculate_cost(rental):
            return False
        else:
            rental.user.balance-=rental.paymant
        self.history.uppend(f'{rental.user} sovershil oplatu razmerom v {rental.paymant}')


class Complaint():
    def __init__(self, user, recourse, text):
        self.user=user
        self.recourse=recourse
        self.text=text

class Review():
    def __init__(self, user, recourse, raiting, kommentarii):
        self.user=user
        self.recourse=recourse
        self.raiting=raiting
        self.kommentatii=kommentarii
class AccessPolicy():
    def __init__(self):
        pass
    def mojno_li_arendovat(self, recourse):
        if recourse.status=='available':
            return True
        else:
            return False
    def mojno_li_zakonchit_arendu(self, rental):
        if rental.user.balance<rental.paymant:
            return False
        else:
            return False
        

        
class NotificationCenter():
    def __init__(self):
        pass
    def notify(self, users, text):
        for i in users:
            i.get_message(text)


class Logger():
    def __init__(self):
        self.history=[]
    def add_to_history(self, info):
        self.history.uppend(info)

class Platform():
    def __init__(self):
        self.users=[]
        self.recources=[]
        self.arendy=[]
        self.proverka=AccessPolicy()
        self.rental=Rental()
        self.payment=PaymentServise()
        self.raschet_stoimosti=PaymantPolicy()
        self.logger=Logger()
    def arendovat(self, user, recourse):
        if self.proverka(recourse) is True:
            self.rental(user, recourse)
            self.logger.add_to_history(f'{recourse} arendovali')
    def zakonchit_arendu(self,  rental):
        if self.payment.snatiye_deneg is False:
            return False
        self.raschet_stoimosti.calculate_cost(rental)
        self.payment.snatiye_deneg(rental)
        self.rental.finish()
        self.logger.add_to_history(f'{rental.user} zakonchil arendu')
        
        
