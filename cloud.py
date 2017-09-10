import paho.mqtt.client as mqtt
import json
import urllib.request

def greatCircleDistance( coords_1, coords_2 ):
 url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}, {1}&destinations={2}, {3}&key= AIzaSyAhpEf5XIFeMDdPYvembz7WWWh5ryRTO-0".format(coords_1[0], coords_1[1], coords_2[0], coords_2[1])
 webURL = urllib.request.urlopen(url)
 print(webURL.read())
 result = json.loads(webURL.read())
 driving_time = result['rows'][0]['elements'][0]['duration']['value']
 print("driving time: {0}".format(driving_time))

 return result

# The callback for when the client successfully connects to the broker
def on_connect(client, userdata, flags, rc):
    ''' We subscribe on_connect() so that if we lose the connection
        and reconnect, subscriptions will be renewed. '''

    client.subscribe("owntracks/+/+")

# The callback for when a PUBLISH message is received from the broker
def on_message(client, userdata, msg):

    topic = msg.topic

    try:
        data = json.loads(str(msg.payload, 'ascii'))
        print(data)
        print("TID = {0} is currently at {1}, {2}".format(data['tid'], data['lat'], data['lon']))
        coords_1 = (data['lat'], data['lon'])
        coords_2 = (-22.5827088, -47.400379699999995)
        print("Distance Logic {0}: {1}".format(coords_2, greatCircleDistance(coords_1, coords_2)))
    except Exception as e:
        print("Error: {0}".format(e))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="ha", password="133906949")
client.connect("m11.cloudmqtt.com", 12821, 60)

# Blocking call which processes all network traffic and dispatches
# callbacks (see on_*() above). It also handles reconnecting.

client.loop_forever()
