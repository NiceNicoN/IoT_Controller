

# Pseudocode: IoT Controller System with Raspberry Pi, ESP32, and Arduino

 *Here’s an updated pseudocode integrating both a Raspberry Pi (running as the main MQTT broker and controller) and an ESP32-Arduino system. The Raspberry Pi will handle MQTT communication, while the ESP32-Arduino setup will handle local sensor and actuator control. The ESP32 will communicate with the Raspberry Pi over MQTT, and the Arduino will communicate with the ESP32 over Serial.*


## 1. Initialize System Components

### Raspberry Pi:

  * Install and run the MQTT broker.

  * Create an MQTT client to handle rules and system actions.

  * Set up callback functions to handle incoming MQTT messages.

  * Connect to the local MQTT broker and subscribe to all relevant topics.


### ESP32:

  * Set up MQTT client to communicate with Raspberry Pi’s broker.

  * Set up callback functions to handle incoming messages.

  * Establish Serial communication with Arduino (e.g., baud rate 9600).


### Arduino:

* Initialize sensors (temperature, light, etc.) and actuators (e.g., LED lights, heater).

* Establish Serial communication with ESP32.




## 2. Define Rules on Raspberry Pi

* Specify a list of rules where each rule includes:

  * Conditions: topic, comparison operator (==, >, <), and target value.

  * Actions: MQTT topic to publish to, value to send, and message to log.




## 3. Main Program Loop on Raspberry Pi

* Start the MQTT client loop to continuously listen for incoming MQTT messages.

* Continuously evaluate the rules to determine if any actions should be triggered based on current MQTT data.


## 4. Data Exchange Between Devices

**ESP32 to Raspberry Pi:**

  * ESP32 publishes sensor data (from Arduino) to relevant MQTT topics.


**Raspberry Pi to ESP32:**

  * When a rule triggers an action (e.g., turn on heater), publish the command to the MQTT topic subscribed by the ESP32.


**ESP32 to Arduino:**

  * ESP32 receives commands from Raspberry Pi via MQTT and forwards relevant commands to Arduino over Serial.




## 5. Data Collection and Processing on ESP32-Arduino System

**Arduino:**

  * Periodically read sensor data (e.g., temperature, light level).

  * Send structured data (e.g., {"sensor":"temp", "value":30}) over Serial to ESP32.


**ESP32:**

  * Receive sensor data from Arduino over Serial.

  * Parse data and publish it to the MQTT broker running on Raspberry Pi.




## 6. On MQTT Message Received (Raspberry Pi)

Decode the message payload and extract the topic and value.

Update the mqtt_data dictionary with the received data for reference in rules evaluation.



## 7. Filter Out Duplicate Messages (Raspberry Pi)

Use a message_log to identify and ignore messages previously sent by the controller within a specified timeframe.



## 8. Rule Evaluation and Action Triggering (Raspberry Pi)

**For each rule in rules:**

 - Set conditions_met to True.

**For each condition:**

 - Check if the topic exists in mqtt_data.

 - Compare mqtt_data values with condition requirements.

 - If any condition fails, set conditions_met to False.


**If all conditions are met:**

 - Execute the action by publishing to the corresponding MQTT topic.

 - Log the action in message_log to avoid repeated actions.

 - Send command to ESP32 if action relates to an actuator controlled by Arduino.





## 9. Action Execution on ESP32-Arduino

**ESP32:**

  * Receives commands from Raspberry Pi over MQTT.

  * Parses action commands and forwards them to Arduino over Serial.


**Arduino:**

  * Receives commands from ESP32 over Serial.

  * Activates actuators based on received commands (e.g., turn on LED, heater).




## 10. Condition Evaluation Function (Raspberry Pi)

  * Define a function on Raspberry Pi that:

  * Fetch the core conditions and actions that have been saved in a separate json rules file)

  * Evaluates if conditions are met based on operators (>, >=, <, <=, ==).

  * Returns True if condition is satisfied, else False.




## 11. Arduino Continuous Loop

* Periodically reads sensor data (e.g., every 5 seconds).

* Sends sensor readings to ESP32 over Serial.

* Listens for Serial commands from ESP32 to activate actuators.

