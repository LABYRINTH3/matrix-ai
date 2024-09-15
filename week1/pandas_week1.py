import pandas as pd
import numpy as np
titanic_df = pd.read_csv("/Users/th/Desktop/pandas/train.csv")
# 전체 정보를 알려줌
titanic_df.info()

# 데이터의 첫 10개의 행을 출력합니다
print(titanic_df.head(10))

# Age의 열 처음 5개를 출력합니다 
print(titanic_df['Age'].head())

# Survived 값이 1인 행의 첫 4줄만 출력합니다
print(titanic_df[titanic_df['Survived'] == 1].head(4))



print('\n')

df1 = pd.DataFrame({
    '학번': ['A0001','A0002','A0003','A0004','A0005'],
    '학점': np.random.rand(5)*2.25 + 2.25
}, columns=['학번','학점'])

df2 = pd.DataFrame({
    '학번': ['A0001','A0002','A0003','A0004','A0005'],
    '수강과목' : ['데이터 통신', '이산수학', '자료구조 프로그래밍', '어셈블리 언어', '선형대수학']
}, columns=['학번','수강과목'])

# 학점 데이터 프레임과 수강과목을 병합했습니다.
print("학점 데이터 프레임과 수강과목을 병합했습니다.\n")
merge1_df=pd.merge(df1,df2)
print(merge1_df)


df3 = pd.DataFrame({
    '학번': ['A0001','A0002','A0003','A0004','A0005'],
    '학과' : ['컴퓨터 공학과', '산업 데이터 공학과', '법학과', '컴퓨터 공학과', '산업 데이터 공학과']
}, columns=['학번','학과'])
# 학점 데이터 + 수강과목 프레임과 학과를 병합했습니다.
print("\n학점 데이터 + 수강과목 프레임과 학과를 병합했습니다.\n")
merge2_df=pd.merge(merge1_df,df3)
print(merge2_df)

df4 = pd.DataFrame({
    '학번': ['A0001','A0002','A0003','A0004','A0005'],
    '나이' : np.random.randint(20,24,size=5)
}, columns=['학번','나이'])
# 학점 데이터 + 수강과목 + 학과 프레임과 나이를 병합했습니다.
print("\n학점 데이터 + 수강과목 + 학과 프레임과 나이를 병합했습니다.\n")
merge3_df=pd.merge(merge2_df,df4)
print(merge3_df)