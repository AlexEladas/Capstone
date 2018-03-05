import smbus
import math
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c


def read_byte(reg):
    return bus.read_byte_data(address, reg)


def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg + 1)
    value = (h << 8) + l
    return value


def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val


def dist(a, b):
    return math.sqrt((a * a) + (b * b))


def get_y_rotation(x, y, z):
    radians = math.atan2(x, dist(y, z))
    return -math.degrees(radians)


def get_x_rotation(x, y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)


bus = smbus.SMBus(1)  # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68  # via i2cdetect

# Activate to be able to address the module
bus.write_byte_data(address, power_mgmt_1, 0)

Gx = read_word_2c(0x43)/131
Gy = read_word_2c(0x45)/131
Gz = read_word_2c(0x47)/131

Ax = read_word_2c(0x3b)/16384.0
Ay = read_word_2c(0x3d)/16384.0
Az = read_word_2c(0x3f)/16384.0

Atotal = math.sqrt((Ax^2 + Ay^2 + Az^2))
Gtotal = math.sqrt((Gx^2 + Gy^2 + Gz^2))

CLK=12
MISO=23
MOSI=24
CS=25
mcp=Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

print("| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |".format(*range(8)))
print("-" * 57)

while True:
    values = [0]*8
    for i in range(8):
        values[i] = mcp.read_adc(i)
        if i > 4:
            Gx = read_word_2c(0x43) / 131
            Gy = read_word_2c(0x45) / 131
            Gz = read_word_2c(0x47) / 131

            Ax = read_word_2c(0x3b) / 16384.0
            Ay = read_word_2c(0x3d) / 16384.0
            Az = read_word_2c(0x3f) / 16384.0

            Atotal = math.sqrt((Ax ^ 2 + Ay ^ 2 + Az ^ 2))
            Gtotal = math.sqrt((Gx ^ 2 + Gy ^ 2 + Gz ^ 2))

            values[i] = Atotal
            values[i + 1] = Gtotal
            break
    print("|{0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |".format(*values))
    time.sleep(0.5)