class Store:
    def __init__(self, name_store):
        self.name_store=name_store
        self.items=defaultdict(int)
        self.names={}
        self.history=[]
        self.cart=defaultdict(list)
        self.sold_items=defaultdict(int)
        self.clients=set()
        self.item_objects=[]
    def add_item(self, item, count):
        self.items[item.strihkod]+=count
        self.names[item.strihkod]=item

    def add_cart(self, client, item, count):
        if count<self.items[item.strihkod]:
            self.cart[client.phone].append((item.strihkod, count))
            self.items[item.strihkod]-=count
            self.sold_items[self.names[item.strihkod].strihkod]+=count

            self.clients.add(client.name)
    def solditems(self, item, count):
        self.sold_items[item.strihkod]=count
    def add_ite(self, item):
        self.item_objects.append(item)
    def close_cart(self, client):
        total=0
        for strihkod, count in self.cart[client.phone]:
            total+=self.names[strihkod].sale_price*count
        del self.cart[client.phone]
        self.history.append((client.phone, total))
    def show_history(self):
        result=''
        for client_phone, total in self.history:
            result+=f'{client_phone}:{total} \n'
        result+='\n'
        return result
    def update_price(self, item, new_price):
        item.sale_price=new_price 

# Задание 8. Популярные товары

# Реализуйте метод show_popular_items(self, n=5), который:

# сортирует товары по количеству продаж;

# выбирает n самых популярных;

# возвращает строку, где указано:
# количество, штрихкод, название, цена продажи
# (каждый товар с новой строки).
    def show_popular_items(self, n=5):
        sorted_sells = sorted(self.sold_items, key=self.sold_items.get, reverse=True)[:n]
        result = ''
        for strihkod in sorted_sells:
            count = self.sold_items[strihkod]
            item = self.names[strihkod]
            result += f'{count}, {item.strihkod}, {item.name}, {item.sale_price} \n'
        return result
    # Задание 9. Подсчёт прибыли

# Реализуйте метод show_profit(self), который:

# для каждого проданного товара вычисляет разницу между ценой продажи и закупки,

# суммирует её по всем товарам,

# возвращает итоговую прибыль магазина
    def show_profit(self):
        profit=0
        for product, count in self.sold_items.items():
            profit+=(self.names[product].sale_price-self.names[product].purchase_price)*count
        return profit       
    def client_count(self):
        return len(self.clients)       
# Реализуйте метод show_item(self, item: Item),
# который возвращает строку с информацией о товаре в формате:

# name: <название>
# shtrihkod: <код>
# sale_price: <цена продажи>
# purchase_price: <цена закупки>
# sold items: <количество проданных>                  
    def info(self):
        for i in self.names:
            result=''
            result+=f'{'name'}:{self.names['strihkod'].name}, {'sale_price'}: {self.names['strihkod'].sale_price},{'purchase_price'} :{self.names['strihkod'].purchase_price}, {'sold_items'}:{self.sold_items['sttihkod']} ' 
    def sell(self, item, amount):
        self.history.append(f'{item.name} prodali za {item.pursale_price*amount}')




def naibolshii_povtor(x):
    if len(x)==0:
        return False
    max_count=1
    max_el=x[0]
    current_el=x[0]
    current_count=1
    for i in range(1, len(x)):
        if x[i]==current_el:
            current_count+=1
        else:
            current_el=x[i]
        if current_count>max_count:
            max_el9=x[i]
            max_count=max_count

print(naibolshii_povtor('dfibvoisbdvoigwsrwwwweooooooooooooobfddddddddddd'))
