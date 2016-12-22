import json
from flask import Flask, url_for
from flask import Response
app = Flask(__name__)

@app.route('/userinfo', methods = ['GET'])
def api_hello():
    data = {
        "userinfo": {
                "Department": "Devops",
                "first_name": "Hello",
                "last_name": "Testing",
                "Age": 25
        	    }
	}

    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)


