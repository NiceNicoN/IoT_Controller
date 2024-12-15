# Reflection - Durring the Lab - IoT Controller

## What I have learned: 

Durring this lab we improved the code of our IoT_Controller by implementing logic to differentiate between sent and received messages. We introduced a `message_log` that will track outgoing messages, to prevent looping caused by the controller potentially reacting to its own actions. This adjustment improves reliability in the MQTT message handling of our IoT project. Additionally, we explored time-based filtering by incorporating timestamps into the `message_log`, allowing us to automatically discard outdated entries. This dynamic approach enhances data processing efficiency, particularly for handling time-sensitive sensor data.

## What I believe we need to improve: 

Our error-handling mechanism could be more reliable, especially for cases where data is missing or improperly formatted. Though the code skips rules with invalid topics without logging the errors. We are not satisfied because it limits debugging. Finding a way, perhaps a piece of code or a protocol, to improve the flexibility of our rules structure would greatly expand functionality. Presently, actions can only be triggered by specific rules. Developing code to support multiple actions across a diverse range of multiple topics to make our IoT system respond to complex, real-world scenarios would make it more realistic and alike other real-life renowned systems we encounter every day across multiple industries.

## What the teacher could have said or done to make learning easier: 

Providing examples of real-world applications for MQTT controllers would have added valuable context to the lab. I would have liked a more in depth understanding of the functions we were adding to our codes and explinations of how to use them appropriatelly, how does their logic work and how they come to be defined that way. Understanding practical use cases could help us make more informed decisions during development and better evaluate system requirements and limitations. Perhaps provide a chart of these functions or the resource that keeps track of all of them, like the Arduino official website.

## What we could have done to make the learning easier: 

Testing the code with physical devices could have helped us troubleshoot its issues earlier. Simulating multiple scenarios, would have detected the edge cases we did not foresee, the communication failures and the mishandled time-based data, might have uncovered gaps our current implementation lacks. This hands-on approach could improve both the design and functionality of our system.

## Other reflections: 

Takeing part in this project has cultivated my problem-solving skills, particularly in dealing with IoT systems. I learned the importance of planning and breaking down complex tasks into manageable steps. Moreover, I realized the value of thoroughly testing individual components, such as handling MQTT messages, before integrating them into the overall system.

I also think that teamwork is great! Even though not everyone has their RPIs, we found a way to manage. We take turns codind when the teacher is guiding us. That way, one teammate types, another one wispers closer to the typer what the teacher just wrote on the board so the typer doesn't have to lift their head everytime, and the third teammate actually listens to what the teacher is sayind and asks questions accordingly.

# Linux and Python Commands Learned:

## Linux Commands:
`mosquitto` - Starts the MQTT broker.

`mosquitto_sub` - Subscribes to an MQTT topic to receive messages.

`mosquitto_pub` - Publishes messages to a specified MQTT topic.

## Python Commands (from the updated code):

`time.time()` - Retrieves the current time in seconds, which we use to timestamp each message entry in the log, allowing us to track recent activity.

`.append()` - Adds entries to lists. Here, it allows us to log new messages in the message_log.

`try...except` - Used for error handling when parsing MQTT messages, ensuring that the system doesn’t crash if unexpected data is received.

##### These commands are crucial in setting up, running, and debugging the IoT system.

## About the LIA:

As part of my contribution to the LIA Project, I started developing the Arduino code for our IoT system. I was able to develop a working prototype for the ESP32. I learned about the callback function for Arduino and how to implement it into the code. The callback function proved itself crucial since we wanted to control our physical actuators with the ESP32 with the orders recieved from the MQTT broker. All in all, I really liked this expirience. I felt usefull to the team and proud to put in tangible work into our project.




