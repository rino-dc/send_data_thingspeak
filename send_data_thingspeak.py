import requests
import json
import time
import random

api_key = '467HQZ2548W1G8LS'
hosts = 'api.thingspeak.com'
URL = 'http://api.thingspeak.com/update.json'
HEADER = {"Host" : hosts, "Content-Type" : "application/json"}

data_1 = "0"
data_2 = "0"
sleep_time = 20 #akan sleep (delay) selama 20 detik

def generate_dummy_data():
	global data_1
	global data_2

	print("GENERATE DUMMY DATA")
	data_1 = str(random.randint(56,97))
	print("DATA 1 : "+ data_1)
	data_2 = str(random.randint(12,40))
	print("DATA 2 : "+ data_2)

def send_data():
	global data_1
	global data_2
	
	print("SEND DATA")
	
	payload = "{\"api_key\" : \"" + api_key + "\",\"field1\": " + data_1 + ", \"field2\" : " + data_2 + "}"
	print(payload)
	response = requests.post(url = URL , data = payload, headers = HEADER)
	print(response.text)
	print #ini untuk newline aja

while True:
	generate_dummy_data()
	send_data()
	print
	print
	time.sleep(sleep_time) #fungsi delay/sleep
