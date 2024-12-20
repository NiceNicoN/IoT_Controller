import json
import time
import paho.mqtt.client as mqtt

class IOT_Controller:
    client = None
    #TODO: support for collections of conditions leading to single outputs
    #JSON: JavaScript Object Notation is the format used for the rules below
    # [] lists of items go between []
    # {} lists of key-value pairs go between {} (dictionaries)
    rules = [
               {
                        "conditions":[
                                {"topic":"house/temp", "comparison":">", "value":30},
                                {"topic":"house/presence", "comparison":"==", "value":"True"}
                        ],
                        "action":{"message":"it's too hot, turn on the AC", "topic":"room/AC", "value":"on"}
               },
               {
                        "conditions":[
                                {"topic":"house/temp", "comparison":"<", "value":20},
                                {"topic":"house/presence", "comparison":"==", "value":"True"} 
                        ],

                        "action":{"message":"it's too cold, turn off the AC", "topic":"room/heat", "value":"on"}
               },
               {
                        "conditions":[
                                {"topic":"house/temp", "comparison":"<", "value":10} 
                        ],

                        "action":{"message":"it's too cold, turn on the heat to keep the pipe from bursting ", "topic":"room/heat", "value":"on"}
               }

         ]
    mqtt_data = {}
    # to remember the messages we sent out
    message_log = {}


    def configure():
        IOT_Controller.client = mqtt.Client()
        #pass the reference to the callback function to handle incoming messages    
        IOT_Controller.client.on_message = IOT_Controller.on_message
        #must connect to the MQTT message broker at "localhost" on port 1883
        IOT_Controller.client.connect("localhost",1883)
        IOT_Controller.client.subscribe("#")

    def on_message(client, userdata, message):
        #this is where we handle the message
	#Using try..except (exception handeling)
        try:
            value = float(message.payload.decode("utf-8"))
        except ValueError:
            print("String")
            value = message.payload.decode("utf-8")
        topic = message.topic

        #discriminate messages that I sent vs messages that I did not send
        #if  IOT_Controller.message_log contains an entry
        for entry in IOT_Controller.message_log:
            if entry["time"] < time.time() - 5:
                #delete all message_log entries
                IOT_Controller.message_log.remove(entry)
            elif entry["topic"] == topic  and entry["value"] == value:
                return

        # record the received data in our dictionary
        IOT_Controller.mqtt_data[topic] = value
#        IOT_Controller.mqtt_data["room/temp"] = 30
#        IOT_Controller.mqtt_data["room/temp"] = 20
#        IOT_Controller.mqtt_data["room/temp"] = 30
#        IOT_Controller.mqtt_data["room/temp"] = 30



        #the only action is the printout
        print(topic, value)
        #based on the value(s) the topic(s) received trigger an action


        #loop through the rules
#               {
#                       "condition":{"topic":"house/temp", "comparison":">", "value":30}
#                      "action":{"message":"it's too hot, turn on the AC", "topic":"room/AC", "value":"on"}
#               },

        for rule in IOT_Controller.rules:
            conditions = rule["conditions"] #change from condition
            conditions_met = True
            for condition in conditions:
                # use the topic from the condition to access the value in the mqtt_data dictionary
                topic = condition["topic"]
                try:
                    value = IOT_Controller.mqtt_data[topic] #not going to work if there is no value for the key provider
                    condition_met = IOT_Controller.condition_met(value,condition["comparison"],condition["value"])
                except KeyError:
                    value = None
                    condition_met = False
                conditions_met = conditions_met and condition_met

            if conditions_met:
                #action
                action = rule["action"]
                print(action["message"])
                IOT_Controller.client.publish(action["topic"],action["value"])
                # record that we sent that message
                entry = {"time":time.time(),"topic":action["topic"],"value":action["value"]}
                IOT_Controller.message_log.append(entry) #end the item to the end of the list

    def condition_met(value,comp_operator,comp_value):
        if comp_operator == ">":
            return value > comp_value
        if comp_operator == ">=":
            return value >= comp_value
        if comp_operator == "<":
            return value < comp_value
        if comp_operator == "<=":
            return value <= comp_value
        if comp_operator == "==":
            return value == comp_value




    def run():
        IOT_Controller.client.loop_forever()

def main():
    IOT_Controller.configure()
    IOT_Controller.run()

if __name__ == "__main__":
   main()

