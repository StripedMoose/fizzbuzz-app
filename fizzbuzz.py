from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.cli.command('test')

def is_fizz(n):
	if ( n % 3 == 0 ):
		return True

def is_buzz(n):
	if ( n % 5 == 0 ):
		return True

def find_response(x):

	response = "ack"

	if is_fizz(x):
		response = "fizz"

#	if is_fizz(x) and is_buzz(x):
#		response = "fizzbuzz"
#	else:	
#		if is_fizz(x):
#			response = "fizz"
#		elif is_buzz(x):
#			response = "buzz"
#		else:
#			x += 1
#			resposne = str(x)
	return response

@app.route('/query/<int:q>', methods=['GET'])
def get_reply(q):
	reply = find_response(q)
	return jsonify({'reply': reply})


if __name__ == "__main__":
    app.run()
