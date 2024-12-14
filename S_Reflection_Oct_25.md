# Reflection - IoT Controller

## What I have learned: 

In this project, I learned how to integrate MQTT with Python to control IoT devices and manage conditions using structured data formats like JSON. I gained a deeper understanding of handling complex executions where multiple conditions need to be met to trigger an action. Additionally, I developed hands-on experience with distributed IoT systems and creating automated control systems.

## What I believe I need to improve: 

I need to enhance my debugging skills, particularly in addressing edge cases, such as missing MQTT data or ensuring conditions are evaluated consistently. We could also improve optimizing code efficiency to handle more complex scenarios, especially as the system grows larger with additional sensors and conditions.

## What the teacher could have said or done to make learning easier: 

The learning experience could have been improved with more examples or tutorials showcasing real-world MQTT applications in IoT systems. Guidance on structuring conditional logic and implementing robust error-handling mechanisms would also have been highly beneficial.

## What I could have done to make the learning easier: 

We could have spent more time experimenting with smaller, simpler MQTT programs before tackling the complete project. Building the understanding gradually would have helped me identify and resolve issues before they could even happen. Dedicating time to mastering advanced Python concepts like exception handling and working with dictionaries would have made the project easier to manage.

## Other reflections: 

Takeing part in this project has cultivated my problem-solving skills, particularly in dealing with IoT systems. I learned the importance of planning and breaking down complex tasks into manageable steps. Moreover, I realized the value of thoroughly testing individual components, such as handling MQTT messages, before integrating them into the overall system.

I also think that teamwork is great! Even though not everyone has their RPIs, we found a way to manage. We take turns codind when the teacher is guiding us. That way, one teammate types, another one wispers closer to the typer what the teacher just wrote on the board so the typer doesn't have to lift their head everytime, and the third teammate actually listens to what the teacher is sayind and asks questions accordingly.

# Linux and Python Commands Learned:

## Linux Commands:
`mosquitto` - Starts the MQTT broker.

`mosquitto_sub -h localhost -t "#" -v`: Subscribes to all MQTT topics on the local broker, helping to monitor messages in real time.

`mosquitto_pub -h localhost -t "topic" -m "message"`: Publishes an MQTT message to a specific topic, simulating a sensor or device.

## Python Commands (from the updated code):

`paho.mqtt.client as mqtt`: Imports the MQTT client library, enabling the Python script to connect to an MQTT broker.

`client.loop_forever()`: Keeps the MQTT client running, continuously listening for messages and triggering events based on the data received.

`try...except`: Used for error handling when parsing MQTT messages, ensuring that the system doesn’t crash if unexpected data is received.

`client.publish(topic, message)`: Sends an MQTT message to a specific topic, triggering actions in other connected devices based on the rules defined.

##### These commands are crucial in setting up, running, and debugging the IoT system.

