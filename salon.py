# salon.py
from collections import deque

class Client:
    def __init__(self, name):
        self.name = name
      
        

class Salon:
    def __init__(self):
        # available == True означает: мастер свободен
        self.masters = {
            'Olga':  {'available': True, 'current': None, 'queue': deque()},
            'Anna':  {'available': True, 'current': None, 'queue': deque()},
            'Nastya':{'available': True, 'current': None, 'queue': deque()},
        }
        self.clients = {}

    def add_client(self, name):
        if not name:
            return 'Имя пустое'
        if name in self.clients:
            return f'Клиент {name} уже существует'
        self.clients[name] = Client(name)
        return f'{name} успешно добавлен'

    def book_mesto(self, client, master_name, wait=False):
        # проверки
        if client not in self.clients:
            return f'Нет клиента {client}'
        if master_name not in self.masters:
            return f'Нет мастера {master_name}'

        master = self.masters[master_name]

        # если мастер свободен — клиент обслуживается сразу
        if master['available']:
            master['available'] = False
            master['current'] = client
            return f'{client} обслуживается у {master_name} прямо сейчас'

        # мастер занят
        if wait:
            master['queue'].append(client)
            return f'{client} добавлен в очередь к {master_name}'

        # клиент не хочет ждать — ищем другого свободного мастера
        for name, m in self.masters.items():
            if m['available']:
                m['available'] = False
                m['current'] = client
                return f'{client} перенаправлен к {name}, так как {master_name} занят'
        # если ни одного свободного мастера нет
        return 'Нет свободных мастеров'

    def finish_master(self, master_name):
        if master_name not in self.masters:
            return 'Нет такого мастера'
        master = self.masters[master_name]

        # если есть очередь — берем следующего
        if master['queue']:
            next_client = master['queue'].popleft()
            master['current'] = next_client
            master['available'] = False
            return f'{master_name} теперь обслуживает {next_client} (взято из очереди)'

        # очереди нет — мастер становится свободен
        master['current'] = None
        master['available'] = True
        return f'{master_name} теперь свободен'

    def list_clients(self):
        return list(self.clients.keys())

    def list_masters(self):
        # вернём словарь с явными значениями (queue в виде списка)
        result = {}
        for name, m in self.masters.items():
            result[name] = {
                'available': m['available'],
                'current': m['current'],
                'queue': list(m['queue'])
            }
        return result
