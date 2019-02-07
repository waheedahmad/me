from flask import (
    Flask,
    render_template,
	request,json, jsonify
)

app = Flask(__name__)


@app.route('/', methods=['GET'])

def home():
    return "OK"


@app.route('/plans', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "415 Unsupported Media Type ;)"+request.headers['Content-Type']
