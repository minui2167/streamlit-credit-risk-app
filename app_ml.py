import streamlit as st
import pandas as pd
import joblib
import numpy as np

def run_ml():
    classifier = joblib.load('data/classifier.pkl')
    ct = joblib.load('data/ct.pkl')
    encoder = joblib.load('data/encoder.pkl')
    scaler = joblib.load('data/scaler.pkl')


    st.subheader('파산 여부 예측')
    df = pd.read_csv('data/credit_risk.csv', index_col = 0)
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('나이', 20, 120, 27)
        income = st.number_input('연봉', 0, value = 55900)
        ownership = st.selectbox('주거 유형', df['person_home_ownership'].unique())
        length = st.number_input('경력', 0, value = 5)
        intent = st.selectbox('목적', df['loan_intent'].unique())
    with col2:
        grade = st.selectbox('등급', sorted(df['loan_grade'].unique()))
        amount = st.number_input('대출금액', 0, value = 8000)
        rate = st.number_input('이자율', 0, value = 11)
        percent = income / amount
        len = st.number_input('신용 기록',0 , value = 4)
        default = st.checkbox('과거 파산 여부')
        if default:
            default = 'Y'
        else:
            default = 'N'
        default = np.array([default])
        default = default.reshape(1, -1)
        if st.button('예측'):
            default = encoder.transform(default)
            test = np.array([age, income, ownership, length, intent, grade, amount, rate, percent, default, len])
            test = test.reshape(1, -1)
            test = ct.transform(test)
            test = scaler.transform(test)    
            if classifier.predict(test)[0] == 0:
                st.text('파산 저위험군 입니다.')
            else:
                st.text('파산 고위험군 입니다.')




