# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

#loading the saved model
loaded_model=pickle.load(open("C:/Users/msria/OneDrive/Documents/Deploy models/Diabetes_Prediction_trained_model.sav","rb"))
inp_data=(7,196,90,0,0,39.8,0.451,41)#o/p==1
#convert list to numpy array
inp_data_np=np.asarray(inp_data)
#reshape for one instance input
reshape_data=inp_data_np.reshape(1,-1)
prediction=loaded_model.predict(reshape_data)
if(prediction[0]==1):
  print("The person is Diabetic")
else:
  print("The person is Non-Diabetic")
