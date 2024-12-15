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

* `sudo nano /etc/systemd/system/IoT_Controller.service` - Opens the Nano text editor with root privileges to edit the service file.
* `sudo systemctl daemon-reload` - Reloads `systemd` to recognize changes made to service files. 
* `sudo systemctl enable IoT_Controller.service` - Enables the IoT Controller service to start automatically at boot.
* `sudo systemctl start IoT_Controller.service` - Starts the IoT Controller service manually without rebooting.
* `sudo systemctl status IoT_Controller.service` - Checks the status of the service, including logs and errors.
* `sudo apt-get install python3-matplotlib` - Installs the `matplotlib` package system-wide for Python.


## Python Commands (from the updated code):

* `ExecStart=/home/username/IoT_Controller/IoT/bin/python /home/username/IoT_Controller/IoT_Controller.py` - Specifies the command to execute the `IoT_Controller.py` script using the Python interpreter from a virtual environment.
* `WorkingDirectory=/home/username/IoT_Controller/` - Sets the working directory for the script execution.
* `Restart=always` - Configures the service to restart automatically if it crashes or stops unexpectedly.
* `User=username` - Sets the user under which the service runs to manage permissions and secure the execution environment. 



##### These commands are crucial in setting up, running, and debugging the IoT system.

# About the LIA: DuckPen - Heating System - IoT Project

## Progress so Far
We have successfully implemented the following features:

#### ESP32 Integration

* The __ESP32__ reads temperature and light data using a DHT11 sensor and a photocell sensor.
* LEDs indicate system states: red (high temperature), green (optimal temperature), blue (cold temperature), and yellow (heater activity).

#### MQTT Communication

* The ESP32 communicates with the MQTT broker using the PubSubClient library.
* Topics include:
  * Temperature states: cage/temphot, cage/tempnorm, cage/tempcold.
  * Light level: cage/nighttime.
  * Heater control: cage/heater.

#### Automation and Interactivity
* Automated responses are triggered based on MQTT messages:
  * LEDs toggle based on MQTT messages.
  * The heater is controlled via MQTT commands, with visual feedback from a yellow LED.
* Sensor data is periodically published to relevant topics, ensuring real-time updates.


#### Challenges Encountered

* Wi-Fi and Network Issues: Due to the restrictive school Wifi network, we had difficulty connecting the ESP32. Resolved by switching to the teacher's less restrictive network.
* Sensor Calibration: Adjusted thresholds and added delays for accurate readings.
* MQTT Debugging: Implemented reconnection logic to address intermittent disconnections.

#### Areas for Improvement

* Sensor Efficiency: Upgrade to more accurate sensors like the DHT22.
* Code Optimization: Separate code into modular components for better maintainability.
* Scalability: Expand to manage multiple cages with a hierarchical topic structure.

#### Lessons Learned

* Technical Skills: Enhanced understanding of embedded systems and networking.
* Problem-Solving: Debugging taught persistence and systematic approaches.
* Collaboration: Effective teamwork proved crucial in overcoming challenges.

#### Next Lab

* **Finalize** testing on a home network and tweek code accordingly.
* **Document** the system by creating a user manual and technical report.
* Prepare a **demonstration** showcasing real-time MQTT communication and system responsiveness.
