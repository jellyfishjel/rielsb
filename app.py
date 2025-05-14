
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Interactive Pie Chart", layout="centered")

st.title("📊 Biểu đồ tròn tương tác từ dữ liệu giáo dục và nghề nghiệp")

# Đọc dữ liệu từ file Excel
df = pd.read_excel("education_career_success.xlsx")

# Các cột dạng phân loại có thể chọn
categorical_cols = ["Field_of_Study", "Gender", "Current_Job_Level", "Entrepreneurship"]

# Cho người dùng chọn cột
selected_col = st.selectbox("Chọn cột để vẽ biểu đồ tròn:", categorical_cols)

# Đếm tần suất từng giá trị
counts = df[selected_col].value_counts().reset_index()
counts.columns = [selected_col, "Count"]

# Vẽ biểu đồ với Plotly
fig = px.pie(counts, names=selected_col, values="Count", title=f"Phân bố theo '{selected_col}'")
fig.update_traces(textinfo='percent+label')

st.plotly_chart(fig, use_container_width=True)
