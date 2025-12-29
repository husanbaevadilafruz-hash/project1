from flask import Flask, request, jsonify
app=Flask(__name__)
import random
history1num=[]
@app.route('/primer', method=['POST'])
def primer():
    num1=random.randint(0, 9)
    history1num.append(num1)
    num2 
    