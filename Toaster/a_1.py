import pandas as pd

# CSV 파일 경로
file_path = 'path/to/your/file.csv'

# CSV 파일을 DataFrame으로 읽기
actionLog = pd.read_csv('./Raw/actionLog.csv')
tokens = pd.read_csv('./Raw/tokens.csv')
userHistory = pd.read_csv('./Raw/userHistory.csv')


# DataFrame 출력 (선택 사항)
actionLog.head()
tokens.head()
userHistory.head()

# Group by 'name' in actionLog
grouped_actionLog = actionLog.groupby(by='name').agg(
    row_cnt=('name', 'size'),  # Count of rows for each name
    user_cnt=('userAddress', 'nunique'),  # Unique user count
).reset_index()

# Add 'perc_total' column
grouped_actionLog['perc_total'] = (grouped_actionLog['row_cnt'] / grouped_actionLog['row_cnt'].sum()) * 100

# Sort by 'perc_total' in descending order
grouped_actionLog = grouped_actionLog.sort_values(by='perc_total', ascending=False)

# Calculate the percentage of users who experienced deposit and withdraw
total_users = actionLog['userAddress'].nunique()
deposit_users = actionLog[actionLog['name'] == 'Deposit']['userAddress'].nunique()
withdraw_users = actionLog[actionLog['name'] == 'Withdraw']['userAddress'].nunique()
swap_users = actionLog[actionLog['name'] == 'Swap']['userAddress'].nunique()

# Calculate the percentage
deposit_percentage = (deposit_users / total_users) * 100
withdraw_percentage = (withdraw_users / total_users) * 100
swap_percentage = (swap_users / total_users) * 100

# Calculate the percentage of users with only one row
single_row_users = actionLog.groupby('userAddress').size().reset_index(name='row_count')
one_row_users_count = single_row_users[single_row_users['row_count'] == 1].shape[0]
one_row_percentage = (one_row_users_count / total_users) * 100

# Calculate the percentage of users with only one approved row
approved_single_row_users = actionLog[(actionLog['name'] == 'Approve')].groupby('userAddress').size().reset_index(name='row_count')
one_approved_row_users_count = approved_single_row_users[approved_single_row_users['row_count'] == 1].shape[0]
one_approved_row_percentage = (one_approved_row_users_count / total_users) * 100

# Print the results
print(f"Percentage of users who experienced deposit: {deposit_percentage:.2f}%")
print(f"Percentage of users who experienced withdraw: {withdraw_percentage:.2f}%")
print(f"Percentage of users who experienced swap: {swap_percentage:.2f}%")
print(f"Percentage of users with only one row: {one_row_percentage:.2f}%")
print(f"Percentage of users with only one approved row: {one_approved_row_percentage:.2f}%")
