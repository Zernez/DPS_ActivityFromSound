from predict_model import predict
from train_model import training
from predict_model import predict
import pandas as pd
import pickle
import numpy as np
import threading


print('1')
folder_data= "./data/"

train_wav= False

inp = input("Choose Train Option: 1-Train 2-Predict 3-Visualize Data\n")

if(inp == "1"):
    train_wav = True

if (inp== "3"):
    training_data= pickle.load(open(folder_data + "definitive_audio.pickle", 'rb'))
    pd.set_option('display.max_rows', None)
    print (training_data)
    quit()   

# "train_wav= False" when you want to train the model with phidget data so use "sound222_FFT_only_training.py" for produce data
if train_wav== True:
    tr = training()
    # for i in range(0, 6):
    #     tr.create_model(i)
    tr.create_model()
# train_wav= True when you want to predict
else:
   pr = predict()
   pr.load_model()
   # pr.real_time_pred()

   def do_predictions():
       threading.Timer(1.0, do_predictions).start() # do it every 10 seconds
       label = pr.real_time_pred()
       print('now you are doing', label)
#        pre_shimmer= pickle.load(open(folder_data + "shimmer_prediction.pickle", 'rb'))
#       pickle.dump(label,open(folder_data + "prediction_result.pickle", 'wb'))
    #    newlabel = label
    #    print(pre_shimmer)       

   do_predictions()


