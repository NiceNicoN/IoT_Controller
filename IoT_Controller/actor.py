
import smbus
import time

class TemperatureSensor:
 def __init__(self, i2c_bus, i2c_address):
     # Constructor to initialize the sensor with I2C bus and address
     self.i2c_bus = i2c_bus
     self.i2c_address = i2c_address

 def get_temperature(self):
     # Method to convert temperature data from the I2C sensor
     data = self._read_sensor_data()
     temperature = ((data[0] & 0x0F) << 8) | data[1]
     temperature /= 16.0
     return temperature

 def _read_sensor_data(self):
     # Private method to read sensor data from the I2C device
     try:
         bus = smbus.SMBus(self.i2c_bus)
         # Read temperature data from the specified I2C address
         # In the datasheet for MCP9808, the temperature is stored in the
         # 0x5 register
         data = bus.read_i2c_block_data(self.i2c_address, 0x5, 2)
         return data
     except Exception as e:
         print(f"Error reading data from I2C sensor: {e}")
         return None

# I2C bus 1 is on SDA SCL pins 3,5 (physical)
i2c_bus_number = 1
# MCP9808 has a default I2C address of 0x18 (from the datasheet)
i2c_device_address = 0x18
# Creating a TemperatureSensor instance with I2C configuration
sensor = TemperatureSensor(i2c_bus=i2c_bus_number, i2c_address=i2c_device_address)
# Invoking the get_temperature method and displaying the result

while True:
 print(f"Temperature: {sensor.get_temperature():.2f}°C")
 time.sleep(1)
