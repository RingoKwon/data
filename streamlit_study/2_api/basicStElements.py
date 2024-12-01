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
st.dataframe(df1)



