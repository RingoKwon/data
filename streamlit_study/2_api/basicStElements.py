from tarfile import data_filter
import streamlit as st 
import pandas as pd 
import numpy as np 
import time 





st.title("title")
st.caption("explain caption ")
st.header("header")
st.subheader("subheader")

df = pd.DataFrame({
    'first_col' : [1,2,3], 
    'second_col' : [1,2,3]
})
st.markdown("""
# df 
- see this 
---
""")
st.write(df)

body = '''
import streamlit as st 
import pandas as pd 
import numpy as np 


st.title("title")
st.caption("explain caption ")
st.header("header")
st.subheader("subheader")

df = pd.DataFrame({
    'first_col' : [1,2,3], 
    'second_col' : [1,2,3]
})
st.markdown("""
# df 
- see this 
---
""")
st.write(df)
'''

st.subheader('codeblock')
st.code(body, language='python')

formula = """
a+ar +a r^3 +\cdots + a r^{n-1} = \sum_{k=1}^{n-1} a r^k
"""

st.subheader('LaTex')
st.latex(formula)

st.header('data')
st.subheader('DataFrame')

df1 = pd.read_csv('tips.csv')
st.dataframe(data = df1 , width = 1000, height=150)

st.subheader("static tatble")
st.table(data=df1.head(5))

st.subheader('JSON')
json_var = df1.head(5).to_dict()
st.json(json_var, expanded=False)


st.header("Status Element")
st.subheader('Progress Bar')

# Create two containers
progress_container = st.container()
content_container = st.container()
st.write('test2')








# Display content in the lower container first
with content_container:
    st.write('test')
    st.write('다른 내용들도 여기에 추가할 수 있습니다')

# Run the progress bar in the upper container
def progress_bar() :
    for i in range(101): 
        my_bar.progress(i)
        time.sleep(0.05)
with progress_container:
    with st.spinner('Processing'):
        my_bar = st.progress(0)
        progress_bar()


