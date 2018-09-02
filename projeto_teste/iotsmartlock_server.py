import paho.mqtt.client as mqtt
import time
import requests
import json

#URL do Banco de Dados Firebase
firebase_url = "https://iotsmartlockgg.firebaseio.com/"

#URL do Broker MQTT
broker_address = "iotsmartlock.mooo.com"
#broker_address = "pksr.eletrica.eng.br"

##############################################################
# Funcao que le as mensagens, monta JSON e insere no Firebase
##############################################################
def on_message(client, userdata, message):
    try:
        #Set dos dados que serao inseridos no JSON de comunicacao com o Firebase
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%d/%m/%Y')
        node = message.topic.split('/')[0]
        topic = message.topic.split('/')[1]
        msg = str(message.payload.decode("utf-8"))

        #Mensagem original capturada
        print("message received", str(message.payload.decode("utf-8")), \
              "topico", message.topic, "retained ", message.retain)
        print message.topic.split('/')[0]
        print message.topic.split('/')[1]

        #Se for uma mensagem dos topicos 'leave' ou 'alert', sera inserida um novo objeto na base de notificacoes do Firebase
        if topic == "leave" or topic == "alert":
            notificationData = {'date': date_mmddyyyy, 'time': time_hhmmss, 'node': node, 'type': topic, 'read': '0'}
            notificationResult = requests.post(firebase_url + '/notifications.json', data=json.dumps(notificationData))
            print 'Notification inserted. Result Code = ' + str(notificationResult.status_code) + ',' + notificationResult.text

        #Insere novo objeto log na base de logs do Firebase
        logData = {'date': date_mmddyyyy, 'time': time_hhmmss, 'node': node, 'topic': topic, 'msg': msg}
        logResult = requests.post(firebase_url + '/logs.json', data=json.dumps(logData))
        print 'Log inserted. Result Code = ' + str(logResult.status_code) + ',' + logResult.text
    except IOError:
        print('Error! Something went wrong.')
########################################

########################################
################ MAIN ##################
########################################

#Criacao de nova instancia
print("criando nova instancia")
client = mqtt.Client("IoTSmartLockPython_Server")
client.on_message=on_message

#Conectando-se ao broker MQTT
print("conectando ao broker")
client.connect(broker_address) #connect to broker

#Subscribe em todos os topicos do broker
client.loop_start() #start the loop
#print("Subscribing to topic","00124B000F28C303/+")
print("Subscribing to topic","+/+")
client.subscribe("+/+")

#Loop de leitura das mensagens enviadas ao broker
while True:
    time.sleep(4) # wait
client.loop_stop() #stop the loop

########################################