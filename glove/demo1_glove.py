'''
* CSE520 Real-Time Systems
* Demo 1 Glove Sensor Data Collection Service
* Jeremy Manin
*
* Created with help from sample code from AWS and Adafruit
'''
'''
TODO:
* Remove remaining arp parser refs
* Add sensor data collection
* Add subscribing to control sensorDataTopic
* Investigate prettier way handle json creation
* Split file into functions?
* Add files to git
'''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import json

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from sensorDataTopic: ")
    print(message.topic)
    print("--------------\n\n")

# Connection settings
host = "an91x6ytmr3ss-ats.iot.us-east-2.amazonaws.com"
'''rootCAPath = "certs/root-CA.crt"
certificatePath = "certs/2db4660fce-certificate.pem.crt"
privateKeyPath = "certs/2db4660fce-private.pem.key"'''
rootCAPath = "root-CA.crt"
certificatePath = "2db4660fce-certificate.pem.crt"
privateKeyPath = "2db4660fce-private.pem.key"
port = 8883
clientId = "glove"
sensorDataTopic = "$aws/things/sensor_glove/shadow/update"
controlTopic = "\$aws/things/glove_control/shadow/update"

# Global vars
start = False

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

# Subscribe to control sensorDataTopic
myAWSIoTMQTTClient.subscribe(sensorDataTopic, 1, customCallback)
time.sleep(2)

# Publish to sensor data sensorDataTopic when start sensorDataTopic is received until control sensorDataTopic says stop
while True:
    '''message = {}
    message['state'] = {}
    message['state']['reported'] = {}
    message['state']['reported']['flex_index'] =
    message['state']['reported']['flex_middle'] =
    message['state']['reported']['flex_ring'] =
    message['state']['reported']['flex_pinky'] =
    message['state']['reported']['flex_thumb'] =
    message['state']['reported']['imu_x'] =
    message['state']['reported']['imu_y'] =
    message['state']['reported']['imu_z'] =
    message['state']['reported']['imu_accel_x'] =
    message['state']['reported']['imu_accel_y'] =
    message['state']['reported']['imu_accel_z'] =
    messageJson = json.dumps(message)
    
    myAWSIoTMQTTClient.publish(sensorDataTopic, messageJson, 1)'''

    time.sleep(1)
