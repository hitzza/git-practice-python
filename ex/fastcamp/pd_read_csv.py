import pandas as pd

df = pd.read_csv('C:/jhex/jh_ex.py/ex/fastcamp/과일가게.csv',index_col=0)
#index_col=0, 데이터의 index를 불러올 때 중복으로 불러와져 unnamed(인덱스 번호를 표시하는 컬럼)이 생기지 않게 해줌

sep_check_df = pd.read_csv('C:/jhex/jh_ex.py/ex/fastcamp/read_sep.txt',index_col=0, sep='|')
#구분자가 콤마가 아닌 경우 sep ='구분자' 추가

#헤더가 여러줄인 경우
header_df = pd.read_csv('C:/jhex/jh_ex.py/ex/fastcamp/read_multi_header.csv', header=1)

#데이터를 읽으면서 컬럼명을 추가하고 싶을 때
make_column_df = pd.read_csv('C:/jhex/jh_ex.py/ex/fastcamp/make_column_name.csv',
                index_col= 0, names = ['품목', '크기', '금액', '수수료'])

#원하는 컬럼만 쓰고 싶을 때
use_df = pd.read_csv('C:/jhex/jh_ex.py/ex/fastcamp/과일가게.csv',usecols=['품목', '크기'])
#csv파일 만들기
#make_column_df.to_csv('C:/jhex/jh_ex.py/ex/fastcamp/make_csv_to_csv.csv')