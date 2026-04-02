from flask import Flask, request, jsonify

import socket


app = Flask(__name__)

# @app.route mapeaza URL -> functie Python​

@app.route('/', methods=['GET'])

def index():

    return "Rotaru Stefan 367/2024"



# <item_id> = parametru dinamic in URL​

@app.route('/item/<item_id>', methods=['GET'])

def get_item(item_id):

    return jsonify({"item_id": item_id})



# IP-ul real​

@app.route('/ip', methods=['GET'])

def get_ip():

    ip = socket.gethostbyname(socket.gethostname())

    return jsonify({"ip": ip})



# POST: citeste body JSON​

@app.route('/post', methods=['POST'])

def post_data():

    data = request.json # dict Python din body​

    value = data.get('value', 0)

    return jsonify({"received": value})



if __name__ == '__main__':

# 0.0.0.0 = TOATE interfetele (nu doar localhost!)​

    app.run(host='0.0.0.0', port=8001, debug=True)