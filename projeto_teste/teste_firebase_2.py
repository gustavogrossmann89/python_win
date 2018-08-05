import time
import requests
import json
fixed_interval = 10
firebase_url = "https://iotsmartlockgg.firebaseio.com/"

while 1:
    try:
        # current time and date
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%d/%m/%Y')
        node = '00124B000F28C303'
        topic = 'lock'
        msg = '1'

        # insert record
        data = {'date': date_mmddyyyy, 'time': time_hhmmss, 'node': node,'topic': topic,'msg': msg}
        result = requests.post(firebase_url + '/logs.json', data=json.dumps(data))

        print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
        time.sleep(fixed_interval)
    except IOError:
        print('Error! Something went wrong.')
    time.sleep(fixed_interval)