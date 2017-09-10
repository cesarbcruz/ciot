import RPi.GPIO as GPIO 
import time 
import paho.mqtt.client as mqtt 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(13,GPIO.IN) 
mqttc=mqtt.Client() 
mqttc.username_pw_set(username="ha", password="133906949")
mqttc.connect("m11.cloudmqtt.com",12821,60) 
mqttc.loop_start() 
def reading1():
    a=GPIO.input(13)
    print(a)
    return a 
while 1:
    t=reading1()
    (result,mid)=mqttc.publish("temp",t,2)
    time.sleep(1) 
mqttc.loop_stop()
mqttc.disconnect()

