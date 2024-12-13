import paho.mqtt.client as mqtt 
import sqlite3
from datetime import datetime

# record everything coming  over MQTT


# Connect to MQTT Server
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "#" #multi-level wildcard
#client setting
MQTT_CLIENT_ID = "historian-client"#name of this program to disclose to the broker
DB_FILE = "historian_data.db"

#MQTT client callback for connection - runs once at the momment the client connects to the broker 
def on_connect(client, userdata, flags, rc):
    print("connected to MQTT")
    #good time to subcribe
    client.subscribe(MQTT_TOPIC)

#MQTT client callback to handle incomming message
def on_message(client, userdata, msg):
    print("got a message")
    #get the value from the message 
    payload = msg.payload.decode()
    #get the topic form the message
    topic = msg.topic
    #get the current time to log the time when the message came in...format it as a date I can read
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #save this to the database
    #wait... print for debugging
    #print(topic, payload, timestamp)
    save_to_database(topic, payload, timestamp)

def save_to_database(topic, payload, timestamp):
    print("saved a message")
    #connect to the database - open the database file
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor() #finger to send commands to the database

    #make sure that there is a place where we can save the massage
    #SQL (Structured Query Language) is a lanquege to talk to databases
    SQL = "CREATE TABLE IF NOT EXISTS historian_data (topic TEXT, message TEXT, timestamp TEXT);"
    cursor.execute(SQL)

    #save the message
    SQL = "INSERT INTO historian_data (topic, message, timestamp) VALUES (?,?,?)"
    cursor.execute(SQL,(topic, payload, timestamp))

    #confirm the writeing and close
    conn.commit()
    conn.close()


##...

#create the MQTT client object
client = mqtt.Client(client_id=MQTT_CLIENT_ID)
#set callbacks
# on_connect as the actual callback to use upon connecting
client.on_connect = on_connect
# on_meassage callback when ever I recive a message
client.on_message = on_message
#connect to the server
#setting the  definded om_connect as the actual callback to use upon  connceting
client.on_connect = on_connect

client.connect(MQTT_BROKER, MQTT_PORT, 60)
#start receiving message
client.loop_start()

try:
    while True:#infinite loop
        #logic goes here
        pass
except KeyboardInterrupt:
    #disconnect from MQTT Broker
    client.disconnect()

#subscribe to all topics
#when messages come in, store them to a database
