from flask import Flask,request, jsonify
from datetime import datetime
from collections import defaultdict
rates=defaultdict(lambda:defaultdict(float))
history=[]
kassa=defaultdict(float)
app=Flask(__name__)
polza=0.0 

def initialize_default_data():
    rates['USD'] = {'buy': 87.5, 'sell': 87.0}
    rates['EUR'] = {'buy': 95.0, 'sell': 94.5}
    rates['SOM'] = {'buy': 0.01, 'sell': 0.009}

    kassa['USD'] = 1000.0
    kassa['EUR'] = 500.0
    kassa['SOM'] = 100000.0


def log_transaction(transaction_type, currency, amount, profit=0.0):
    transaction = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'type': t_type,
        'currency': currency.upper(),
        'amount': amount,
        'profit': profit
    }
    history.append(transaction)


@app.route('/add_rate')
def add_rate():
    valuta=request.args.get('valuta')
    t_type=request.args.get('type')
    cena=request.args.get('cena')
    if not cena or not valuta or not t_type:
        return "vvedite, cenu, valutu i type"
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rates[valuta][t_type]=float(cena)
    history.append(f'v {time} dla {t_type} {valuta} ustanovili cenu {cena}')

    return jsonify({
        "message": f'dla {t_type} {valuta} ustanovlena cena {cena}',
        "rates":rates
        })

@app.route('/kassochka')
def kassochka():
    currency=request.args.get('currency')
    balance=(request.args.get('balance'))
    if not currency :
        return 'vvedite valutu i balance'
    if balance is None:
        return 'vvedite balance'
    try:
        balance=float(balance)
    except ValueError:
        return 'balance doljen byt chislom'

    kassa[currency]=balance
    history.append(f'dla {currency} ustanovlen balance {balance}')
    return jsonify ({
        'message':f'dla {currency} ustanovlen balance {balance}',
        'kassa':kassa
    })

    

@app.route('/buy')
def buy():
    x=request.args
    currency=request.args.get('currency')
    summa=x.get('summa')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not currency:
        return 'vvedite valutu'
    if summa is None:
        return 'vvedite summu'
    try:
        summa=float(summa)
    except ValueError:
        return 'summa doljna byt chislom'
    if currency not in rates or 'buy' not in rates[currency]:
        return 'net ceny dla pokupki takoi valuty'
    trata=float(rates[currency]['buy'])*summa
    if float(kassa['som'])<trata:
        return 'u nas ne hvatit deneg'
    kassa['som']-=trata
    kassa[currency]+=summa
    history.append(f"v {time} kupili {summa} {currency} po cene {rates[currency]['buy']}")
    return jsonify({
        'message':f"kupili {summa} {currency} po cene {rates[currency]['buy']}",
        'kassa':kassa
    })


@app.route('/sell')
def sell():
    currency=request.args.get('currency')
    summa=request.args.get('summa')
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not currency or not summa:
        return 'vvedite summu i valutu'
    if currency not in rates or 'sell' not in rates[currency]:
        return 'net ceny dla prodaji takoi valuty'
    if currency not in kassa:
        return 'net v prodaje takoi valuty'
    try:
        summa=float(summa)
    except ValueError:
        return 'summa doljna byt chislom'
    if summa<=0:
        return "summa doljna byt>0"
    if kassa[currency]<summa:
        return 'ne hvataet'
    stoimost=rates[currency]['sell']*summa
    kassa['som']+=stoimost
    kassa[currency]-=summa
    pol=stoimost-summa*rates[currency]['buy']
    polza+=pol
    history.append(f'v {time} prodali {summa} po cene {rates[currency]["sell"]}')
    return jsonify({
        'message':(f'prodali {summa} po cene {rates[currency]["sell"]}'),
        "poluchili polzu:" : pol,
        'kassa':kassa
    })

@app.route('/vernut_istoriu')
def vernut_istoriu():
    return jsonify(history)


@app.route('/vernut_polzu')
def vernut_polzu():
    return jsonify(polza)



@app.route('/change_cena')
def change_cena():
    currency=request.args.get('currency')
    t_type=request.args.get('type')
    new_price=request.args.get('new_price')
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not currency or not new_price or not t_type:
        return 'vvedite valutu, type i new_price'
    if not currency in rates or not t_type in rates[currency]:
        return 'net takogo'
    try:
        new_price = float(new_price)
    except ValueError:
        return 'new_price dolzhen byt chislom'
    rates[currency][t_type]=new_price
    history.append(f' v {time}dla {type} {currency} ustanovili novuu cenu {new_price}')
    return jsonify({
        "message":f' dla {t_type} {currency} ustanovili novuu cenu {new_price}',
        "rates":rates
    })

