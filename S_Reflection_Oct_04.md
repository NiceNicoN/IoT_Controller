## What I have learned: 

To recap what we have done so far, we have learned to set up and configure an MQTT client in Python using the paho-mqtt library. I now understand how to connect to the MQTT message broker, and how to use the Publish-Subscribe Model to subscribe to topics and to process the incoming published messages. As we do more of these labs, I feel more confident programing, developing code, and understanding and troubleshooting the basic errors that can occur in Python, particularly when working with various types of message payloads.

## What I believe I need to improve: 

I want to enhance my understanding of efficiently structuring callbacks and managing high volumes of messages. I also aim to improve my ability to understand and develop better more compex MQTT topics in order to work with larger data sets. Gaining a deeper familiarity with MQTT protocols and message flow will be crucial for scaling the system as the project evolves.
How to understand the syntax better? I often confuse these symnols `<` `>`.

## What the teacher could have said or done to make learning easier: 

* I like exemple the teacher is currently guiding us on. I just wish it was something more interesing than just tempeture.
* I also want a better understanding of how we should chose our topics.
* Maybe next year it would be a good idea to also develop a log/chart of troubleshooting protocols.

## What I could have done to make the learning easier: 

* Haveving my RPI with me to code along with everyone else would have deffinetly helped me develop a better memory of the most commonly used functions and develop my motor skills.
* I should do more proactive reasearch and studying. Reviewing more background material on MQTT communication on my own would definetlly do me favors.

## Other reflections: 

Although we’ve just begun covering the fundamentals, it’s already clear how critical it is to effectively manage the communication protocol and message flow in IoT systems. This project provides an excellent opportunity to enhance my programming skills and deepen my understanding of real-time data processing.

I also think that teamwork is great! Even though not everyone has their RPIs, we found a way to manage. We take turns codind when the teacher is guiding us. That way, one teammate types, another one wispers closer to the typer what the teacher just wrote on the board so the typer doesn't have to lift their head everytime, and the third teammate actually listens to what the teacher is sayind and asks questions accordingly.

# Linux and Python Commands Learned:

## Linux Commands:
`sudo apt install mosquitto mosquitto-clients` : This command installs the Mosquitto MQTT broker and client tools on the Raspberry Pi, allowing for local MQTT communication.
      
`systemctl start mosquitto` : Starts the Mosquitto MQTT broker service, enabling the system to handle MQTT messaging.

## Python Commands (from the code):
`import paho.mqtt.client as mqtt` : Imports the Paho MQTT client, which is used to manage MQTT communication.

`mqtt.Client()` : Creates a new MQTT client instance to send and receive messages.

`client.on_message = IOT_Controller.on_message` : Assigns a callback function (on_message) to handle incoming messages. By using `IOT_Controller.on_message`, I am referencing a method defined at the class level, rather than an instance-specific method. This is a direct reference to the method `on_message` within the `IOT_Controller class`.

`client.connect("localhost", 1883)` : Connects the client to the local MQTT broker running on port 1883.

`client.subscribe("**")` : Subscribes to all topics (using wildcard **), enabling the controller to receive messages on any topic.

`client.loop_forever()` : Keeps the client running in an infinite loop to continuously listen for and process messages.
