# Reflection - Lab 9 - IoT System Automated Startup

## What we have learned: 

#### Topic-Specific Learning
This lab introduced me to `systemd` as a tool for automating IoT system startups on Raspberry Pi devices. I learned how to create, configure, and enable custom services to manage various components of an IoT system, including controllers, data historians, and web interfaces.

#### Technical Understanding
* I now understand the structure and purpose of systemd service files, including key directives like `ExecStart`, `WorkingDirectory`, and `Restart`.
* I gained practical knowledge of ensuring Python virtual environments are correctly referenced within service files, preventing dependency-related issues.
* Troubleshooting errors with systemd commands like `sudo systemctl status` gave me a deeper understanding of debugging service-related problems.

#### Practical Skills
*Configuring system-wide packages for compatibility (e.g., solving the matplotlib issue) taught me to identify and resolve dependency conflicts.
* Automating startup processes through sudo systemctl enable ensures IoT applications reliably launch after reboots.

## What I believe I need to improve: 

#### Debugging Systemd Services
I struggled to identify issues when a service failed to start. While I eventually resolved them, I need to improve my ability to interpret systemd logs (`journalctl -u service_name`) to diagnose errors more effectively.

#### Managing Dependencies
The need for a system-wide installation of `matplotlib` highlighted gaps in my understanding of managing Python environments. I plan to study best practices for handling dependencies, especially in mixed environments like virtual environments and system-wide installations.

## What the teacher could have said or done to make learning easier: 

#### Provide Context for Common Issues
Highlighting typical pitfalls (e.g., dependency conflicts or file permission errors) and how to address them would have helped me anticipate and resolve issues faster.

#### Pre-Built Examples
Providing a pre-configured service file template for the lab’s specific applications would have allowed me to focus more on understanding its functionality instead of spending time on trial-and-error adjustments.

## What I could have done to make the learning easier: 

#### Preparation
Reviewing systemd documentation and understanding its core concepts beforehand would have made me more confident in creating and managing services. Additionally, revisiting Python virtual environment usage could have prevented the dependency conflict I encountered.

#### Experimentation
Testing simpler services before tackling the IoT system components could have helped me build a stronger foundation for understanding systemd configuration.

## Other reflections: 

#### Adaptability
This lab reinforced the importance of adaptability when facing unexpected issues like the `matplotlib` conflict. Problem-solving in a dynamic environment like IoT projects is a skill I am actively improving.

#### Collaboration
While this was an individual task, discussing challenges and solutions with peers provided valuable insights. Learning from others’ approaches broadened my perspective.

#### Attention to Detail
Small errors in service files, such as typos in file paths or incorrect `ExecStart` commands, had significant impacts. This highlighted the need for meticulous attention to detail, a critical skill in both programming and system configuration.

# Linux and Python Commands Learned:

## Linux Commands:

* Opens the Nano text editor with root privileges to edit the service file.
```
sudo nano /etc/systemd/system/IoT_Controller.service
```
* Reloads `systemd` to recognize changes made to service files.
```
sudo systemctl daemon-reload
```
* Enables the IoT Controller service to start automatically at boot.
```
sudo systemctl enable IoT_Controller.service
```
* Starts the IoT Controller service manually without rebooting.
```
sudo systemctl start IoT_Controller.service
```
* Checks the status of the service, including logs and errors.
```
sudo systemctl status IoT_Controller.service
```
* Installs the `matplotlib` package system-wide for Python.
```
sudo apt-get install python3-matplotlib
```


## Python Commands (from the updated code):

* Specifies the command to execute the `IoT_Controller.py` script using the Python interpreter from a virtual environment.
```
ExecStart=/home/username/IoT_Controller/IoT/bin/python/home/username/IoT_Controller/IoT_Controller.py
```
* Sets the working directory for the script execution.
```
WorkingDirectory=/home/username/IoT_Controller/
```
* Configures the service to restart automatically if it crashes or stops unexpectedly.
```
Restart=always
```
* Sets the user under which the service runs to manage permissions and secure the execution environment. 
```
User=username
```

