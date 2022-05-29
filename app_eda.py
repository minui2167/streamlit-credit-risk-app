import streamlit as st
import pandas as pd
import plotly.express as px

def run_eda():
    df = pd.read_csv('data/credit_risk.csv', index_col = 0)
 
    st.subheader('분포 그래프')
    selected = st.selectbox('컬럼 선택', df.columns)
    fig = px.histogram(df, x = selected) 
    st.plotly_chart(fig)