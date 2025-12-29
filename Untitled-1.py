from flask import Flask, request
from collections import defaultdict

app = Flask(__name__)

user_messages = defaultdict(list)

@app.route('/send_message')
def send_message():
    user = request.args.get('user')
    message = request.args.get('message')
    
    if not user or not message:
        return 'Введите данные через ссылку!'

    user_messages[user].append(message)
    return f'Сообщения {user}: {user_messages[user]}'

if __name__ == '__main__':
    app.run(debug=True)
