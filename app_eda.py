from email.policy import default
import streamlit as st
import pandas as pd
import plotly.express as px

def run_eda():
    df = pd.read_csv('data/credit_risk.csv', index_col = 0)
 
    st.subheader('분포 그래프')
    selected = st.selectbox('컬럼 선택', df.columns)
    fig = px.histogram(df, x = selected) 
    st.plotly_chart(fig)

    st.subheader('파산 여부와 상관관계')
    fig = px.bar(df.corr()['loan_status'].sort_values(ascending = False)[1:])
    st.plotly_chart(fig)
    st.text('연봉 대비 대출금액, 이자율, 과거 파산 여부가 상관관계가 상대적으로 높다.\n파산 여부에 따른 세 조건들의 평균값을 살펴보자.')

    st.subheader('파산 여부에 따른 연봉 대비 대출금액')
    fig = px.histogram(df, x = 'loan_status', y = 'loan_percent_income' , color = 'loan_status', histfunc = 'avg')
    st.plotly_chart(fig)

    st.subheader('파산 여부에 따른 이자율')
    fig = px.histogram(df, x = 'loan_status', y = 'loan_int_rate' , color = 'loan_status', histfunc = 'avg')
    st.plotly_chart(fig)

    st.subheader('파산 여부에 따른 과거 파산 여부')
    fig = px.histogram(df, x = 'loan_status', y = 'cb_person_default_on_file' , color = 'loan_status', histfunc = 'avg')
    st.plotly_chart(fig)
    st.text('세 조건다 확연히 파산한 쪽이 더 높다.')

