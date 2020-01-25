#lower relative humidity- readily fire is about to start
# no rain , low humidity, good amount of oxygen
#temperature from fahrenheit -  celcius

import requests 
import time
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import pandas as pd
import csv
import numpy as np


API_KEY='4Y8K3SBERJ8L8SS4'
CHANNEL1='970657'
temp_url = 'https://api.thingspeak.com/channels/970657/fields/1.json?api_key=4Y8K3SBERJ8L8SS4&results=1'
hum_url = 'https://api.thingspeak.com/channels/970657/fields/2.json?api_key=4Y8K3SBERJ8L8SS4&results=1'
flame_url = 'https://api.thingspeak.com/channels/970657/fields/3.json?api_key=4Y8K3SBERJ8L8SS4&results=1'


while True:
    data_temp = requests.get(temp_url).json()
    data_hum = requests.get(hum_url).json()
    data_flame = requests.get(flame_url).json()
    
    feilds_temp = data_temp['feeds']
    feilds_hum = data_hum['feeds']
    feilds_flame = data_flame['feeds']
    temp = [x['field1'] for x in feilds_temp]
    temp = np.array(temp,dtype=float)
    print(type(temp))
    # hum = [y['field2'] for y in feilds_hum]
    # flame = [z['field3'] for z in feilds_flame]
    print(temp)
    time.sleep(5)



