import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from streamlit.components.v1 import html

# Hide streamlit menu and footer
# hide_streamlit_style = """
#             <style>
#             MainMenu {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Function to create sparkline using plotly
def create_sparkline(data):
    fig = go.Figure(go.Scatter(
        y=data,
        line=dict(color='#00ff00', width=1.5),
        mode='lines',
        showlegend=False
    ))
    
    # Update layout for minimal appearance
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis={'visible': False},
        yaxis={'visible': False},
        width=100,
        height=30
    )
    
    return fig.to_html(include_plotlyjs='cdn', full_html=False)

# Create sample data
np.random.seed(42)
data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [1000, 1500, 800, 1200],
    'Trend': [
        np.random.randn(10),
        np.random.randn(10),
        np.random.randn(10),
        np.random.randn(10)
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert sparkline data to HTML
df['Sparkline'] = df['Trend'].apply(create_sparkline)

# Create HTML table with sparklines and dark mode styling
html_table = f"""
<style>
    table {{
        width: 100%;
        border-collapse: collapse;
        color: white;
        background-color: #1e1e1e;
    }}
    th, td {{
        padding: 8px;
        text-align: left;
        border: 1px solid #444;
    }}
    th {{
        background-color: #2e2e2e;
    }}
    tr:nth-child(even) {{
        background-color: #262626;
    }}
    tr:hover {{
        background-color: #363636;
    }}
</style>
<table>
    <thead>
        <tr>
            <th>Product</th>
            <th>Sales</th>
            <th>Trend</th>
        </tr>
    </thead>
    <tbody>
"""

for _, row in df.iterrows():
    html_table += f"""
        <tr>
            <td>{row['Product']}</td>
            <td>{row['Sales']}</td>
            <td>{row['Sparkline']}</td>
        </tr>
    """

html_table += """
    </tbody>
</table>
"""

# Display the table with sparklines
st.title("Sales Data with Sparklines")
html(html_table, height=300)

# Display the raw data (optional)
st.subheader("Raw Data")
st.dataframe(df[['Product', 'Sales']])