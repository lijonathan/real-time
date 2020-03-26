'''
* CSE520 Real-Time Systems
* Demo 1 Glove Sensor Data Collection Service
* Jeremy Manin
*
* Created with help from sample code from AWS and Adafruit
'''

# Import utility libs
import time
# Import AWS IoT Core libs
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import json
# Import Adafruit base libs
#import board
#import busio
#import digitalio
# Import BNO055 lib
#import adafruit_bno055
# Import MCP3008 libs
#import adafruit_mcp3xxx.mcp3008 as MCP
#from adafruit_mcp3xxx.analog_in import AnalogIn
from sklearn.ensemble import RandomForestClassifier
import json


with open ("..\\src\\web-app\\misc\\fabData.json") as json_file:
    data = json.load(json_file)

X = []
Y = []
for data_pt in data:
    vals = data_pt["state"]["reported"]
    X.append(list(vals.values()))
    result = data_pt["result"]
    Y.append(result)


rf = RandomForestClassifier()
print(X)
rf.fit(X, Y)

class CallbackContainer(object):

    def __init__(self, client):
        self._client = client
        self.imu_orient_z = 0
        self.imu_orient_x = 0
        self.imu_orient_y = 0
    # Custom MQTT message callback
    def customCallback(self, client, userdata, message):
        topicContents = json.loads(message.payload.decode('utf-8'))
        self.imu_orient_x = topicContents['state']['reported']['imu_x']
        self.imu_orient_y = topicContents['state']['reported']['imu_y']
        self.imu_orient_z = topicContents['state']['reported']['imu_z']
        print(topicContents)
        print("\n\n\n")

    def getx(self):
        return self.imu_orient_x

    def gety(self):
        return self.imu_orient_y

    def getz(self):
        return self.imu_orient_z

# Connection settings
host = "an91x6ytmr3ss-ats.iot.us-east-2.amazonaws.com"
rootCAPath = "certs/root-CA.crt"
certificatePath = "certs/2db4660fce-certificate.pem.crt"
privateKeyPath = "certs/2db4660fce-private.pem.key"
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

# Create BNO055 device
#i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_bno055.BNO055(i2c)

# Setup MCP3008
## Create the spi bus
#spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
## Create the cs (chip select)
#cs = digitalio.DigitalInOut(board.D5)
## Create the mcp object
#mcp = MCP.MCP3008(spi, cs)
## Create an analog input channels
#chan0 = AnalogIn(mcp, MCP.P0)
#chan1 = AnalogIn(mcp, MCP.P1)
#chan2 = AnalogIn(mcp, MCP.P2)
#chan3 = AnalogIn(mcp, MCP.P3)
#chan4 = AnalogIn(mcp, MCP.P4)

# Publish to sensor data sensorDataTopic when start sensorDataTopic is received until control sensorDataTopic says stop
while True:


	X_data = []
    X_input = []
    vals_input = message["state"]["reported"]

    X_input.append(myCallbackContainer.getx())
    X_input.append(myCallbackContainer.gety())
    X_input.append(myCallbackContainer.getz())
    
    X_data.append(X_input)
    res = rf.pred(X_data)


    myAWSIoTMQTTClient.publish(sensorDataTopic, res, 1)

    time.sleep(1)
