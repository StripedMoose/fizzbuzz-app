from flask import Flask, jsonify

app = Flask(__name__)

def is_fizz(n):
	if ( n % 3 == 0 ):
		return True 

def is_buzz(n):
	if ( n % 5 == 0 ):
		return True

def find_response(x):

	if is_fizz(x) and is_buzz(x):
		response = "fizzbuzz"
	else:	
		if is_fizz(x):
			response = "fizz"
		elif is_buzz(x):
			response = "buzz"
		else:
			x += 1
			response = str(x)
	return response

@app.route('/query/<int:q>', methods=['GET'])
def get_reply(q):
	reply = find_response(q)
	return jsonify({'reply': reply})

@app.route("/ping")
def pong():
    return "poing"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
