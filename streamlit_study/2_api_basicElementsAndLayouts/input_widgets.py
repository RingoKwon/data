import streamlit as st
import pandas as pd
import numpy as np
import os 

data = pd.read_csv('tips.csv')
st.write(data.head())

# button 
click = st.button('click me')
st.write('clicked', click)



