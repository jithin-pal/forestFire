import requests
import time
import csv
import numpy as np 
import json

# API_KEY_1='7T303XJMPKKTXCK8'
# API_KEY_2 = '81I75FZRBKZNBC01'

# CHANNEL1='964374'
# CHANNEL2= '970657'

temp1_url = 'https://api.thingspeak.com/channels/964374/fields/1.json?results=1'
hum1_url =  'https://api.thingspeak.com/channels/964374/fields/2.json?results=1'
flame1_url = 'https://api.thingspeak.com/channels/964374/fields/3.json?results=1'

temp2_url = 'https://api.thingspeak.com/channels/970657/fields/1.json?api_key=4Y8K3SBERJ8L8SS4&results=1'
hum2_url = 'https://api.thingspeak.com/channels/970657/fields/2.json?api_key=4Y8K3SBERJ8L8SS4&results=1'
flame2_url = 'https://api.thingspeak.com/channels/970657/fields/3.json?api_key=4Y8K3SBERJ8L8SS4&results=1'


fieldnames = ["temperature1", "humidity1", "flame1", "temperature2", "humidity2", "flames2","prediction_prob"]

with open('MergeData.csv', 'w') as csv_file:
    csv_write = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_write.writeheader()

while True:
    data_temp1 = requests.get(temp1_url).json()
    data_hum1 = requests.get(hum1_url).json()
    data_flame1 = requests.get(flame1_url).json()
    feilds_temp1 = data_temp1['feeds']
    feilds_hum1 = data_hum1['feeds']
    feilds_flame1 = data_flame1['feeds']
    data_temp2 = requests.get(temp2_url).json()
    data_hum2 = requests.get(hum2_url).json()
    data_flame2 = requests.get(flame2_url).json()
    feilds_temp2 = data_temp2['feeds']
    feilds_hum2 = data_hum2['feeds']
    feilds_flame2 = data_flame2['feeds']
    # json.loads(data_temp, cls= Decoder)

    with open('MergeData.csv','a') as csv_file:
        temp1 = [x['field1'] for x in feilds_temp1]
        temp1 = np.array(temp1, dtype= float)
        hum1 = [y['field2'] for y in feilds_hum1]
        hum1 = np.array(hum1, dtype= float)
        flame1 = [z['field3'] for z in feilds_flame1]
        flame1 = np.array(flame1, dtype= float)
        temp2 = [x['field1'] for x in feilds_temp2]
        temp2 = np.array(temp2, dtype= float)
        hum2 = [y['field2'] for y in feilds_hum2]
        hum2 = np.array(hum2, dtype= float)
        flame2 = [z['field3'] for z in feilds_flame2]
        flame2 = np.array(flame2, dtype= float)
        csv_write = csv.DictWriter(csv_file, fieldnames= fieldnames)
        data = {
            "temperature1": float(temp1),
            "humidity1": float(hum1),
            "flame1": float(flame1),
            "temperature2": float(temp2),
            "humidity2": float(hum2),
            "flames2": float(flame2),
            
        }
        csv_write.writerow(data)
        print(temp1, hum1, flame1, temp2, hum2, flame2)
    time.sleep(10)


