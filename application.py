from flask import (
    Flask,
    render_template,
	request, jsonify
)

app = Flask(__name__)

plans = [
    {'planId': 1,
     'projectId': '1',
     'storeId': '1',
     'projectDuration': '1 Weeks',
     'filename': 'S1P1W1.phs',
	 'versionNmbr': 'v1',
	 'activeflag': 'true',
	 'createdByUser': 'ABC'	 ,
	 "createdDate": "2018-11-16"
	 },
    {'planId': 3,
     'projectId': '1',
     'storeId': '1',
     'projectDuration': '2 Weeks',
     'filename': 'S1P1W2.phs',
	 'versionNmbr': 'v1',
	 'activeflag': 'true',
	 'createdByUser': 'ABC'	 ,
	 "createdDate": "2018-11-16"
	 },
    {'planId': 3,
     'projectId': '1',
     'storeId': '1',
     'projectDuration': '3 Weeks',
     'filename': 'S1P1W3.phs',
	 'versionNmbr': 'v1',
	 'activeflag': 'true',
	 'createdByUser': 'ABC'	,
	 "createdDate": "2018-11-16"
	 },
]

@app.route('/', methods=['GET'])

def home():
    return "OK"

@app.route('/all', methods=['GET'])
def api_all():
    return jsonify(plans)
@app.route('/plans', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
                f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"
@app.route('/BuildPlan', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for plan in plans:
        if plan['planId'] == id:
            results.append(plan)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(id)
