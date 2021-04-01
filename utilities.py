import messages
import fcm
import firebase_admin

from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from flask_expects_json import expects_json
from pyfcm import FCMNotification

# Initialize Firestore DB
# cred = credentials.Certificate('key.json')
# default_app = initialize_app(cred)
# firebase_admin.initialize_app()
initialize_app()
db = firestore.client()

reg_event_ref = db.collection_group('RegisteredEvent')

def homeUtility():
	return "<h1>Welcome to TFD</h1>"

def sendNotifToRegisteredUsersUtility_bkp():
    """
    """
    try:
        id = request.json['pid']

        # to create a profile collection w/ RegisteredEvent sub collection w/ a status key in it 
        # then, uncomment the below line 
        # query = reg_event_ref.where('pid', u'==', id).where('status', u'array_contains_any', [u'active', u'unknown'])
        query = reg_event_ref.where('pid', u'==', id)

        regUsers = [event.to_dict() for event in query.stream()]

        regUsersDocIds = []                        
        for regUser in regUsers:
        	regUsersDocIds.append(regUser['doc_id'])

        # push_service = FCMNotification(api_key=fcm.fcm_api_key, proxy_dict=None)
		# to get the token, data_message
      	# token is the fcm_token_id and data_message is the json format of the message
        # notifyEvents = push_service.notify_multiple_devices(registration_ids=token, data_message=data_message,extra_notification_kwargs=None)
        # result = { messages.STATUS: messages.OK, messages.MESSAGE: messages.SUCCESS, "notifyEvents":notifyEvents} 

        result = { messages.STATUS: messages.OK, messages.MESSAGE: messages.SUCCESS, "regUsersDocIds":regUsersDocIds}
        # result = { messages.STATUS: messages.OK, messages.MESSAGE: messages.SUCCESS, "regUsers":regUsers}
        return jsonify(result), 200
    except Exception as e:
    	# traceback.print_exc(file=sys.stdout)
    	result = { messages.STATUS: messages.FAILED, messages.MESSAGE: messages.ERROR}
    	return jsonify(result), 500

def sendNotifToRegisteredUsersUtility():
    """
    """
    id = request.json['pid']

    # to create a profile collection w/ RegisteredEvent sub collection w/ a status key in it 
    # then, uncomment the below line 
    # query = reg_event_ref.where('pid', u'==', id).where('status', u'array_contains_any', [u'active', u'unknown'])
    query = reg_event_ref.where('pid', u'==', id)

    regUsers = [event.to_dict() for event in query.stream()]

    regUsersDocIds = []                        
    for regUser in regUsers:
        regUsersDocIds.append(regUser['doc_id'])

    # push_service = FCMNotification(api_key=fcm.fcm_api_key, proxy_dict=None)
    # to get the token, data_message
    # token is the fcm_token_id and data_message is the json format of the message
    # notifyEvents = push_service.notify_multiple_devices(registration_ids=token, data_message=data_message,extra_notification_kwargs=None)
    # result = { messages.STATUS: messages.OK, messages.MESSAGE: messages.SUCCESS, "notifyEvents":notifyEvents} 

    result = { messages.STATUS: messages.OK, messages.MESSAGE: messages.SUCCESS, "regUsersDocIds":regUsersDocIds}
    # result = { messages.STATUS: messages.OK, messages.MESSAGE: messages.SUCCESS, "regUsers":regUsers}
    return jsonify(result), 200



def unexpectedErrorUtility(e):
    """Handle exceptions by returning swagger-compliant json."""
    result = { messages.STATUS: messages.FAILED, messages.MESSAGE: messages.ERROR}
    return jsonify(result), 500

