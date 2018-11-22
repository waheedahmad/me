from flask import (
    Flask,
    render_template,
	request, jsonify
)

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/plans', methods=['GET'])
def api_all():
    return jsonify("ALL Items")	

app.run()
