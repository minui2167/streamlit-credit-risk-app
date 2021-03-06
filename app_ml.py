import streamlit as st
import pandas as pd
import joblib
import numpy as np

def run_ml():
    # DecisionTreeClassifier, ColumnTransformer, LabelEncoder, Scaler를 불러온다
    classifier = joblib.load('data/classifier.pkl')
    ct = joblib.load('data/ct.pkl')
    encoder = joblib.load('data/encoder.pkl')
    scaler = joblib.load('data/scaler.pkl')

    # 버튼 누르기 전
    btn = False

    # 제목
    st.header('파산 여부 예측')

    # 데이터 불러오기
    df = pd.read_csv('data/credit_risk.csv', index_col = 0)

    # ui 2등분
    col1, col2 = st.columns(2)

    with col1:
        # 조건 입력
        age = st.number_input('나이', 20, 120, 27)
        income = st.number_input('연봉', 0, value = 55900)
        ownership = st.selectbox('주거 유형', df['person_home_ownership'].unique())
        length = st.number_input('경력', 0, value = 5)
        intent = st.selectbox('목적', df['loan_intent'].unique())
    with col2:
        # 조건 입력2
        grade = st.selectbox('대출등급', sorted(df['loan_grade'].unique()))
        amount = st.number_input('대출금액', 0, value = 8000)
        rate = st.number_input('이자율', 0.0, value = 11.0)
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
            btn = True    
    
    if btn:
        # 예측 실행
        default = encoder.transform(default)
        test = np.array([age, income, ownership, length, intent, grade, amount, rate, percent, default, len])
        test = test.reshape(1, -1)
        test = ct.transform(test)
        test = scaler.transform(test)
        if classifier.predict(test)[0] == 0:
            st.subheader('파산 저위험군 입니다.')
        else:
            st.subheader('파산 고위험군 입니다.')
    
    



