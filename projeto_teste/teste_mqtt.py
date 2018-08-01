import paho.mqtt.client as mqtt
import time

############
def on_message(client, userdata, message):
    print("message received", str(message.payload.decode("utf-8")), \
          "topico", message.topic, "retained ", message.retain)
########################################

broker_address="iotsmartlock.mooo.com"
print("creating new instance")
client = mqtt.Client("Python_Server")
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop
#print("Subscribing to topic","00124B000F28C303/+")
print("Subscribing to topic","+/+")
client.subscribe("+/+")
while True:
    time.sleep(4) # wait
client.loop_stop() #stop the loop