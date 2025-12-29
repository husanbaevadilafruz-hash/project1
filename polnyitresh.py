from flask import Flask, request
from collections import defaultdict
app=Flask(__name__)

user_massages=defaultdict(list)

@app.route('/send_message')
def dend_message():
    user=request.args.get('user')
    message=request.args.get('message')
    if not user or not message:
        return 'vvedite dannye po ssylke'
    user_massages[user].append(message)
    return f'сообщения {user} :{user_massages[user]}'
if __name__=='__main__':
    app.run(debug=True)
