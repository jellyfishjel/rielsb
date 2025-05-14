import plotly.express as px
import pandas as pd

# Giả sử bạn có một DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50, 60],
    'Group': ['X', 'X', 'X', 'Y', 'Y', 'Y']
})

# Tính phần trăm cho mỗi nhóm
df['Percentage'] = df['Value'] / df.groupby('Group')['Value'].transform('sum') * 100

# Tạo biểu đồ với Plotly Express
fig = px.bar(df, 
             x='Category', 
             y='Value', 
             color='Group', 
             text='Percentage', # Hiển thị phần trăm trên các ô
             title='Bar Chart with Percentage',
             labels={'Value': 'Total Value', 'Category': 'Category'})

# Tùy chỉnh để hiển thị phần trăm rõ ràng hơn
fig.update_traces(texttemplate='%{text:.1f}%', textposition='inside', hoverinfo='y+text')

# Hiển thị biểu đồ
fig.show()
