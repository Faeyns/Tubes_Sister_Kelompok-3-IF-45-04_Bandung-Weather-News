# Import Library
import random
from time import sleep
from paho.mqtt import client as mqtt

# Listening Temprature
def getTemprature():
    return random.randint(12,32)
    
# Topic dan ID
Topic = 'Bandung-Weather-News'
ID = '001'

# Publish Data
def on_publish(client, userdata, mid):
    print('Message ID :',mid)
    print('Temprature :',Temprature)  # Menampilkan Temprature
    print('------------------------')

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        print("Terhubung dengan Topic :",Topic)
        print("")
        print('Sensor dengan ID', ID, '\nStatus : ON')
        print('=============================================\n\n------------------------')
    else:
        print("Failed to connect, return code %d\n", rc)
        print("Status : OFF")

# Sensor_(ID), ditentukan sendiri IDnya
exec(f"Sensor_{ID} = mqtt.Client('Sensor_{ID}')")
exec(f"Sensor_{ID}.on_connect = on_connect")
exec(f"Sensor_{ID}.on_publish = on_publish")
exec(f"Sensor_{ID}.connect('localhost', 1883)")

exec(f"Sensor_{ID}.loop_start()")
while True:
    Temprature = getTemprature()
    if Temprature > 1:
        exec(f"Sensor_{ID}.publish(Topic, Temprature)")
    sleep(10)

exec(f"Sensor_{ID}.disconnect()")
exec(f"Sensor_{ID}.loop_stop()")
print('Status : OFF')