from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/time')
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(host='0.0.0.0')

