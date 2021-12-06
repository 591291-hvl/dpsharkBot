from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
	return "Hello. i am alive"

def run():
	app.run(host='0.0.0.0',port=8080)

def keepAlive():
	t = Thread(target=run)
	t.start()

