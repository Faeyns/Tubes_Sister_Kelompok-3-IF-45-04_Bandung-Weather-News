from paho.mqtt import client as mqtt
from time import sleep

Topic = 'Bandung-Weather-News'
Messages = []
ID = 'Local' 
JumSensor = 3

def on_message(client, user_data, msg):
    # Simpan Message jadi INT
    temprature = int(msg.payload.decode('utf-8'))
    print('Temprature yang didapat :', temprature)
    
    # Jika Messages sudah berisi JumSensor temprature, hapus semua temprature (disesuaikan dengan jumlah sensor)
    if len(Messages) >= JumSensor:
        Messages.clear()

    Messages.append(temprature)
    
    # Rata - rata Temprature
    avg_temprature = sum(Messages)/len(Messages)
    print('Semua Temprature pada',JumSensor,'Sensor :', Messages)  # Menampilkan semua temprature pada Messages
    print('Rata - rata temprature di bandung saat ini :', avg_temprature)
    print("")
    if len(Messages) >= JumSensor:
        # Prediksi cuaca berdasarkan rata-rata suhu
        if avg_temprature < 20.0:
            print('Prediksi cuaca: Dingin')
        elif avg_temprature < 25.0:
            print('Prediksi cuaca: Sejuk')
        elif avg_temprature < 30.0:
            print('Prediksi cuaca: Hangat')
        else:
            print('Prediksi cuaca: Panas')
        print('------------------------')

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        print("Terhubung dengan Topic :",Topic)
        print("")
        print('Report dari semua',JumSensor,'Sensor, ( SubReport',ID,')\nStatus : ON')
        print("Prediksi Cuaca : \n< 20.0 = Dingin\n< 25.0 = Sejuk\n< 30.0 = Hangat\nDiluar rentang temprature tersebut = Panas")
        print('=============================================\n\n------------------------')
    else:
        print("Failed to connect, return code %d\n", rc)
        print("Status : OFF")

# Report_(ID), ditentukan sendiri IDnya
exec(f"Report_{ID} = mqtt.Client('Report_{ID}')")
exec(f"Report_{ID}.on_connect = on_connect")
exec(f"Report_{ID}.on_message = on_message")

exec(f"Report_{ID}.connect('localhost', 1883)")

exec(f"Report_{ID}.loop_start()")

while True:
    exec(f"Report_{ID}.subscribe(Topic)")
    sleep(1)

exec(f"Report_{ID}.disconnect()")
exec(f"Report_{ID}.loop_stop()")
print('Status : OFF')
