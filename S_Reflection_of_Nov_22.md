
# Reflection - Durring the Lab - IoT Controller

## What we have learned: 

__Topic-Specific Learning__

We gained practical experience with the __MQTT protocol__, learning how it enables real-time communication between devices. For instance, we used `mosquitto_pub` and `mosquitto_sub` commands to publish and subscribe to topics, allowing seamless data exchange in IoT systems.

__Technical Understanding__

We explored the paho-mqtt Python library, which simplifies writing and debugging MQTT client code. Through this, we implemented key methods like `on_connect` for connection setup and `on_message` for handling incoming messages.

__Practical Skills__

We developed troubleshooting skills for establishing MQTT connections within secure network environments. This included configuring network settings, managing Wi-Fi constraints, and analyzing message flow using logging techniques.

## What I believe we need to improve: 

__Error Troubleshooting__

We faced some challenges debugging connectivity issues when switching between networks. Improving my understanding of network configurations and interpreting logs will help resolve these problems more efficiently.

__Efficiency in Writing Code__

The Python scripts worked but were quite loaded. We aim to write more modular and reusable code by leveraging advanced debugging tools and improving coding practices.

## What the teacher could have said or done to make learning easier: 

__Pre-Configured Tools__

Providing a pre-configured virtual tool with all required dependencies could have reduced time spent troubleshooting setup issues and allowed more focus on the core task.

__Contextual Examples__

Demonstrating how MQTT is applied in real-world scenarios, such as industrial automation or smart homes, would have made the concepts more relatable and engaging.

## What we could have done to make the learning easier: 

__Preparation__
Reviewing the Linux commands and the paho-mqtt library documentation beforehand would have created a clearer starting point.

__Incremental Testing:__

Testing the program in smaller, incremental sections rather than it as a whole would have made it easier to isolate and address compound errors, as well as streamline the workflow.

__Asking for Help:__

Asking more questions to my peers and my teacher during the lab to clarify uncertainties in real time would have enhanced my comprehension of the activity.

## Other reflections: 

__Adaptability__

Working around different networking constraints enhanced my adaptability, a critical skill for real life IoT projects which were created in varied environments and under different circumstances.

__Collaboration__

Collaborating with peers helped resolve issues more quickly, demonstrating the importance of teamwork in technical problem-solving.

__Time Management__

Planing and designated time outside the classroom for debugging is essential. In upcoming projects, I plan to reserve dedicated time slots for this purpose to avoid last-minute challenges.

# Linux and Python Commands Learned:

## Linux Commands:

**`mosquitto`**
 - **Purpose:** Starts the MQTT broker.

**`mosquitto_sub`** 
 - **Purpose:** Subscribes to an MQTT topic to receive messages.

**`mosquitto_pub`** 
 - **Purpose:** Publishes messages to a specified MQTT topic.

**`ifconfig`**
 - **Purpose:** Displays or configures network interfaces. Useful for checking IP addresses and network status.

**`ping`**
 - **Purpose:** Tests connectivity between devices.
 - **Example:** `ping 192.168.1.1` checks if a device at that IP address is reachable.

**`nano` and `vim`**
 - **Purpose:** Text editors for modifying scripts or configuration files directly in the terminal.

**`chmod`**
 - **Purpose:** Changes file permissions.
 - **Example:** `chmod +x script.py` makes a Python script executable.

**`systemctl`**
 - **Purpose:**  Controls system services.
 - **Example:** `systemctl restart mosquitto` restarts the MQTT broker service.

**`top`**
 - **Purpose:**: Monitors system processes.
 - **What it does:** Displays real-time CPU and memory usage for system optimization.

## Python Commands (from the updated code):

**`import paho.mqtt.client as mqtt`**
 - Imports the MQTT library to allow connection, subscription, and message publishing.

**`client = mqtt.Client()`**
 - Creates an MQTT client object.

**`client.connect(broker, port, keepalive)`**
 - Establishes a connection to the MQTT broker.

**`client.subscribe("topic")`**
 - Subscribes to a topic to receive messages.

**`client.publish("topic", message)`**
 - Publishes a message to a topic.

**`client.loop_forever()`**
 - Keeps the client running to handle incoming messages.

**`logging.basicConfig()`**
 - Configures logging to track events, useful for debugging.

**`time.sleep(seconds)`**
 - Introduces a delay in execution, useful for timing message flows.



##### These commands are crucial in setting up, running, and debugging the IoT system.

## About the LIA:

Durring the lab time we tried to test the Arduino code I developped with the Rasberry Pi containing the IoT Controller code we had just updated. For some reason the Raspberry Pi just did not want to establish communication with the ESP32. Turns out the MiniUSB cable we were using was incapable of __transmitting__ DATA. 

Moreover, though I am very confident in my Arduino Programing Skills, I still have a lot to learn and to improve. I need do find a more efficient way to determine my inputs, outputs and variables because I forgot quite a few when I made the Arduino code.

Here is a comprehensive list of objectives I bielieve we need to achive in order to complete our LIA Project.

* Add a topic for the `heater` in our Python code.
* For now, in the Arduino code, I have assigned the topic `nighttime` to be in charge of the White LED. Python code must be updated to reflect that.
* Might use `daytime` topic to control the White LED durring daytime when __light value__ is LOW. Based on a 24H clock.
* We must create a __Web Interface__??? based on the LIA project directions. (What is that???)
* Add a __historian__.
* Check and update the Green LED rules < and >.
* New pins were added. Check and document.
* Ask the teacher to clarify if the outputs are triggered by the ESP32 or should it have been by python??
* **Idea:** We can 3d print parts for our project!
* Add a flip switch. Hardware and Software.
* We must update our schematic!
