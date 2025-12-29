from flask import Flask, request, jsonify
from collections import defaultdict
from datetime import datetime
app=Flask(__name__)
history=[]
kassa=defaultdict(float)
rates=defaultdict(lambda:defaultdict(float))
polza=0.0
def add_tranzakshion(time, tranzakshion_type, valuta, summa, polza=0.0):
    tranzaktion={
        'time':time,
        'tranzaktion_type':tranzakshion_type,
        'valuta':valuta,
        'summa':summa,
        'polza':polza
    }
    history.append(tranzaktion)
@app.route('/add_rate')
def add_rate():
    valuta=request.args.get('valuta')
    t_type=request.args.get('t_type')
    cena=request.args.get('cena')
    if not valuta or not t_type or not cena:
        return 'vvedite vse'
    try:
        cena=float(cena)
    except ValueError:
        return 'cena doljna byt chislom'
    rates[valuta][t_type]=cena
    history.append(f'dla {t_type} {valuta} ustanovili cenu {cena} ')
    return jsonify({
        'message':f"dla {t_type} {valuta} ustanovili cenu {cena}",
        'rates':rates
    })
@app.route('/change_rate')
def change_rate():
    valuta=request.args.get('valuta')
    t_type=request.args.get('t_type')
    new_cena=request.args.get('cena')
    if not valuta or not t_type or not new_cena:
        return 'vvedite vse'
    if valuta not in rates or t_type not in rates[valuta]:
        return 'net takogo'
    try:
        new_cena = float(new_cena)
    except ValueError:
        return 'cena doljna byt chislom'
    rates[valuta][t_type]=new_cena
    history.append(f'v {datetime.now().strftime("%Y:%m:%d %H-%M_%S")} ismenili cenu dla {t_type} {valuta} na {new_cena}')
    return jsonify({
        'message':f'v {datetime.now().strftime("%Y:%m:%d %H-%M_%S")} ismenili cenu dla {t_type} {valuta} na {new_cena}',
        'rates':rates
    })

@app.route('/kassochka')
def kassochka():
    valuta=request.args.get('valuta')
    summa=request.args.get('cena')
    if not valuta or not summa:
        return 'vvedite valutu i summu'
    try:
        summa=float(summa)
    except ValueError:
        return 'summa doljna byt chislom'
    kassa[valuta]=summa
    history.append(f'dla{valuta} ustanovili summu {summa}')
    return jsonify({
        'message':f'dla{valuta} ustanovili summu {summa}',
        'kassa':kassa
    })
    
@app.route('/buy')
def buy():
    valuta=request.args.get('valuta')
    summa=request.args.get('cena')
    if not valuta or not summa:
        return 'vvedite vse'
    if not valuta in rates or not 'buy' in rates[valuta]:
        return 'net ceny dla pokupki takoi valuty'
    try:
        summa=float(summa)
    except ValueError:
        return 'summa doljna byt chislom'
    valuta=valuta.upper()
    stoimost=rates[valuta]['buy']*summa
    if kassa['som']<stoimost:
        return 'u nas ne hvataet deneg'
    kassa['som']-=stoimost
    kassa[valuta]+=summa
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    add_tranzakshion(time, 'buy', valuta, summa, polza=0)
    return jsonify({
            'message':f'kupili {summa} {valuta}',
            'kassa':kassa
        })
@app.route('/sale')
def sale():
    global polza
    valuta=request.args.get('valuta')
    summa=request.args.get('cena')
    if not valuta or not summa:
        return 'vvedite vse'
    if not valuta in rates or not 'sell' in rates[valuta]:
        return 'net ceny dla pokupki takoi valuty'
    try:
        summa=float(summa)
    except ValueError:
        return 'summa doljna byt chislom'
    valuta=valuta.upper()
    if kassa[valuta]<summa:
        return 'ne hvatit deneg'
    stoimost=rates[valuta]['sell']*summa
    kassa[valuta]-=summa
    kassa['SOM']+=stoimost
    pol=stoimost-summa*rates[valuta]['buy']
    polza+=pol
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    add_tranzakshion(time, 'sell', valuta, summa, pol)
    return jsonify({
        'essage':f'prodali {summa} {valuta}',
        'kassa':kassa
    })
