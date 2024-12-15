
# Reflection - Durring the Lab - IoT Controller

## What I have learned: 

This lab provided valuable insights into IoT systems and database integration. Specifically, we learned:

* How to utilize the `paho.mqtt` library in Python to establish MQTT connections, subscribe to topics, and process incoming messages.
* We learned how to install and verify the SQLite3 client on a Raspberry Pi, execute SQL commands to interact with a database, and set up a historian program to log MQTT messages in real-time. 
* Techniques for creating database tables dynamically and storing incoming MQTT messages with relevant metadata, such as timestamps, topics, and payloads.
* The importance of recording data systematically to analyze IoT system behavior and troubleshoot communication issues effectively.
* Using Python’s `datetime` module to incorporate timestamps for temporal context in the logged data records.
* Debugging techniques that ensure reliable message handling and seamless database operations.

## What I believe I need to improve: 

__Error Handling:__

While implementing the historian, we relied on basic functions to handle MQTT messages and database interactions. However, the system lacks robust error handling, such as for cases when the database connection fails or malformed messages are received. Improving this aspect would make the application more reliable.

__Performance Optimization:__

As the database grows, querying and inserting records might become slower. Understanding indexing and optimizing database operations could ensure scalability for larger datasets.

__Data Visualization:__

Enhance my skills in creating dashboards or visual representations of MQTT data to make analysis more intuitive and actionable.

## What the teacher could have said or done to make learning easier: 

__Provide Clear Examples:__

Sharing a simple example that integrates MQTT and SQLite could have accelerated the learning process and clarified concepts.

__Debugging Tools:__

Recommending tools like MQTT Explorer for monitoring MQTT traffic would have simplified troubleshooting and testing.

__Discuss Best Practices:__

Introducing industry-standard practices for IoT data logging and MQTT security, such as authentication and encryption, would have added depth to our understanding.

## What we could have done to make the learning easier: 

__Better Preparation:__

Reviewing documentation for MQTT and SQLite in Python prior to the lab could have provided a stronger foundation.

__Incremental Testing:__

Testing the program in smaller, modular parts rather than as a whole would have made it easier to isolate and address errors.

__Asking for Help:__

Asking more questions to my peers and my teacher during the lab to clarify uncertainties in real time would have enhanced my comprehension of the activity.

## Other reflections: 

This lab emphasized the importance of bridging theoretical knowledge with practical applications. It highlighted areas where I need improvement, such as optimizing database operations and enhancing debugging skills. Additionally, the experience reinforced the value of systematic data documentation and analysis, which are critical in developing scalable IoT systems.

In the following labs, I plan to deepen my understanding of IoT protocols and focus on creating reliable, secure solutions for future projects.

# Linux and Python Commands Learned:

## Linux Commands:
`mosquitto` - Starts the MQTT broker.

`mosquitto_sub` - Subscribes to an MQTT topic to receive messages.

`mosquitto_pub` - Publishes messages to a specified MQTT topic.

`sqlite3` 
 - **Purpose**: Interacts with SQLite databases via the command line.
 - **What it does**: Enables creating, querying, and modifying database files.

`top`
 - **Purpose**: Monitors system processes.
 - **What it does**: Displays real-time CPU and memory usage for system optimization.

## Python Commands (from the updated code):

`mqtt.Client()`
 - **Purpose**: Creates an MQTT client instance.
 - **What it does**: Initiates a connection with the MQTT broker.

`client.subscribe()`
 - **Purpose**: Subscribes to an MQTT topic.
 - **What it does**: Tells the broker to send messages from a specific topic to the client.

`sqlite3.connect()`
 - **Purpose**: Connects to an SQLite database file.
 - **What it does**: Opens a database or creates one if it doesn’t exist.

`datetime.now().strftime()`
 - **Purpose**: Formats the current date and time.
 - **What it does**: Generates timestamps in a readable format for logging.

`cursor.execute()`
- **Purpose**: Executes SQL commands in the database.
- **What it does**: Allows querying, creating tables, or inserting data into the database.


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
* Obtain a miniUSB cable capable of transferring DATA.