##### These commands are crucial in setting up, running, and debugging the IoT system.

# Final LIA Reflection: DuckPen - Heating System - IoT Project

## Project Overview
In this project, we built an IoT-based control system using an ESP32 microcontroller, the MQTT protocol, and a variety of sensors and actuators. The system was designed to monitor environmental parameters such as temperature and light intensity, and to control devices like heaters and fans accordingly. The primary goal was to ensure reliable communication between components and enable real-time device control using MQTT.

## Successes and Achievements

### Demonstration
We have successfully implemented and demostrated the following features:

#### System Integration
Integrating the ESP32 with MQTT was a significant accomplishment. The system now collects environmental data, processes it, and responds to remote commands in real time. This integration is the backbone of the project, enabling seamless communication between devices and users.

#### Remote Device Control
A major success was achieving remote control of actuators via MQTT. By publishing messages to topics like `mqtt_hot_topic` and `mqtt_cold_topic`, we could activate or deactivate the heater and fan. This enabled real-time system feedback, making it interactive and user-friendly.

#### Continuous Data Monitoring
We implemented a periodic data publishing mechanism that sent sensor readings every three seconds. This provided a steady stream of information about temperature, light levels, and system status, offering valuable insights for system optimization.

## Areas for Improvement
#### Error Handling and Robustness
While the system performs well under normal conditions, it could be improved with better error handling. Adding validations for extreme sensor readings and implementing fail-safes like watchdog timers for MQTT reconnection would enhance its robustness.

#### Security Enhancements
Currently, MQTT communication lacks encryption, making it vulnerable to potential breaches. Adding TLS (Transport Layer Security) would secure data transmission and improve system reliability for real-world applications.

#### Scalability
The system is currently designed for a limited number of sensors and actuators. Scaling up will require more sophisticated control logic, such as event-driven programming or advanced state management, to maintain performance and usability.

## Teamwork and Collaboration
Working as a team was an enriching experience. Each member brought unique skills, enabling us to address challenges effectively and deliver a functional, well-rounded system.

#### Task Division
We divided tasks based on individual strengths: some focused on hardware integration and sensor handling, while others worked on MQTT broker setup and communication. This parallel approach sped up development and ensured efficient progress across all areas.

#### Communication and Documentation
Regular team meetings helped address challenges and make critical design decisions. We documented progress in shared files, ensuring everyone stayed informed and redundancy was avoided.

#### Collaborative Troubleshooting
Debugging was a collective effort. Challenges like MQTT connectivity or actuator control were resolved through brainstorming and teamwork, which not only improved the system but also deepened our understanding of IoT technologies.

For future projects, we aim to incorporate more structured planning and time management to further streamline collaboration.

## Learning Experience
This project provided valuable insights into IoT systems, particularly in sensor integration, real-time communication, and actuator control. Key takeaways include:

* Setting up and utilizing MQTT for efficient device communication.
* Processing sensor data and responding to real-time environmental changes.
* Addressing connectivity and reliability challenges with ESP32 and MQTT.
* Refactoring code to manage increasing system complexity.

Collaborating with the team also enhanced both my technical expertise and interpersonal skills, allowing us to learn from one another’s strengths.

## Future Enhancements
Looking ahead, we plan to:

* **Integrate Cloud Platforms:** Using services like AWS or Google Cloud for centralized monitoring and control, enabling remote access from anywhere.
* **Develop a Mobile App:** Creating a mobile interface for easier and more intuitive system control.
* **Incorporate Machine Learning:** Adding predictive capabilities to optimize system performance based on trends in environmental data.

## Conclusion
This project was an excellent opportunity to apply IoT concepts in a practical setting. By integrating the ESP32 with MQTT and various sensors, we created a functional, interactive system. The challenges we faced helped us grow both technically and as a team, and the system’s scalability and adaptability offer exciting potential for future enhancements.

