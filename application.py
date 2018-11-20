from flask import (
    Flask,
    render_template,
	request, jsonify
)

# Create the application instance
app = Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
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


# Create a URL route in our application for "/"
@app.route('/', methods=['GET'])






def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/plans', methods=['GET'])
def api_all():
    return jsonify(plans)
	
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

app.run()