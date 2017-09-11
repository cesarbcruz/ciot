import paho.mqtt.client as mqtt
import urllib.request, json


def geo( coords_1, coords_2 ):
 url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0},{1}&destinations={2},{3}&key=%20AIzaSyAhpEf5XIFeMDdPYvembz7WWWh5ryRTO-0".format(coords_1[0], coords_1[1], coords_2[0], coords_2[1])
 with urllib.request.urlopen(url) as url:
    result = json.loads(url.read().decode())

 origin_addresses = result['origin_addresses'][0]
 destination_addresses = result['destination_addresses'][0]
 driving_time = result['rows'][0]['elements'][0]['duration']['text']
 distance_time = result['rows'][0]['elements'][0]['distance']['text']
 print("Endereço origem: {0}".format(origin_addresses))
 print("Endereço destino: {0}".format(destination_addresses))
 print("Distância: {0}".format(distance_time))
 print("Tempo de Carro: {0}".format(driving_time))
 print("\n")

 return result

def on_connect(client, userdata, flags, rc):
    client.subscribe("owntracks/+/+")

def on_message(client, userdata, msg):

    topic = msg.topic

    try:
        data = json.loads(str(msg.payload, 'ascii'))
        coords_1 = (data['lat'], data['lon'])
        coords_2 = (-22.375454, -47.393242)
        geo(coords_1, coords_2)
    except Exception as e:
        print("Error: {0}".format(e))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="ha", password="133906949")
client.connect("m11.cloudmqtt.com", 12821, 60)

client.loop_forever()
