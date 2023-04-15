# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:43:31 2023

@author: msria
"""

import numpy as np
import pickle #pip install pickle-mixin
import streamlit as st

loaded_model=pickle.load(open("C:/Users/msria/OneDrive/Documents/Deploy models/Diabetes_Prediction_trained_model.sav","rb"))

def diabetes_prediction(inp_data):
   
     #convert list to numpy array
     inp_data_np=np.asarray(inp_data)
     #reshape for one instance input
     reshape_data=inp_data_np.reshape(1,-1)
     prediction=loaded_model.predict(reshape_data)
     if(prediction[0]==1):
          return "The person is Diabetic"
     else:
          return "The person is Non-Diabetic"

def main():
    #title
    st.title("Diabetes Prediction Web APP")
    #getting input from user
    pregnancies=st.text_input("Number of Pregnancies")
    glucose=st.text_input("Glucose Level")
    bloodpressure=st.text_input("Blood Pressure Value")
    skinthickness=st.text_input("Skin Thickness Value")
    insulin=st.text_input("Insulin Value")
    bmi=st.text_input("BMI value")
    diabetespedigreefunction=st.text_input("Diabetes Pedigree Function Value")
    age=st.text_input("Age of the person")
    
    #code for prediction
    diagnosis=""
    #create button for prediction
    if st.button("Diabetes test result"):
        diagnosis=diabetes_prediction([pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()