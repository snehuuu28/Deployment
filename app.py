# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 00:49:30 2024

@author: Snehal
"""

import pickle
import streamlit as st

st.title('Claim Prediction :bar_chart:')

load = open('model.pkl','rb')
model = pickle.load(load)


def predict(age,gender,bmi,smoker):
    prediction = model.predict([[age,gender,bmi,smoker]])
    return prediction

def main():
    
    st.markdown('This is a very simple webapp for prediction of claim amount :chart:')
    age = st.number_input('Age', min_value= 0 , max_value=100)
    gender = st.selectbox('Gender', ('male','female'))
    bmi = st.number_input('BMI')
    smoker = st.selectbox('Smoker',('Yes','No'))
    if st.button('Predict'):
        result = predict(age,gender,bmi,smoker)
        st.success('The claim is : ${} '.format(result))                          
                          
        
if __name__ == '__main__':
    main()