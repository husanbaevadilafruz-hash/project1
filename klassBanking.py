# Класс Banking -центральная система управления банковскими операциями
# 1.поля:
#    .текущий курс обмена USD к SOM (1 usd=87.5 som)
#    .коллекция всех зарегистрированных клиентов
# 2.методы:
#    .регистрация нового клиента с проверкой уникальности имени
#    .поиск клиента в системе по имени
#    .обновление курса валют для всех последующих операций конвертации 
#    .конвертация средств между счетами клиента по текущему курсу

from classCustomer import Customer

class Banking:
    

    def __init__(self):
        self.fromUSDtoKGS=87.5
        self.fromKGStoUSD=0.011 
        self.customers={}
        self.customers_names=[]
       
    def register_client(self, name):
        if name in self.customers:
            return 'etot klient uje sushestvuet'
        self.customers[name]=Customer(name)
    def collection(self):
        return list(self.customers.keys())
    def poisk_klienta(self, name):
        if name not in self.customers:
            return 'takogo klienta ne sushestvuet'
        return self.customers[name]
    def obnovlenie_kursa(self, from_currency, to_currency, new_price):
        try:
            new_price=float(new_price)
        except ValueError:
            return 'cena doljna byt chislom'
        if new_price<0:
            return 'nelza tak'
        if from_currency.strip().upper()=='USD' and to_currency.strip().upper()=='KGS':
            self.fromUSDtoKGS=new_price
        elif from_currency.strip().upper()=='KGS' and to_currency.strip().upper()=='USD':
            self.fromKGStoUSD=new_price 
        return 'uspeshno pomenali'
        
         
    def convertacia(self, customer, from_currency, to_currency, amount:int):
        try:
            anount=float(amount)
        except ValueError:
            return 'vvedite chislo'
        
        if amount<0:
            return 'tak nelza'

        
        if from_currency.strip().upper()=='USD' and to_currency.strip().upper()=='KGS':
          
            if customer.vozvrat_ostatka('usd')<amount:
                return 'ne hvataet'
            
            customer.popolnenie('kgs', amount*self.fromUSDtoKGS)
            customer.snatiye('usd', amount)

        if from_currency.strip().upper()=='KGS' and to_currency.strip().upper()=='USD':
        
            if customer.vozvrat_ostatka('kgs')<amount:
                return 'ne hvataet'
            customer.popolnenie('usd', amount*self.fromKGStoUSD)
            customer.snatiye('kgs', amount)
        return 'uspeshno'    
    
# bakai=Banking()
# bakai.register_client('Alya')
# Alya=bakai.customers["Alya"]
# print(Alya.popolnenie('usd', 200))
# print(bakai.customers)
# bakai.poisk_klienta('Alya')
# print(bakai.obnovlenie_kursa('usd', 'kgs', 88))
# print(bakai.fromKGStoUSD)
# print(bakai.fromUSDtoKGS)
# Alya.popolnenie('kgs', 10000)
# bakai.convertacia(Alya, 'usd', 'kgs', 10)
# print(Alya.vozvrat_ostatka('usd'))
# print(Alya.vozvrat_ostatka('kgs'))   





            
            
        





