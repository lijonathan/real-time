'''
* CSE520 Real-Time Systems
* Cloud ML processing of data sent from glove
* Jonathan Li
*
* Created with help from sample code from AWS
* Random Forest Classifier
'''

# Import utility libs
import time
# Import AWS IoT Core libs
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import json
from sklearn.ensemble import RandomForestClassifier
import json
from os import listdir
from os.path import isfile, join
import os


X = []
Y = []

onlyfiles = [f for f in listdir("../glove/training_data") if isfile(join("../glove/training_data", f))]

for i in range(0, len(onlyfiles)):
    onlyfiles[i] = os.path.join("../glove/training_data", onlyfiles[i])

for i in range(0, len(onlyfiles)):
    with open(onlyfiles[i]) as data_file:
        for line in data_file:
            line = line.strip("\n")
            x = []
            data_pts = line.split(",")
            result = data_pts[- 1]
            del data_pts[-1]
            for i in range(0, len(data_pts)):
                x.append(float(data_pts[i]))

            X.append(x)
            Y.append(result)
            

print(X)
print(Y)
rf = RandomForestClassifier()
rf.fit(X, Y)

class CallbackContainer(object):

    def __init__(self, client):
        self._client = client
        self.imu_orient_z = 0
        self.imu_orient_x = 0
        self.imu_orient_y = 0
        self.flex_index = 0
        self.flex_middle = 0
        self.flex_ring = 0
        self.flex_pinky = 0
        self.flex_thumb = 0


    # Custom MQTT message callback
    def customCallback(self, client, userdata, message):
        topicContents = json.loads(message.payload.decode('utf-8'))
        self.imu_orient_x = topicContents['state']['reported']['imu_x']
        self.imu_orient_y = topicContents['state']['reported']['imu_y']
        self.imu_orient_z = topicContents['state']['reported']['imu_z']

        self.flex_index = topicContents['state']['reported']['flex_index']
        self.flex_middle = topicContents['state']['reported']['flex_middle']
        self.flex_ring = topicContents['state']['reported']['flex_ring']
        self.flex_pinky = topicContents['state']['reported']['flex_pinky']
        self.flex_thumb = topicContents['state']['reported']['flex_thumb']


        print(topicContents)
        print("\n\n\n")

    def getx(self):
        return self.imu_orient_x

    def gety(self):
        return self.imu_orient_y

    def getz(self):
        return self.imu_orient_z

    def get_flex_index(self):
        return self.flex_index

    def get_flex_middle(self):
        return self.flex_middle

    def get_flex_ring(self):
        return self.flex_ring

    def get_flex_pinky(self):
        return self.flex_pinky

    def get_flex_thumb(self):
        return self.flex_thumb



# Connection settings
host = "an91x6ytmr3ss-ats.iot.us-east-2.amazonaws.com"
rootCAPath = "../glove/certs/root-CA.crt"
certificatePath = "../glove/certs/2db4660fce-certificate.pem.crt"
privateKeyPath = "../glove/certs/2db4660fce-private.pem.key"
port = 8883
clientId = "cloud_Ec2"
sensorDataTopic = "$aws/things/processed_data/shadow/update"
controlTopic = "$aws/things/sensor_glove/shadow/update"

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
myCallbackContainer = CallbackContainer(myAWSIoTMQTTClient)
myAWSIoTMQTTClient.subscribe(controlTopic, 1, myCallbackContainer.customCallback)
time.sleep(2)


# Publish to sensor data sensorDataTopic when start sensorDataTopic is received until control sensorDataTopic says stop
while True:


    X_received = []
    data_pt = []
    data_pt.append(myCallbackContainer.getx())
    data_pt.append(myCallbackContainer.gety())
    data_pt.append(myCallbackContainer.getz())

    data_pt.append(myCallbackContainer.get_flex_index())
    data_pt.append(myCallbackContainer.get_flex_middle())
    data_pt.append(myCallbackContainer.get_flex_ring())
    data_pt.append(myCallbackContainer.get_flex_pinky())
    data_pt.append(myCallbackContainer.get_flex_thumb())

    print(data_pt)
    X_received.append(data_pt)
    res = rf.predict(X_received)
    
    send_result = res[0]
    print(send_result)
    myAWSIoTMQTTClient.publish(sensorDataTopic, send_result, 1)

    time.sleep(1)
