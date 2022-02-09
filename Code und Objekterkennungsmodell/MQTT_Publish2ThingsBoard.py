#mqtt libraris
import paho.mqtt.client as paho                     
import os
import json
import time
from datetime import datetime

ACCESS_TOKEN='6EPakPtbI8ZmehC0Rz1X'                 #Token von ThingsBoard Gerät angeben
broker="demo.thingsboard.io"                        #ThingsBoard als Host angeben
port=1883                                           

def on_publish(client,userdata,result):             
    print("Data published to thingsboard \n")
    pass
client1= paho.Client("control1")                    
client1.on_publish = on_publish                     
client1.username_pw_set(ACCESS_TOKEN)               
client1.connect(broker,port,keepalive=60)           

counter = 0
noContent = '\n'
anzahlDurchlauf = 5
datei = open('/var/www/html/ContentListFridge.txt','r') #Textdatei mit Inhalten einlesen


for zeile in datei:
       
    counter+=1  

    payload="{\"Inhalt"+str(counter)+"\":\""+zeile+"\"}" # json Format generieren

    ret= client1.publish("v1/devices/me/telemetry",payload) #Upload der Daten
      
       
    print(payload);
    time.sleep(0.5)
       
       
if counter < anzahlDurchlauf:                    #Wenn weniger Inhalte als zuvor vorhanden sind, leere Inhalte hochladen
   counter+=1
   for zahl in range(counter,6):
       #print(zahl)
       payload="{\"Inhalt"+str(zahl)+"\":\""+noContent+"\"}"
       ret= client1.publish("v1/devices/me/telemetry",payload) 
       print(payload);
       time.sleep(0.5)