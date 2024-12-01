import streamlit as st 
import pandas as pd 
import time 


st.title('Layouts')

side_bar = st.sidebar

side_bar.header('sidebar')
side_bar.write('this it sidebar')

st.write('This is page')

# load df 
df = pd.read_csv('tips.csv')

