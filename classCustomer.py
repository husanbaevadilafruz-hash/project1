# MODEL=БИЗНЕС-ЛРОГИКА И ДАННЫЕ

# Класс CUSTOMER-представляет клиента банка с двумя валютными счетами

# 1.приватные поля(доступ только через методы класса)
#       .имя клиента(уникальный идентификатор)
#       .баланс в долларах(начальный 0.0)
      
#       .баланс в сомах(начальный 0.0)
# 2.Публичные методы:
#       .пополнение счета-увеличение баланса в указанной валюте на заданную сумму с валидацией
#       .снятие средств-уменьшение баланса с предварительной проверкой достаточности средств
#       .запрос баланса-возврат текущего остатка по указанной валюте
#       .get для получения имени клиента
class Customer():
    def __init__(self, name):
        self.__name=name
        self.balanceKGS=0.0
        self.balanceUSD=0.0
    def popolnenie(self, currency:str, amount:int):
        if amount<0:
            return 'vvedine >0'
        if currency.strip().upper()=='USD':
            self.balanceUSD+=amount
        if currency.strip().upper()=='KGS':
            self.balanceKGS+=amount 
        return f'balance klienta {self.__name} popolnen na {amount} {currency}'
    def snatiye(self, currency:str, amount:int):
        if amount<0:
            return 'vvedine >0'
        if currency.strip().upper()=='USD' and self.balanceUSD>amount:
            self.balanceUSD-=amount
        if currency.strip().upper()=='KGS' and self.balanceKGS.amount:
            self.balanceKGS-=amount 
        return f's balanca klienta {self.__name} snali {amount} {currency}'


    def vozvrat_ostatka(self, currency):
        if currency.strip().upper()=='USD':
            return self.balanceUSD
        if currency.strip().upper()=='KGS':
            return self.balanceKGS
        else:
            return 'oshibka'
        
    def get_name(self):
        return self.__name

Dilia=Customer('Dilia')
print(Dilia.get_name())
print(Dilia.popolnenie('usd', 10000))
print(Dilia.snatiye('usd', 600))
print(Dilia.vozvrat_ostatka('usd'))
print(Dilia.popolnenie('som', 1000000)) 



               