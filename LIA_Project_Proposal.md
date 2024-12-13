# Project Proposal 
## Duckling Safety Pen

For our LIA Project, our team came forth with this idea for the __Project Proposal__: a guarded pen for baby ducks. 

It will have tempeture sensors and a photosensor. It will have a heat lamp as an actuator. Sensors and actuators are connected to an ESP32 microcontroller. The Sensors will be activated, the data is sent to the ESP32, then it is sent to the Raspberry Pi. The RPI will use MQTT protocol to calculate, evaluate and do the decision makeing. Then the data is sent back to the ESP32 which then triggers the actuators. The ESP32, the Raspberry Pi  and the MQTT protocol are communicating over Wireless Networking Technology (WiFi).



## Explanation of How the LIA Final Project Works (with ESP32 and Raspberry Pi):
The project simulates a heater system for ducks using an ESP32 board and a Raspberry Pi for control and communication. Here's how it functions:

### Temperature Control:
The ESP32 reads data from a temperature sensor. If the temperature is too low, the system activates the heater, and when the desired range is reached, the heater turns off. LEDs indicate the temperature status: blue for too cold, yellow to indicate Heater is functioning, green for the right temperature, and red for too hot.

### Night Simulation:
The duckpen is inside but natural light shines in. A photocell sensor detects when the room light is too low(simulating nighttime). The photocell data is sent to the ESP32 and after recieving approval from the RPI, the ESP32 triggers a security light to turn on. 

### Emergency Button:
If the heater fails to stop, an emergency button can be pressed to shut it down.

### Start Button:
A start button allows the system to begin monitoring and controlling the temperature.

## How It Could Be Implemented in Real Life (with ESP32 and Raspberry Pi):
To make this system functional in real life:

### ESP32 Board:
The ESP32 would handle sensor inputs (temperature, photocell) and control the heater and LEDs based on predefined thresholds. It communicates wirelessly with the Raspberry Pi over MQTT.

### Raspberry Pi:
Acts as the central controller, managing the overall system logic, logging data, and possibly hosting a web interface to monitor and control the system remotely.

### Sensors and Actuators:
The temperature sensor and photocell would be connected to the ESP32. The heater and LEDs could be controlled directly by the ESP32 using GPIO pins.

### MQTT Protocol:
The Raspberry Pi and ESP32 communicate via MQTT, allowing for distributed control and status updates across the system.
