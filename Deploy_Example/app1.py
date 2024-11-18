# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 00:16:08 2024

@author: Snehal
"""

import streamlit as st

st.title('Welcome to my Webpage! :wave:')
st.markdown('It is a basic webapp which gives prediction')

st.number_input('Enter Your Age:',min_value=18, max_value=95)
st.selectbox('Select Gender', ['male','female'])