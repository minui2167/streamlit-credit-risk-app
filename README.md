# streamlit-credit-rist-app
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

[http://ec2-3-35-26-163.ap-northeast-2.compute.amazonaws.com:8503/](http://ec2-3-35-26-163.ap-northeast-2.compute.amazonaws.com:8503/)

대출시 위험 요소 분석과 대출시 파산 위험 예측 앱입니다.

데이터출처 [https://www.kaggle.com/datasets/laotse/credit-risk-dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)

![사진](https://cdn.pixabay.com/photo/2019/02/22/12/04/investing-4013413__340.jpg)

# 데이터셋
* person_age 나이
* person_income 연간 수입
* person_home_ownership 주거 유형
* person_emp_length 경력
* loan_intent 대출 의도
* loan grade 대출 등급
* loan amnt 대출 금액
* loan_int_rate 이자율
* loan_percent_income 대출금대비 소득
* cb_person_default_on_file 과거 파산 여부
* cb_person_cred_hist_length 신용 기록
* loan_status 파산 여부

# 분석

* plotly를 통해서 각 요소들 분포 시각화
* 선택한 컬럼 히스토그램 불러오기
* 파산 여부와의 상관관계 출력
* groupby를 통해서 파산한 그룹과 아닌 그룹 비교 

# 파산 예측

* 각 요소들을 입력하면 DecisionTreeClassifier로 파산 고위험군과 저위험군 분류

![다운로드 (3)](https://user-images.githubusercontent.com/105832345/173175988-1442976c-4fd5-4780-af8a-45d736e812c0.png)

