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
st.dataframe(df)

columns = tuple(df.columns)
st.write(columns)

#  create widget select box 
select_column = side_bar.selectbox(
    'Select the column you wnat to display', 
    columns
)

side_bar.write('You selected the column_name = `{}'.format(select_column) + '`')
