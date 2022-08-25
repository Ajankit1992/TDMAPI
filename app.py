from flask import Flask
from flask import jsonify
from flask import request
import main
import HelperLibrary.helperLibrary as helperLib


app = Flask(__name__)

""" Function for checking API is running or not"""
@app.route('/')
def index():
	return "Hello TDM"


""" Function for Masking, Cloning and generating data based on SSN number."""
@app.route('/TDMAPI')
def tdmapi():
	ssn = request.args.get('ssn', default='*', type=str)
	result, error = main.TDMAPI(ssn)
	if result:
		helperLib.print_msg("INFO", "API Called successfully")
		return jsonify(status="Success", Message=error)
	else:
		helperLib.print_msg("ERROR", error)
		return jsonify(status="Failure", Message=error)


if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=8080)
