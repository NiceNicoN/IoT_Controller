
// Include the necessary libraries
#include <WiFi.h>
#include <PubSubClient.h>
#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

// Wi-Fi credentials
const char* ssid = "iot_wireless";
const char* password = "passphrase";

// MQTT broker details
const char* mqtt_server = "hamstersnack.local";
const int mqtt_port = 1883;
const char* mqtt_publish_topic = "house/greeting";
const char* mqtt_hot_topic = "cage/temphot";
const char* mqtt_norm_topic = "cage/tempnorm";
const char* mqtt_cold_topic = "cage/tempcold";
const char* mqtt_light_topic ="cage/nighttime";
const char* mqtt_heater_topic ="cage/heater";
const char* mqtt_fan_topic ="cage/fan";

String name = "Nico! :D";

// WiFi and MQTT clients
WiFiClient espClient;
PubSubClient client(espClient);

// Pins for LEDs and sensors

// **Indicators** //
int hotPin = 32;       // Red LED output
int coldPin = 33;      // Blue LED output
int perfectPin = 26;   // Green LED output

// **Outputs** //
int lightPin = 27;     //White LED output
int heaterPin = 25;    //Heatlamp, RED LED output
int fanPin = 12;       //motor, indicates the FAN is on

// **Sensors** //
int photoPin = 34;     // Analog pin for Photocell Sensor

#define DHTPIN 4
#define DHTTYPE DHT11

int lightValue = 0;
float tempValue = 0;

unsigned long previousMillis = 0;
const long interval = 3000;

DHT_Unified dht(DHTPIN, DHTTYPE);

// MQTT callback function
void callback(char* topic, byte* payload, unsigned int length) {
  String message;
  for (unsigned int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.print("Message received on topic: ");
  Serial.println(topic);
  Serial.print("Message: ");
  Serial.println(message);

  // Check the topic and take action
  if (String(topic) == mqtt_hot_topic) {
    if (message == "on") {
      digitalWrite(hotPin, HIGH); // Turn on Red LED
      digitalWrite(fanPin, HIGH); // Turn on FAN Motor
      Serial.println("Action: Fan and Red LED ON (High Temperature)");
    } else if (message == "off") {
      digitalWrite(hotPin, LOW); // Turn off Red LED
      digitalWrite(fanPin, LOW); // Turn off FAN Motor
      Serial.println("Action: Fan and Red LED OFF");
    }
  } 
  if (String(topic) == mqtt_norm_topic) {
    if (message == "on") {
      digitalWrite(perfectPin, HIGH); // Turn on Green LED
      Serial.println("Action: Green LED ON (Optimal Temperature)");
    } else if (message == "off") {
      digitalWrite(perfectPin, LOW); // Turn off Green LED
      Serial.println("Action: Green LED OFF");
    }
  } 
  if (String(topic) == mqtt_cold_topic) {
    if (message == "on") {
      digitalWrite(coldPin, HIGH); // Turn on Green LED
      Serial.println("Action: Blue LED ON (Cold Temperature)");
    } else if (message == "off") {
      digitalWrite(coldPin, LOW); // Turn off Green LED
      Serial.println("Action: Blue LED OFF");
    }
  }
  if (String(topic) == mqtt_light_topic) {
    if (message == "on") {
      digitalWrite(lightPin, HIGH); // Turn on Green LED
      Serial.println("Action: White LED ON (Light level low)");
    } else if (message == "off") {
      digitalWrite(lightPin, LOW); // Turn off Green LED
      Serial.println("Action: White LED OFF");
    }
  } 
  if (String(topic) == mqtt_fan_topic) {
    if (message == "on") {
      digitalWrite(hotPin, HIGH); // Turn on Red LED
      digitalWrite(fanPin, HIGH); // Turn on FAN Motor
      Serial.println("Action: Fan and Red LED ON (High Temperature)");
    } else if (message == "off") {
      digitalWrite(hotPin, LOW); // Turn off Red LED
      digitalWrite(fanPin, LOW); // Turn off FAN Motor
      Serial.println("Action: Fan and Red LED OFF");
    }
  }
  else if (String(topic) == mqtt_heater_topic) {
    if (message == "on") {
      digitalWrite(heaterPin, HIGH); // Turn on RED LED
      //digitalWrite(indicatorPin, HIGH); // Turn on Yellow LED
      digitalWrite(coldPin, HIGH); // Turn on BLUE LED
      Serial.println("Action: Heater and Blue LED ON (Heater ON)");
    } else if (message == "off") {
      digitalWrite(heaterPin, LOW); // Turn off RED LED
      //digitalWrite(indicatorPin, LOW); // Turn off YELLOW LED
      digitalWrite(coldPin, LOW); // Turn off BLUE LED
      Serial.println("Action: Heater and Blue LED OFF");
    }
  }  

}

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Set MQTT server and callback
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);

  // Initialize DHT
  dht.begin();

  // Configure pins
  pinMode(photoPin, INPUT);
  
  pinMode(hotPin, OUTPUT);
  pinMode(coldPin, OUTPUT);
  pinMode(perfectPin, OUTPUT);
  pinMode(lightPin, OUTPUT);
  
  pinMode(heaterPin, OUTPUT);
  pinMode(fanPin, OUTPUT);


  // Attempt initial MQTT connection
  connect();
}

void loop() {
  // Reconnect to MQTT if disconnected
  if (!client.connected()) {
    connect();
  }

  // Process MQTT messages
  client.loop();

  // Get temperature data
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  tempValue = event.temperature;
  //Serial.println(tempValue);

  // Measure light level
  lightValue = analogRead(photoPin);

  // Publish messages every 3 seconds
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    //String greetingMessage = "Hello all from " + name;
    //client.publish(mqtt_publish_topic, greetingMessage.c_str());

    String lightingMessage = String(lightValue);
    client.publish("room/lighting", lightingMessage.c_str());

    String temperatureMessage = String(tempValue) ;
    client.publish("room/temperature", temperatureMessage.c_str());

    // Subscribe to the topics (ensures subscriptions remain active)
    client.subscribe(mqtt_hot_topic);
    client.subscribe(mqtt_norm_topic);
    client.subscribe(mqtt_cold_topic);
    client.subscribe(mqtt_light_topic);
    client.subscribe(mqtt_heater_topic);
    client.subscribe(mqtt_fan_topic);
  }
}

void connect() {
  // Keep attempting to connect until successful
  while (!client.connected()) {
    Serial.println("Attempting MQTT connection...");
    if (client.connect(name.c_str())) {
      Serial.println("Connected to MQTT broker");

      // Subscribe to topics
      client.subscribe(mqtt_hot_topic);
      client.subscribe(mqtt_norm_topic);
      client.subscribe(mqtt_cold_topic);
      client.subscribe(mqtt_light_topic);
      client.subscribe(mqtt_heater_topic);
      client.subscribe(mqtt_fan_topic);
      
      Serial.print("Subscribed to topics: ");
      Serial.println(mqtt_hot_topic);
      Serial.println(mqtt_norm_topic);
      Serial.println(mqtt_cold_topic);
      Serial.println(mqtt_light_topic);
      Serial.println(mqtt_heater_topic);
      Serial.println(mqtt_fan_topic);
    } else {
      Serial.print("Failed to connect, rc=");
      Serial.print(client.state());
      Serial.println(" Try again in 5 seconds...");
      delay(5000);
    }
  }
}
