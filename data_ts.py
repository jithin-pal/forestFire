#lower relative humidity- readily fire is about to start
# no rain , low humidity, good amount of oxygen
#temperature from fahrenheit -  celcius

"""

{'channel': {'id': 964374, 'name': 'ForestFire', 'latitude': '0.0', 'longitude': '0.0', 'field1': 'Temperature', 'field2': 'Humidity',
'field3': 'Soil Moisture', 'field4': 'Wind Speed', 
'created_at': '2020-01-18T12:15:41Z', 'updated_at': '2020-01-18T12:16:36Z', 'last_entry_id': None}, 'feeds': []}

"""

import requests 
import time

API_KEY='81I75FZRBKZNBC01'
CHANNEL1='964374'
temp_url = 'https://api.thingspeak.com/channels/964374/fields/1.json?results=1'
hum_url = 'https://api.thingspeak.com/channels/964374/fields/2.json?results=1'

def take_data(temp_url, hum_url):
    while True:
        data_temp = requests.get(temp_url).json()
        data_hum = requests.get(hum_url).json()
        feilds_temp = data_temp['feeds']
        feilds_hum = data_hum['feeds']
        temp = []
        hum = []
        for x in feilds_temp:
            temp.append(x['field1'])
        for y in feilds_hum:
            hum.append(y['field2'])
        print(temp,hum)
        time.sleep(15)
    return temp, hum
 
if __name__ == "__main__":
    take_data(temp_url, hum_url)


