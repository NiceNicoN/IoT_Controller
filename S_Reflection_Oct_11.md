# Reflection - IoT Controller

## What you have learned: 

At this stage, we learned to implement condition-based rules in an IoT system using Python code and the MQTT broker. This has given us the capability to define specific actions triggered by incoming messages, such as changeing the state of the temperature  by turning the AC __`ON`__ or __`OFF`__. In addition to that, I gained experience in writing comparison logic and ensuring the system automatically responds based on the predefined conditions.

## What you believe you need to improve: 

I want to improve my control upon the more complicated rule sets. The current implementation works for simple conditions, but I would like to add the conditions that require a more complicated logic, such as multiple requirements triggering a single action. Debugging the logic behind message handling and actions triggered by different topics could also be more efficient.
I want to understand the syntax better? I often confuse these symnols `<` `>`.

## What the teacher could have said or done to make learning easier: 

Providing more detailed guidance on the structure of IoT rules, along with examples of advanced MQTT workflows, would be very helpful. A tutorial focused on efficiently testing IoT systems in real-time, particularly for handling message delays or errors, could have significantly sped up the process.

## What you could have done to make the learning easier: 

I could have better prepared by researching the design of condition-based systems in IoT beforehand, which might have reduced some of the trial and error during the coding process. Additionally, experimenting with more loaded use cases and testing a broader range of inputs and outputs exemples would have made the implementation smoother.

## Other reflections: 

This part of the project underscored the importance of thoughtful planning when designing condition-handling logic. I realized that creating scalable and maintainable IoT systems requires a solid understanding of both hardware components and the logical processes that govern them. Moving forward, I intend to build reliable systems to manage more intricate conditions and actions effectively.

I also think that teamwork is great! Even though not everyone has their RPIs, we found a way to manage. We take turns codind when the teacher is guiding us. That way, one teammate types, another one wispers closer to the typer what the teacher just wrote on the board so the typer doesn't have to lift their head everytime, and the third teammate actually listens to what the teacher is sayind and asks questions accordingly.

# Linux and Python Commands Learned:

## Linux Commands:
`sudo apt install mosquitto mosquitto-clients` : This command installs the Mosquitto MQTT broker and client tools on the Raspberry Pi, allowing for local MQTT communication.
      
`systemctl start mosquitto` : Starts the Mosquitto MQTT broker service, enabling the system to handle MQTT messaging.

## Python Commands (from the updated code):

***Comparison logic*** 

Added functions like:
```
condition_met()
```
To handle comparisons (`<` , `>` , `==` , etc.` )  between values.

`client.publish(topic, payload)` 

Sends a message to a specific MQTT topic, enabling action in the system based on the condition being met (e.g., publishing a message to turn on the AC).
