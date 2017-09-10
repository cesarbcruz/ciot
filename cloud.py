import paho.mqtt.client as mqtt
import json

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
    except Exception as e:
        print("Cannot decode data on topic {0}\n{1}".format(topic, e))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="ha", password="133906949")
client.connect("m11.cloudmqtt.com", 12821, 60)

# Blocking call which processes all network traffic and dispatches
# callbacks (see on_*() above). It also handles reconnecting.

client.loop_forever()
