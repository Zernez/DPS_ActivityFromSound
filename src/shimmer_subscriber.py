import paho.mqtt.client as mqtt
from predict_model import predict 
from train_model import training 
import pandas as pd
import pickle
from timeit import Timer

# Select True if you want to train a model
training_selector= False
folder_data= "./data/"
data_type= "shimmer"
max_pre_alarm= 6

prediction_obj= predict()
train_obj= training()
data_out= pd.DataFrame()

# The callback for when the client receives a CONNACK response from the server.
    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("shimmer")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    if (training_selector== True):
        train_obj.store_data_train(msg.payload, data_type)
    else:
        # if ((prediction_obj.timing> max_pre_alarm or not prediction_obj.timing.is_alive()) and prediction_obj.immutable== False):
        prediction_obj.store_data_prediction(msg, data_type)

#    print(f"topic = {msg.topic}, payload = {msg.payload}")

client = mqtt.Client()
    # Client callback that is called when the client successfully connects to the broker.
client.on_connect = on_connect
    # Client callback that is called when a message within the subscribed topics is published.
client.on_message = on_message

client.connect("84.238.56.157", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a manual interface.
client.loop_forever()