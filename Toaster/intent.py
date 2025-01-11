import pandas as pd

intentLog = pd.read_csv('./Raw/intentLog.csv')

# Filter for rows where 'doen' is True
# intentLog = intentLog[intentLog['done'] == True]

# CTE와 유사한 방식으로 userAddress별로 행 수를 계산
aa = intentLog.groupby('userAddress').size().reset_index(name='row_cnt')

# intentLog와 aa를 조인
result = pd.merge(intentLog, aa, on='userAddress')

# 필요한 열을 선택하고 그룹화
final_result = result.groupby(['row_cnt', 'name']).agg(lambda x: x.tolist()).reset_index()

# 유저별 비율 계산
final_result['user_ratio'] = final_result['row_cnt'] / final_result['row_cnt'].sum()

# 결과 출력
print(final_result)


