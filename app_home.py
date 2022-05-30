import streamlit as st
import pandas as pd

def run_home():
    st.title('대출 에서 위험요소와 파산 예측')

    url = 'https://cdn.pixabay.com/photo/2019/02/22/12/04/investing-4013413__340.jpg'   
    st.image(url)

    st.text('(달러 기준) 나이, 연봉, 주거 유형, 경력, 목적, 등급, 대출금액, 이자율,\n연봉 대비 대출금액, 과거 파산 여부, 신용 기록에 따라 파산 예측을 해보자')

    df = pd.read_csv('data/credit_risk.csv', index_col = 0)
    st.subheader('데이터 미리보기')
    st.dataframe(df)

    st.subheader('수치형 데이터 요약')
    st.dataframe(df.describe())