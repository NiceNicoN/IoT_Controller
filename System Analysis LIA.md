
# System Analysis: Final Project - Duck Heater Simulation 

 System Overview 

  Our project simulates a heater for ducks using an ESP32 board, Raspberry Pi, temperature sensors, and photocell sensors. The system is designed to monitor temperature and light levels, activating a heater or light depending on the environment. We will control the system via MQTT communication between the ESP32 and Raspberry Pi. 

 

## Applications and Tasks 

#### 1. ESP32: 

* Task: Collect temperature and light data from sensors (temperature sensor and photocell sensor). 

* Task: Send this data via MQTT to the Raspberry Pi. 

* Task: Receive commands from the Raspberry Pi to control the heater and LED lights. 

* Task: Handle input from the emergency and start buttons. 

 

#### 2. Raspberry Pi (IoT Controller): 

 * Task: Serve as the MQTT broker for communication. 

 * Task: Process incoming sensor data from the ESP32. 

 * Task: Evaluate conditions based on temperature and light data. 

 * Task: Send commands back to the ESP32 to turn on/off the heater and LEDs (green for optimal, blue for cold, red for hot). 

 * Task: Log data for performance analysis and troubleshooting. 

 

## Conditions and Results 

#### 1. Temperature Sensor Conditions: 

 * If temperature < 27°C, the system will turn on the heater and activate the blue LED. 

 * If 27°C ≤ temperature ≤ 31°C, the system will turn on the green LED, indicating an optimal temperature. 

 * If temperature > 31°C, the system will turn off the heater and activate the red LED, indicating it's too hot. 

 

#### 2: Light Sensor (Photocell) Conditions: 

 * If light level low in the environment is observed, it is night, Photocell will send a signal to ESP32, which will send it to MQTT server which will make a decision, which will 

 

#### 3. Light Actuator Conditions: 

* If heater is turned on (True), the system will turn on the yellow LED, indicating the heater is running. 

* If the photocell sensor detects low light value (night conditions), the security white LED will turn on for safety. 

* If the photocell sensor detects high light value (day conditions), the white LED turns off. 

 

#### 4. Emergency and Start Buttons: 

* The emergency button will override the system, turning off the heater immediately if it’s not responding correctly. 

* The start button will initiate the system process, allowing the heater and LEDs to function according to sensor readings. 

 

## Additional Considerations 

 

**MQTT Communication:** The ESP32 will publish sensor data to specific topics (e.g., cage/temp, cage/light), while the Raspberry Pi will subscribe to these topics to process the data and trigger the appropriate actions. 

 

**Safety Mechanisms:** The emergency button ensures safety by giving manual control to stop the heater in case of malfunction. 

 

**Historian (Data Logging):** We will implement a data logging system to track system behavior over time, which can help in diagnosing issues and improving system performance. 
