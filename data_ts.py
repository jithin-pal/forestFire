import requests 
import time

API_KEY='81I75FZRBKZNBC01'
CHANNEL1='964374'
url = 'https://api.thingspeak.com/channels/964374/fields/1.json?results=2'

def take_data(url):
    while True:
        
        data = requests.get(url).json()
        feilds = data['feeds']
        temp = []
        hum = []
        soil_mois = []
    
        for x in feilds:
            temp.append(x['field1'])
            hum.append(x['field2'])
            soil_mois.append(x['field2'])
        print(temp, hum, soil_mois)
        time.sleep(10)
      
    return temp, hum, soil_mois
 
if __name__ == "__main__":
    take_data(url)


#lower relative humidity- readily fire is about to start
# no rain , low humidity, good amount of oxygen
#temperature from fahrenheit -  celcius










"""

{'channel': {'id': 964374, 'name': 'ForestFire', 'latitude': '0.0', 'longitude': '0.0', 'field1': 'Temperature', 'field2': 'Humidity',
'field3': 'Soil Moisture', 'field4': 'Wind Speed', 
'created_at': '2020-01-18T12:15:41Z', 'updated_at': '2020-01-18T12:16:36Z', 'last_entry_id': None}, 'feeds': []}

"""

