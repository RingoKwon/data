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

# checkbox
st.markdown('---')
st.header('checkbox')
st.subheader('single checkbox')
checkbox = st.checkbox('show/hide')
st.write("checkbox", checkbox)

st.subheader('multiple checkbox')


with st.container():
    st.info('multiple checkbox')
    checkbox1 = st.checkbox('checkbox1')
    checkbox2 = st.checkbox('checkbox2')
    checkbox3 = st.checkbox('checkbox3')
    checkbox4 = st.checkbox('checkbox4')

    button = st.button('submit')

    if button:
        dict = {'checkbox1': checkbox1,
                'checkbox2': checkbox2, 
                'checkbox3': checkbox3, 
                'checkbox4': checkbox4  }
        st.json(dict)

# radio 
st.markdown('---')
st.header('radio')

st.subheader('single radio')
radio = st.radio('select', ['option1', 'option2', 'option3'])
st.markdown(f'Selected: `{radio}`')


