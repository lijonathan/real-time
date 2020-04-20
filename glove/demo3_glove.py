#! /usr/bin/env python3
'''
* CSE520 Real-Time Systems
* Demo 3 (Final Demo) Glove Sensor Data Collection Service
* Jeremy Manin
'''

# Import utility libs
import time
import os
# Import AWS IoT Core libs
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import json
# Import LED lib
from gpiozero import LED
# Import Adafruit base libs
import board
import busio
import digitalio
# Import MCP3008 libs
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
# Import BNO055 lib
from Adafruit_BNO055 import BNO055

# Custom MQTT message callback
class CallbackContainer(object):

    def __init__(self, client):
        self._client = client
        self._state = False

    def customCallback(self, client, userdata, message):
        topicContents = json.loads(message.payload.decode('utf-8'))
        if(topicContents['state']['reported']['command'] == 'start'):
            self._state = True
        elif(topicContents['state']['reported']['command'] == 'stop'):
            self._state = False

    def getState(self):
        return self._state

# Create Status LED
led = LED(12)

# Setup MCP3008
## Create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
## Create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
## Create the mcp object
mcp = MCP.MCP3008(spi, cs)
## Create an analog input channels
chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)
chan3 = AnalogIn(mcp, MCP.P3)
chan4 = AnalogIn(mcp, MCP.P4)

# Setup BNO055
## Create BNO055 device
bno = BNO055.BNO055(serial_port='/dev/serial0', rst=13)
## Init connection to BNO055
bnoStarted = False
while not bnoStarted:
    try:
        bnoStarted = bno.begin()
    except RuntimeError:
        print('Error starting BNO! Retrying...')
        led.blink(0.1, 0.1, 5)
        time.sleep(1)
## Calibrate BNO055
cal_data = open('bno055_cal.dat', 'rb')
bno.set_calibration(cal_data.read())

# Setup AWS IoT
## Configure AWS IoT connection settings
host = "an91x6ytmr3ss-ats.iot.us-east-2.amazonaws.com"
scriptPath = os.path.dirname(os.path.realpath(__file__))
rootCAPath = os.path.join(scriptPath, "certs/root-CA.crt")
certificatePath = os.path.join(scriptPath, "certs/2db4660fce-certificate.pem.crt")
privateKeyPath = os.path.join(scriptPath, "certs/2db4660fce-private.pem.key")
port = 8883
clientId = "glove"
sensorDataTopic = "$aws/things/sensor_glove/shadow/update"
controlTopic = "$aws/things/glove_control/shadow/update"

## Configure AWS IoT logging
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

## Configure AWSIoTMQTTClient connection settings
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

## Connect to AWS IoT
myAWSIoTMQTTClient.connect()

## Subscribe to control topic
myCallbackContainer = CallbackContainer(myAWSIoTMQTTClient)
myAWSIoTMQTTClient.subscribe(controlTopic, 1, myCallbackContainer.customCallback)

time.sleep(2)
led.on()
print('System initialization complete.')

# Function to convert received analog voltage to percentage flex
def mapFlexToPercent(x, in_min, in_max):
    out_min = 0
    out_max = 100

    mappedVal = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Bounding
    if (mappedVal < out_min):
        mappedVal = out_min
    elif (mappedVal > out_max):
        mappedVal = out_max

    # Flip percent (was 100=no flex, now 100=max flex)
    return (mappedVal-100) * -1

# Publish to sensor data topic when control topic is received saying start until control topic says stop
while True:
    if(myCallbackContainer.getState()):
        imu_orient = bno.read_euler()

        flex_index = mapFlexToPercent(chan0.voltage, 1.87, 2.57)
        flex_mid = mapFlexToPercent(chan1.voltage, 2.02, 2.65)
        flex_ring = mapFlexToPercent(chan2.voltage, 2.18, 2.76)
        flex_pinky = mapFlexToPercent(chan3.voltage, 1.71, 2.54)
        flex_thumb = mapFlexToPercent(chan4.voltage, 1.35, 2.07)

        message = {}
        message['state'] = {}
        message['state']['reported'] = {}
        message['state']['reported']['flex_index'] = flex_index
        message['state']['reported']['flex_middle'] = flex_mid
        message['state']['reported']['flex_ring'] = flex_ring
        message['state']['reported']['flex_pinky'] = flex_pinky
        message['state']['reported']['flex_thumb'] = flex_thumb
        message['state']['reported']['imu_x'] = imu_orient[0]
        message['state']['reported']['imu_y'] = imu_orient[1]
        message['state']['reported']['imu_z'] = imu_orient[2]
        messageJson = json.dumps(message)

        myAWSIoTMQTTClient.publish(sensorDataTopic, messageJson, 1)

    time.sleep(1)
