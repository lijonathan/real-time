import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin P#
chan = AnalogIn(mcp, MCP.P4)

i = 0;
sum = 0;

while i < 60:
    sum += chan.voltage
    i += 1
    time.sleep(0.5)

print('Average: ' + str(sum/60) + 'V')
