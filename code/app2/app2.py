from flask import Flask, render_template, redirect, url_for
import matplotlib.pyplot as plt
import io
import base64
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/nextjs/*": {"origins": "http://localhost:3000"}})
# app.config['APPLICATION_ROOT'] = '/app2'

@app.route('/')
def index():
    return '''
    <h1>This is the Flask App</h1>
    <a href="/app2/plot/"><button>Go to Plot Page</button></a>
    '''

@app.route('/plot/')
def plot():
    img = io.BytesIO()
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 2, 3, 4]
    plt.plot(x, y)
    plt.title('Simple Plot')
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return f'<img src="data:image/png;base64,{plot_url}">'

if __name__ == '__main__':
	# dash_app.server = app
	# app.run(host='localhost',port=8001, debug=True)
	app.run(host='localhost',port=8001, debug=True)