@app.route('/polza_v_promejutke')
def polza_v_promejutke():
    start_time=request.args.get('start_time')
    end_time=request.args.get('end_time')
    start_time=datetime.fromisoformat(start_time)
    end_time=datetime.fromisoformat(end_time)
    itog=0.0
    for i in history:
        if start_time<datetime.fromisoformat(i['time'])<end_time:
            itog+=i['polza']
    return jsonify({'polza_v_promejutke':polza})


def pribil_po_valute(history):
    pribyl_po_valutam=defaultdict(float)
    for i in history:
        pribyl_po_valutam[i['valuta']]+=i['polza']
    return max(pribyl_po_valutam, key=pribyl_po_valutam.get)

def sorted_po_polze(history):
    return sorted(history, key=lambda x: x['polza'], reverse=True)
def sorted_po_date(history):
    return sorted(history, key=lambda x:datetime.fromisoformat(x['time']))


def chastoprodavaemyi(history):
    prodaji=defaultdict(int)
    for i in history:
        if i['tranzaktion_type']=='sell':
            prodaji[i['valuta']]+=1
    return max(prodaji, key =prodaji.get)



@app.route('/chastoprodavaemui')
def chasroprodavaemyi():
    start_date=request.args.get('start_date')
    end_date=request.args.get('end_date')
    prodaji=defaultdict(int)
    for i in history:
        if datetime.fromisoformat(start_date)<datetime.fromisoformat(i['time'])<datetime.fromisoformat(end_date):
            prodaji[i['name']]+=1

    
    if not prodaji:
         return 'net prodaj za etot period'
    return jsonify({'max':max(prodaji, key=prodaji.get)})
            

# Функция/маршрут для топ-3 валют по прибыли

# Возвращать 3 валюты с самой большой суммарной прибылью.

# Функция/маршрут для топ-3 валют по количеству продаж

# Считаем, сколько раз каждая валюта была продана.

# Фильтрация истории по типу транзакции

# /history_filtered?t_type=sell → возвращает все продажи.

# Суммарная прибыль по каждой валюте

# Возвращаем JSON вида: {'USD': 50, 'EUR': 30}.

# Сортировка истории по сумме сделки

# По возрастанию/убыванию summa.

# Функция для самого прибыльного промежутка дня

# Например, искать час с наибольшей суммарной прибылью.

# Частопродаваемое блюдо или валюта по промежутку

# То, что ты уже делала, но с возможностью возвращать топ-3.

# Вывод статистики баланса кассы

# /kassa_stats → сколько валюты, суммарная прибыль, общее количество сделок.


def pribil_po_valute(history):
    pribyl_po_valutam=defaultdict(float)
    for i in history:
        pribyl_po_valutam[i['valuta']]+=i['polza']
    return sorted(pribyl_po_valutam, key=pribyl_po_valutam.get, reverse=True)[:3]
def top_3_saled():
    saled_koli=defaultdict(int)
    for i in history:
        if i['t_type']=='sell':
            saled_koli[i['currency']]+=1
    return sorted(saled_koli, key=saled_koli.get, reverse=True)[:3]
def summarnaya_pribyl():
    pribyli=defaultdict(float)
    for i in history:
        if i['tranzaktion_type']=='sell':
            pribyli[i['currency']]+=i['polza']
    return jsonify({'ptibyli':pribyli})


\
def sorted_by_polza(history):
    filtered=[i for i in history if isinstance(i, dict) and 'sorted' in i]
    return sorted(filtered, key=lambda x:x['polza'], reverse=True)



def max_v_chasu(history):
    prodaji=defaultdict(float)
    for i in history:
        if isinstance(i,dict) and i.get('tranzakshion_type')=='sell':
            date=datetime.isoformat(i['time'])
            hour=hour.date
            prodaji[hour]=i['polza']
    return max(prodaji, key=prodaji.get)


def statistik():
  
    result={
        'skolko_valuty':0,
        'kolishestvo_sdelok':0,
        'obshaa_pribyl':0.0
    }
    for i in history:
        if isinstance(i,dict):
            result['kolishestvo_sdelok']
        result['obshaa_pribyl']+=i['pribyl']
    return result






