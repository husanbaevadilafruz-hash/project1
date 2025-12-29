# server.py
from flask import Flask, request, jsonify
from salon import Salon

app = Flask(__name__)
salon = Salon()

@app.route('/add_client', methods=['POST'])
def add_client():
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    result = salon.add_client(name)
    return jsonify({'result': result})

@app.route('/get_clients', methods=['GET'])
def get_clients():
    result = salon.list_clients()
    return jsonify({'result': result})

@app.route('/book_mesto', methods=['POST'])
def book_mesto():
    data = request.get_json() or {}
    client_name = data.get('client_name', '').strip()
    master_name = data.get('master_name', '').strip()
    prefer_wait = data.get('wait', False)
    result = salon.book_mesto(client_name, master_name, prefer_wait)
    return jsonify({'result': result})

@app.route('/get_masters', methods=['GET'])
def get_masters():
    result = salon.list_masters()
    return jsonify({'result': result})

@app.route('/finish_master', methods=['POST'])
def finish_master():
    data = request.get_json() or {}
    master_name = data.get('master_name', '').strip()
    result = salon.finish_master(master_name)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
