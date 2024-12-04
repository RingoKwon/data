import streamlit as st
import pandas as pd
import numpy as np
import os 

data = pd.read_csv('tips.csv')

def sample_function(df):
    return df.sample(5)


# button 
st.header('button')
st.subheader('sample data')
st.caption('click the button to see the sample data')
 
click = st.button('sample data')

if click:
    st.write(sample_function(data))



