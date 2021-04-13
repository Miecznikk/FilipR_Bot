from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Zyje zyje"

def run():
  app.run(host='0.0.0.0',port=50662)

def keep_alive():
    t = Thread(target=run)
    t.start()