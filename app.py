# app.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hola cara de Bolaaaaaaaa!"}), 200

@app.route('/about')
def about():
    return jsonify({"version": "1.0", "author": "Yagmur Ozden"}), 200

if __name__ == '__main__':
    app.run(debug=True)
