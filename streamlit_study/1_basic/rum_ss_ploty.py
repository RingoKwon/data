import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.title('Animated Charts with Plotly Express')

# 샘플 데이터 생성
np.random.seed(42)
dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
df = pd.DataFrame({
    'date': dates,
    'value': np.random.randn(len(dates)).cumsum(),
    'category': np.random.choice(['A', 'B', 'C'], len(dates)),
    'size': np.random.randint(10, 100, len(dates))
})

# 차트 선택
chart_type = st.selectbox(
    "차트 유형을 선택하세요",
    ["Line Animation", "Scatter Animation", "Bar Animation"]
)

if chart_type == "Line Animation":
    # 주별 데이터로 변환
    df['week'] = df['date'].dt.isocalendar().week
    
    fig = px.line(df, x='date', y='value', color='category',
                  animation_frame='week',
                  title='시계열 데이터 애니메이션',
                  range_y=[df['value'].min(), df['value'].max()],
                  range_x=[df['date'].min(), df['date'].max()])
    
    # 애니메이션 설정 조정
    fig.update_layout(
        updatemenus=[{
            'buttons': [{
                'args': [None, {'frame': {'duration': 500, 'redraw': True},
                               'fromcurrent': True,
                               'transition': {'duration': 300}}],
                'label': '▶',
                'method': 'animate'
            }],
            'type': 'buttons'
        }]
    )
    
    st.plotly_chart(fig)

elif chart_type == "Scatter Animation":
    # 월별 데이터로 변환
    df['month'] = df['date'].dt.month
    
    fig = px.scatter(df, x='value', y='size', color='category',
                     animation_frame='month',
                     size='size',
                     title='산점도 애니메이션',
                     range_x=[df['value'].min(), df['value'].max()],
                     range_y=[0, 100])
    
    fig.update_layout(
        updatemenus=[{
            'buttons': [{
                'args': [None, {'frame': {'duration': 1000, 'redraw': True},
                               'fromcurrent': True}],
                'label': '▶',
                'method': 'animate'
            }],
            'type': 'buttons'
        }]
    )
    
    st.plotly_chart(fig)

else:  # Bar Animation
    # 월별 평균 계산
    monthly_data = df.groupby(['category', df['date'].dt.month])[['value']].mean().reset_index()
    monthly_data.columns = ['category', 'month', 'value']
    
    fig = px.bar(monthly_data, x='category', y='value',
                 animation_frame='month',
                 color='category',
                 title='막대 차트 애니메이션',
                 range_y=[monthly_data['value'].min(), monthly_data['value'].max()])
    
    fig.update_layout(
        updatemenus=[{
            'buttons': [{
                'args': [None, {'frame': {'duration': 1000, 'redraw': True},
                               'fromcurrent': True}],
                'label': '▶',
                'method': 'animate'
            }],
            'type': 'buttons'
        }]
    )
    
    st.plotly_chart(fig)

# 데이터 컨트롤
st.sidebar.header('데이터 설정')
show_data = st.sidebar.checkbox('원본 데이터 보기')
if show_data:
    st.write(df)

# 추가: 학교 출석 애니메이션 차트
st.title('학교 출석 애니메이션 차트')

dates = ["2022-12-03", "2022-12-04", "2022-12-05", "2022-12-06", "2022-12-07", "2022-12-08", "2022-12-09"]
school_a = [86.77, 80.74, 79.48, 76.47, 75.44, 74.49, 70.41]
school_b = [92.77, 91.64, 90.68, 92.37, 92.84, 90.29, 92.71]

df_attendance = pd.DataFrame(list(zip(dates, school_a, school_b)),
                             columns=['date', 'school_a', 'school_b'])

fig_attendance = go.Figure(
    layout=go.Layout(
        updatemenus=[dict(type="buttons", direction="right", x=0.9, y=1.16)],
        xaxis=dict(range=["2022-12-02", "2022-12-10"],
                   autorange=False, tickwidth=2,
                   title_text="Time"),
        yaxis=dict(range=[0, 100],
                   autorange=False,
                   title_text="Price")
    ))

# Add traces
i = 1

fig_attendance.add_trace(
    go.Scatter(x=df_attendance.date[:i],
               y=df_attendance.school_a[:i],
               name="School A",
               visible=True,
               line=dict(color="#f47738", dash="dash")))

fig_attendance.add_trace(
    go.Scatter(x=df_attendance.date[:i],
               y=df_attendance.school_b[:i],
               name="School B",
               visible=True,
               line=dict(color="#1d70b8", dash="dash")))

# Animation
fig_attendance.update(frames=[
    go.Frame(
        data=[
            go.Scatter(x=df_attendance.date[:k], y=df_attendance.school_a[:k]),
            go.Scatter(x=df_attendance.date[:k], y=df_attendance.school_b[:k])]
    )
    for k in range(i, len(df_attendance) + 1)])

# Buttons
fig_attendance.update_layout(title="Attendance % of two schools over time.",
                             xaxis_title="Date",
                             yaxis_title="Attendance %",
                             legend_title="Legend Title",
                             showlegend=False,
                             font=dict(
                                 family="Arial",
                                 size=14
                             ),
                             paper_bgcolor='rgba(0,0,0,0)',
                             plot_bgcolor='rgba(0,0,0,0)',
                             hovermode="x",
                             updatemenus=[
                                 dict(
                                     buttons=list([
                                         dict(label="Play",
                                              method="animate",
                                              args=[None, {"frame": {"duration": 500}}]),
                                         dict(label="School A",
                                              method="update",
                                              args=[{"visible": [False, True]},
                                                    {"showlegend": True}]),
                                         dict(label="School B",
                                              method="update",
                                              args=[{"visible": [True, False]},
                                                    {"showlegend": True}]),
                                         dict(label="All",
                                              method="update",
                                              args=[{"visible": [True, True, True]},
                                                    {"showlegend": True}]),
                                     ]))
                             ]
                             )

# Streamlit에서 차트 표시
st.plotly_chart(fig_attendance)