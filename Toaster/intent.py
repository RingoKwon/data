import pandas as pd

intentLog = pd.read_csv('./Raw/intentLog.csv')

# Filter for rows where 'doen' is True
intentLog = intentLog[intentLog['done'] == True]

grouped_actionLog = intentLog.groupby(by='name').agg(
    row_cnt=('name', 'size'),  # Count of rows for each name
    user_cnt=('userAddress', 'nunique'),  # Unique user count
).reset_index()

# Calculate the proportion of userAddress and row_cnt for each name
grouped_actionLog['userAddress_ratio'] = grouped_actionLog['user_cnt'] / grouped_actionLog['user_cnt'].sum()
grouped_actionLog['row_cnt_ratio'] = grouped_actionLog['row_cnt'] / grouped_actionLog['row_cnt'].sum()


