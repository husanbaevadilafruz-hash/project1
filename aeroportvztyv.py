class Passenger():
    def __init__(self, id, name, passport):
        self.id=id
        self.name=name
        self.passport=passport
        self.tickets=[]
        self.bagagge=[]
        self.inbox=[]
    def add_message(self, message):
        self.inbox.append(message)

class Ticket():
    def __init__(self, passenger,flight, seat,class_type, status):
        self.passenger=passenger
        self.flight=flight
        self.seat=seat
        self.class_type=class_type
        self.status=status

class Baggage():
    def __init__(self,id,owner,weight):
        self.id=id
        self.owner=owner
        self.weigth=weight
        self.status='checked'
class Aircraft():
    def __init__(self, id, model, capacity):
        self.id=id
        self.model=model
        self.capacity=capacity
        self.status='ready'
    

class CrewMember():
    def __init__(self,id, name,role,license_valid):
        self.id=id
        self.name=name
        self.role=role
        self.license_valid=license_valid


class Crew():
    def __init__(self, aircraft):
        self.aircraft=aircraft
        self.members=[]
    def is_ready(self):
            return all(i.is_ready for i in self.members)

class Gate():
    def __init__(self, id, terminal):
        self.id=id
        self.terminal=terminal
        self.status='free'
class RunWay():
    def __init__(self, id):
        self.id=id
        self.status='open'

class WeatherReport():
    def __init__(self, wind, visibility, storm_level):
        self.wind=wind
        self.visibility=visibility
        self.storm_level=storm_level
        

class Flight():
    def __init__(self,	 number, aircraft,crew,gate,runway, date):
        self.number=number
        self.crew=crew
        self.gate=gate
        self.aircraft=aircraft
        self.runway=runway
        self.passengers=[]
        self.status='SCHEDULED'
        self.date=date
        self.baggases=[]

    def board_passenger(self, passenger):
        self.passengers.append(passenger)
    def delay(self):
        self.status='delayed'
    def cancel(self):
        self.status='canceled'
    def delay(self):
        self.status='delayed'
    def depart(self):
        self.status='departed'



class ScheduleManager():
    def __init__(self):
        pass
    def assign_gate(self, new_gate, flight):
        flight.gate=new_gate
    def reschedule(self, flight, new_date):
        flight.date=new_date

class SecurityCheck():
    def __init__(self, passenger, cleared:bool):
        self.passenger=passenger
        self.cleared=cleared

class MaintenanceRequest():
    def __init__(self, aircraft, issue, priority):
        self.aircraft=aircraft
        self.issue=issue
        self.priority=priority

class Emergency():
    def __init__(self, type, severity, flight):
        self.type=type
        self.severity=severity
        self.flight=flight
    def razreshit(self):
        if self.severity<1:
            return
        else:
            self.flight.status='cancelled'

class AIcontroller():
    def __init__(self):
        pass
    


class BaggageService():
    def __init__(self):
        pass
    def load_baggage(self, flight, baggage):
        flight.baggages.append(baggage)
    def report_lost(self, baggage):
        baggage.status='lost'   


        



    

class Notificenter():
    def __init__(self):
        pass
    def notify_passenger(self, passenger, text):
        passenger.add_message(text)



