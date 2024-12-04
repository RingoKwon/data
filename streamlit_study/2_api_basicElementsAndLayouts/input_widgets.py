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

# selectbox
st.markdown('---')
st.header('selectbox')
st.subheader('single selectbox')

selectbox = st.selectbox('select', ['option1', 'option2', 'option3'])
st.write(f'Selected: `{selectbox}`')

st.subheader('multiple selectbox')

with st.container():
    st.info('multiple selectbox')
    multiselect = st.multiselect('selectbox1',
                               ['option1',
                                'option2', 
                                'option3'])
    st.write(f'Selected: ',multiselect)

# slider
st.markdown('---')
st.header('slider') 

slider = st.slider('select', 0, 10000, 1000, 100)
st.write(f'Selected: `{slider}`')

# text input 
st.markdown('---')
st.header('text input')

text = st.text_input('input text')
st.write(f'Input text: `{text}`')

# number input 
st.markdown('---')
st.header('number input')

number = st.number_input('input number', 0, 10000, 1000, 100)
st.write(f'Input number: `{number}`')

# text area 
st.markdown('---')
st.header('text area')

text_area = st.text_area('input text area')
st.write(f'Input text area: `{text_area}`')

# date input 
st.markdown('---')
st.header('date input')

date = st.date_input('select date')
st.write(f'Selected date: `{date}`')

#  file uploader 
st.markdown('---')
st.header('file uploader')


uploaded_file = st.file_uploader('upload file')
save_button = st.button('save')

if save_button:
    if uploaded_file is not None:
        with open(os.path.join("./saved_file", uploaded_file.filename), mode='wb') as f:
            f.write(uploaded_file.getvalue())