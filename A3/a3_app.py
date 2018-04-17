from a3 import prod
from flask import *

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index1.html', prod = None)

@app.route('/multiply', methods=['POST','GET'])
def mult():
	return render_template('index1.html', prod = prod(int(request.form['num1']), int(request.form['num2'])))		

if __name__ == '__main__':
	app.run(host="0.0.0.0") #in () can put host="0.0.0.0" for client server type running
