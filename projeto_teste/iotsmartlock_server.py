import paho.mqtt.client as mqtt
import time
import requests
import json
firebase_url = "https://iotsmartlockgg.firebaseio.com/"
#broker_address = "iotsmartlock.mooo.com"
broker_address = "pksr.eletrica.eng.br"

########################################
def on_message(client, userdata, message):
    try:
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%d/%m/%Y')
        node = message.topic.split('/')[0]
        topic = message.topic.split('/')[1]
        msg = str(message.payload.decode("utf-8"))

        print("message received", str(message.payload.decode("utf-8")), \
              "topico", message.topic, "retained ", message.retain)
        print message.topic.split('/')[0]
        print message.topic.split('/')[1]

        data = {'date': date_mmddyyyy, 'time': time_hhmmss, 'node': node, 'topic': topic, 'msg': msg}
        result = requests.post(firebase_url + '/logs.json', data=json.dumps(data))
        print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
    except IOError:
        print('Error! Something went wrong.')
########################################

print("creating new instance")
client = mqtt.Client("IoTSmartLockPython_Server")
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