import streamlit as st 
import pandas as pd 
import numpy as np 


df = pd.DataFrame({
    'first_col' : [1,2,3], 
    'second_col' : [1,2,3]
})
st.write(df)


