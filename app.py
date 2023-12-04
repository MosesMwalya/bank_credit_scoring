# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 16:44:38 2023

@author: MMMutua
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# load scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))
# load the saved model
model = pickle.load(open('model.pkl', 'rb'))


st.title('Customer Credit Score')


##
job = st.checkbox('Customer has job')
marital = st.checkbox('Customer is Married')
housing = st.checkbox('Has house')
loan = st.checkbox('Has loan')
poutcome = st.checkbox('Poutcome')

age = st.slider('Customer age in years', 19,73,1)
education = st.select_slider('Select Education Level, primary=0, secondary=1, tertiary=2',[0,1,2])
default = st.select_slider('Select default', [0,1])
balance = st.slider('Enter customer balance', -2047.0, 3596.5, 1.0)
contact = st.select_slider('Select contact, cellular=0,telephone=1, unknown=2', [0,1,2])
day = st.slider('date of month', 1, 31, 1)
month = st.slider('month', 0, 11, 1)
duration = st.slider('Enter duration', 4.0, 667.0, 1.0)
campaign = st.select_slider('Select campaign', [0,1,2,3,4,5,6])

pdays = st.slider('Enter pdays', -1, 900, 1)
previous = st.slider('Enter previous', 0, 25, 1)

    
    
    
   
#Define input features for prediction
inputs = [[age,job,marital,education,default,balance,housing,loan, 
           contact,day,month,duration,campaign,pdays,previous,poutcome]]
    

    
#Supply inputs to perform prediction
if st.button('Predict Credit Score'): 
    inputs_scaled = scaler.transform(inputs) #using Loaded scaler
    score = pd.DataFrame(model.predict_proba(inputs_scaled))
    new_score = round(1000*score.iloc[0,0],0)
    
    
    st.success(new_score)


