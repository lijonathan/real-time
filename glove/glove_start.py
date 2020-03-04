'''
* CSE520 Real-Time Systems
* Demo 1 Glove Sensor Data Collection Start Test Command
* Jeremy Manin
*
* Created with help from sample code from AWS
'''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import json

# Connection settings
host = "an91x6ytmr3ss-ats.iot.us-east-2.amazonaws.com"
rootCAPath = "certs/root-CA.crt"
certificatePath = "certs/2db4660fce-certificate.pem.crt"
privateKeyPath = "certs/2db4660fce-private.pem.key"
port = 8883
clientId = "test_controller"
controlTopic = "$aws/things/glove_control/shadow/update"

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect to AWS IoT
myAWSIoTMQTTClient.connect()
time.sleep(2)

# Build and publish control topic telling glove to start
message = {}
message['state'] = {}
message['state']['reported'] = {}
message['state']['reported']['command'] = "start"
messageJson = json.dumps(message)
myAWSIoTMQTTClient.publish(controlTopic, messageJson, 1)