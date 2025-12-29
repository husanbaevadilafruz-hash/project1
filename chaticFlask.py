from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/list_of_clients')
def list_of_clients():
    spisok=[]
    data=request.get_json()
    name=data.get['name']
    spisok.append(name)
    return jsonify({'spisok':spisok})
