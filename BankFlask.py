
# CONTROLLER- FLASK REST API SERVER
 
# Эндпоинты:
#    .создание клиента-прием имени, проверка уникальности, создание записи
#    .список клиентов-возврат перечня всех зарегистрированных имен
#    .баланс клиента-запрос остатков на обоих счетах выбранного клиента
#    .пополнение счета-зачисление средств на указанный счет в выбранной валюте
#    . снятие средств-снятие с проверкой достаточности баланса
#    .конвертация валют-перевод средств между счетами клиента по текущему курсу
#    .установка курса-обновление курса для будущий операций   from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from klassBanking import Banking 

app = Flask(__name__)
bank = Banking()
@app.route('/add_customer', methods=['POST'])
def add_client():
    data=request.get_json()
    name=data.get('name')
    result=bank.register_client(name)
    return jsonify({'result':result})
@app.route('/zapros', methods=['GET'])
def zapros():
    data=request.get_json()                          
    name=data.get['name']
    client=bank.poisk_klienta(name)

    return jsonify(
        {'balanceUSD': client.vozvrat_ostatka('usd'),
        'balanceKGS': client.vozvrat_ostatka('kgs')}
    )
@app.route('/popolnenie', methods=['POST'])
def popolnenie():
    data=request.get_json()
    customer=data.get['customer']
    currency=data.get['currency']
    amount=data.get['amount']
    result=customer.popolnenie( currency, amount)
    return jsonify({'result': result})

# 1. Список всех клиентов

# GET /all_customers

@app.route('/all_customers', methods=['GET'])
def all_customers():
    result = bank.spisok_klientov()
    return jsonify({'customers': result})

# 📌 2. Снятие средств

# POST /snyatie

@app.route('/snyatie', methods=['POST'])
def snyatie():
    data = request.get_json()
    name = data['name']
    currency = data['currency']
    amount = data['amount']

    client = bank.poisk_klienta(name)
    result = client.snyatie(currency, amount)

    return jsonify({'result': result})

# 📌 3. Конвертация валют

# POST /convert

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    name = data['name']
    from_currency = data['from']
    to_currency = data['to']
    amount = data['amount']

    client = bank.poisk_klienta(name)
    result = client.konvertaciya(from_currency, to_currency, amount)

    return jsonify({'result': result})

# 📌 4. Установка курса

# POST /set_rate

@app.route('/set_rate', methods=['POST'])
def set_rate():
    data = request.get_json()
    usd_to_kgs = data['usd_to_kgs']
    kgs_to_usd = data['kgs_to_usd']

    result = bank.update_rate(usd_to_kgs, kgs_to_usd)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)    