import streamlit as st 
import numpy as np 
import time

# st.write("ddfjl:{}".format(st.__version__))
# st.write(f"djflkjdf{st.__version__}")




st.sidebar.write('dd')
progress_bar = st.sidebar.progress(0)
statue_text = st.sidebar.empty() 

last_row =  np.random.randn(1,1)
chart = st.line_chart(last_row)

for i in range(1,101): 
    new_raw = last_row[-1,:] +np.random.randn(5,1)
    statue_text.text("%i%% Completed"%i)
    progress_bar.progress(i)
    time.sleep(0.1)
    chart.add_rows(new_raw)

progress_bar.empty()

st.button('Re-run')



