import flask
import flask_expects_json
import pyfcm 
import os
import json
import messages
import fcm
import six.moves

from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS, cross_origin
from utilities import *
from six.moves import http_client


# Initialize Flask App
app = flask.Flask(__name__)
# app.config["DEBUG"] = True

# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def home():
    return homeUtility()

@app.route('/sendNotifToRegisteredUsers', methods=['POST'])
@expects_json(messages.registeredEventsSchema)
def sendNotifToRegisteredUsers():
    return sendNotifToRegisteredUsersUtility()

@app.errorhandler(http_client.INTERNAL_SERVER_ERROR)
def unexpectedError(e):
    return unexpectedErrorUtility(e)

# Call factory function to create a blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    messages.SWAGGER_URL,  
    messages.API_URL,
    config={  
        'app_name': "TFD Application"
    },
)

app.register_blueprint(swaggerui_blueprint)

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4445)))
