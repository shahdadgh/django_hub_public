# app.py
from flask import Flask #, redirect, url_for, session, jsonify
# from authlib.integrations.flask_client import OAuth
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/nextjs/*": {"origins": "http://localhost:3000"}})


@app.route('/')
def index():
	return "This is Flask App"


# if __name__ == '__main__':
# 	# dash_app.server = app
# 	# app.run(host='localhost',port=8001, debug=True)
# 	app.run(host='localhost',port=8001, debug=True)

