from flask import Flask, request, jsonify
from ClassCalculator import Calculator

calkul = Calculator()
app = Flask(__name__)

@app.route('/reshenie', methods=['POST'])
def reshenie():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    deistvie = data.get('deistvie')

    result = calkul.reshenie(x, y, deistvie)
    return jsonify({'otvet': result})

if __name__ == '__main__':
    app.run(debug=True)
