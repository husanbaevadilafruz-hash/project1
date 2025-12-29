# class Rate:
#     rates=[]
#     def __init__(self, from_currency,  price):
#         self.from_currency=from_currency
#         self.price=price
#     rates.append(self)



from collections import defaultdict

class Currency:
    def _init_(self, name, money, buy_rate, sell_rate):
        self.name = name
        self.money = money
        self.buy_rate = buy_rate
        self.sell_rate = sell_rate

    def _str_(self):
        return f'{self.name}: money={self.money}, buy={self.buy_rate}, sell={self.sell_rate}'




class Cassa:
    history = []
    profit = defaultdict(float)

    def _init_(self, name, base_currency: Currency):
        self.name = name
        self.base_currency = base_currency 
        self.currencies = {base_currency.name: base_currency}      #chto takoye base currency

    def add_currency(self, currency: Currency):
        self.currencies[currency.name] = currency

    def buy(self, currency_name, amount):
        cur = self.currencies[currency_name]
        cost = cur.sell_rate * amount
        if cur.money < amount:
            return f" Not enough {currency_name} in {self.name}"
        cur.money -= amount
        self.base_currency.money += cost
        profit = cost - (amount * cur.buy_rate)
        Cassa.profit[self.name] += profit
        Cassa.history.append(f"{self.name}: Sold {amount} {currency_name} for {cost} {self.base_currency.name}")
        return f" {self.name}: Client bought {amount} {currency_name} for {cost} {self.base_currency.name}"

    def sell(self, currency_name, amount):
        cur = self.currencies[currency_name]
        gain = cur.buy_rate * amount
        if self.base_currency.money < gain:
            return f" Not enough {self.base_currency.name} in {self.name}"
        cur.money += amount
        self.base_currency.money -= gain
        profit = (amount * cur.sell_rate) - gain
        Cassa.profit[self.name] += profit
        Cassa.history.append(f"{self.name}: Bought {amount} {currency_name} for {gain} {self.base_currency.name}")
        return f" {self.name}: Client sold {amount} {currency_name} for {gain} {self.base_currency.name}"

    def show_currencies(self):
        return "\n".join([str(cur) for cur in self.currencies.values()])






class Branch:
    def _init_(self, name):
        self.name = name
        self.cassas = {}


    def add_cassa(self, cassa: Cassa):
        self.cassas[cassa.name] = cassa

    def show_info(self):
        result = f" Branch {self.name}\n"
        for c in self.cassas.values():
            result += f"\n {c.name}:\n{c.show_currencies()}\n"
        return result

SOM1 = Currency('SOM', 1000000, 1.0, 1.0)
USD1 = Currency('USD', 100000, 87.0, 85.0)

SOM2 = Currency('SOM', 500000, 1.0, 1.0)
EUR2 = Currency('EUR', 50000, 95.0, 93.0)

cassa1 = Cassa("Cassa 1", SOM1)
cassa1.add_currency(USD1)

cassa2 = Cassa("Cassa 2", SOM2)
cassa2.add_currency(EUR2)

branch = Branch("MAIN EXCHANGE CENTRE")
branch.add_cassa(cassa1)
branch.add_cassa(cassa2)

print(branch.show_info())
print(cassa1.buy('USD', 1000))
print(cassa2.sell('EUR', 500))
print(branch.show_info())
print(Cassa.profit)




class  Rate:
    rates=defaultdict[lambda:defaultdict(float)]
    def __init__(self, rate, t_type, price):
        self.rate=rate
        self.t_type=t_type
        self.price=price
        Rate.rates[self.rate][self.t_type]=self.price  
    


    @classmethod
    def change_rate(cls, rate, t_type, new_price):
        cls.rates[rate][t_type]=new_price

    @classmethod
    def show_all(cls):
        return dict(cls.rates)

class Kassa:
    kassa=defaultdict(float)
    def __init__(self, valuta, summa):
        self.valuta=valuta
        self.summa=summa
        Kassa.kasaa[self.valuta]=self.summa
    @classmethod
    def show_kassa(cls):
        return dict(cls.kassa)
    
class History:
    history=[]
    @classmethod
    def add_tranzaction(cls, date, t_type, valuta,summa, polza=0.0):
        tranzaction={
            'date':date,
            't_type':t_type,
            'valuta':valuta,
            'summa':summa,
            'polza':polza

        }
        cls.history.append(tranzaction)
    
        





class Buy:
    
    def __init__(self, valuta, summa):
        self.valuta=valuta
        self.summa=summa
    @classmethod
    def buy(cls, date, valuta, summa):
        if valuta not in Rate.rates or not 'buy' in Rate.rates[valuta]:
            return 'n  et ceny dla pokupki takoi valuty'
        if Kassa.kassa['som']<Rate.rates[valuta]['buy']*summa:
            return 'ne hvataet deneg'
        Kassa.kassa['som']-= Rate.rates[valuta]['buy']*summa
        Kassa.kassa[valuta]+=summa   
    History.add_tranzaction( 'buy', valuta , summa, polza=0.0) 










#     Создай класс Currency, в котором есть:

# code (например, "USD"),

# name (например, "Доллар США").

# 2️⃣ Создай класс Rate, который наследуется от Currency:

# Добавь атрибуты:
# buy_rate, sell_rate.

# Добавь метод spread(), который возвращает разницу между курсами (прибыль обменника).

# ➡️ Таким образом, Rate наследует код и имя валюты от Currency.

class currency:
    def __init__(self, code, name):
        self.code=code
        self.name=name

class Rate(Currency):
    def __init__(self, code, name, buy_rate=None, sell_rate=None):
        super().__init__(code, name)
        self.buy_rate=buy_rate
        self.sell_rate=sell_rate

    def spread(self):
        return self.sell_rate-self.buy_rate 
    


#     Задание 2. Класс Cashbox (инкапсуляция)

# 1️⃣ Создай класс Cashbox, который хранит в себе остатки валют.
# Используй инкапсуляцию:

# создавай словарь __balance = {} (приватный атрибут),

# сделай методы:

# add(currency, amount) — добавить валюту;

# remove(currency, amount) — убрать валюту, если хватает;

# show_balance() — вывести текущее состояние кассы.


class Cashbox:
    __balance={}
    def set_add(self, currency, amount):
        self.currency=currency
        self.amount=amount
        Cashbox.__balance[self.currency]=self.anount      
    def remove(self, currency, amount):
        self.currency=currency
        self.amount=amount
        del Cashbox.__balance[self.currency]
    def get_show_balance(self):
        return Cashbox.__balance
    
# Задание 3. Класс Transaction и History (композиция)

# 1️⃣ Класс Transaction:

# поля: date, type ("buy" или "sell"), currency, amount, profit.

# метод to_dict() — возвращает словарь для добавления в историю.

# 2️⃣ Класс History:

# хранит список всех транзакций;

# имеет метод add(transaction) — добавляет транзакцию;

# метод filter_by_date(start, end) — возвращает все операции за период.


class  Transaction:
    def add_tranzaction(cls, date, t_type, valuta,summa, polza=0.0):
        tranzaction={
            'date':date,
            't_type':t_type,
            'valuta':valuta,
            'summa':summa,
            'polza':polza

        }
        cls.history.append(tranzaction)