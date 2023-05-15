from multiprocessing.reduction import DupFd
import numpy as np
import pandas as pd

engine='openpyxl'
df = pd.read_excel('데이터 분석신청 자료.xlsx', engine='openpyxl')
row = []
print(df)
# 쓰기 함수
wr = pd.ExcelWriter('merge_data.xlsx', engine='xlsxwriter') #작성자 객체 생성
# df에 있는 내용을 엑셀 파일을 생성하고 그곳에 저장하라
df.to_excel(wr, index=False) #sheet_name='Sheet3'
# index는 지정하지 않음
wr.save()