#! /usr/bin/env python3
'''
* CSE520 Real-Time Systems
* Machine Learning Training Data Collection Script
* Jeremy Manin
*
* Usage: python3 collect_training_data.py <output_file> <data classification>
'''

# Import utility libs
import time
import sys
# Import Adafruit base libs
import board
import busio
import digitalio
# Import BNO055 lib
import adafruit_bno055
# Import MCP3008 libs
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Create BNO055 device
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)

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

# Open output file as specified by user
output_file = open(str(sys.argv[1]), 'w')

# Get classification of data from command line to tag captured data with
data_class = str(sys.argv[2])

i = 0

# Writes N samples of sensor data to file
while i<10:
    # Get sensor data
    imu_orient = sensor.euler

    flex_index = mapFlexToPercent(chan0.voltage, 1.87, 2.57)
    flex_mid = mapFlexToPercent(chan0.voltage, 2.02, 2.65)
    flex_ring = mapFlexToPercent(chan0.voltage, 2.18, 2.76)
    flex_pinky = mapFlexToPercent(chan0.voltage, 1.71, 2.54)
    flex_thumb = mapFlexToPercent(chan0.voltage, 1.35, 2.07)

    # Output to file in format "x,y,z,index,middle,ring,pinky,thumb,class"
    output_file.write(str(imu_orient[0]) + ',' + str(imu_orient[1]) + ',' + str(imu_orient[2]) + ',' + str(flex_index) + ',' + str(flex_mid) + ',' + str(flex_ring) + ',' + str(flex_pinky) + ',' + str(flex_thumb) + ',' + data_class + '\n')

    i += 1

    time.sleep(1)

output_file.close()