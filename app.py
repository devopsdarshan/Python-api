from flask import Flask
from apis_fire import api
###from apis import api### use this for normal operations
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api.init_app(app)

app.run(debug=True,host='0.0.0.0', port=8080)
#app.run(debug=True)##to run on on normal 127.0.0.1:5000
#app.run(debug=True,ssl_context='adhoc' ) ######to make this https
#pip install pyopenssl



