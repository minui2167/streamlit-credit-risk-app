import streamlit as st
import pandas as pd

from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml


def main():
    # 제목
    st.set_page_config('대출 위험 분석 및 예측')

    # 메뉴
    menu = ['Home', '분석', '예측']
    st.sidebar.title('대출 위험 분석 및 예측')
    choice = st.sidebar.selectbox('메뉴 선택', menu)

    # 예시 데이터
    df = pd.read_csv('data/credit_risk.csv', index_col = 0)
    st.sidebar.subheader('데이터')
    st.sidebar.dataframe(df)

    # 파일 분리 실행
    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()

if __name__ == '__main__':
    main()