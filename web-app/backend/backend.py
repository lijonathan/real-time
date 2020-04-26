'''
* CSE520 Real-Time Systems
* UI Backend flask server
* Jeremy Manin, Justin Marshall
*
* usage: (with FLASK_APP env var set to "backend.py") flask run
'''

# Import utility libraries
import json
import logging
import threading
import time
# Import flask libraries
from flask import Flask
from flask_cors import CORS
# Import AWS IoT library
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
# Import backend subscription thread
import backend_sub

# Flask setup
app = Flask(__name__)
CORS(app)

# AWS IoT Setup
## Connection settings
host = "an91x6ytmr3ss-ats.iot.us-east-2.amazonaws.com"
rootCAPath = "../../certs/root-CA.crt"
certificatePath = "../../certs/2db4660fce-certificate.pem.crt"
privateKeyPath = "../../certs/2db4660fce-private.pem.key"
port = 8883
clientId = "back_end_pub"
controlTopic = "$aws/things/cloud_control/shadow/update"

## Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.ERROR)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

## Init AWSIoTMQTTClient
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

## AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

## Connect to AWS IoT
myAWSIoTMQTTClient.connect()
time.sleep(2)

# Create thread object for backend subwscription service
class sub_thread (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
   def run(self):
        backend_sub.start_sub()

# Subscribe Start - Starts up backend subscription service
@app.route("/subscribe-start")
def start_subscribe():
    my_sub_thread = sub_thread()
    my_sub_thread.start()
    return('Subscription thread started')

# Cloud Start - Sends cloud control topic to get gesture from glove
@app.route("/cloud-start")
def start_cloud():
    # Build and publish control topic telling cloud to start
    message = {}
    message['state'] = {}
    message['state']['reported'] = {}
    message['state']['reported']['command'] = 'start'
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(controlTopic, messageJson, 1)
    
    # Return success
    return('Cloud control topic successfully published')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
