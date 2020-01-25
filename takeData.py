import requests
import time
import csv
import numpy as np 
import json

API_KEY='4Y8K3SBERJ8L8SS4'
CHANNEL1='970657'
temp_url = 'https://api.thingspeak.com/channels/970657/fields/1.json?api_key=4Y8K3SBERJ8L8SS4&results=1'
hum_url = 'https://api.thingspeak.com/channels/970657/fields/2.json?api_key=4Y8K3SBERJ8L8SS4&results=1'
flame_url = 'https://api.thingspeak.com/channels/970657/fields/3.json?api_key=4Y8K3SBERJ8L8SS4&results=1'
temp = []
humid = []
flame= []

fieldnames = ["temperature", "humidity", "flame", "prediction_prob"]

with open('testdata1.csv', 'w') as csv_file:
    csv_write = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_write.writeheader()

while True:
    data_temp = requests.get(temp_url).json()
    data_hum = requests.get(hum_url).json()
    data_flame = requests.get(flame_url).json()
    feilds_temp = data_temp['feeds']
    feilds_hum = data_hum['feeds']
    feilds_flame = data_flame['feeds']
    # json.loads(data_temp, cls= Decoder)
    with open('testdata1.csv','a') as csv_file:
        temp = [x['field1'] for x in feilds_temp]
        temp = np.array(temp, dtype= float)
        hum = [y['field2'] for y in feilds_hum]
        hum = np.array(hum, dtype= float)
        flame = [z['field3'] for z in feilds_flame]
        flame = np.array(flame, dtype= float)
        csv_write = csv.DictWriter(csv_file, fieldnames= fieldnames)
        data = {
            "temperature": temp,
            "humidity": hum,
            "flame": flame
        }
        csv_write.writerow(data)
        # temp = temp.flatten()
    time.sleep(10)




# url = f'https://api.thingspeak.com/channels/970657/feeds.csv?api_key=4Y8K3SBERJ8L8SS4&results=20'
# df = pd.read_csv(url)

# print(df)




