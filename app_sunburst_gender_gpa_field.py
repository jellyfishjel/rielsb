
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sunburst Chart", layout="centered")
st.title("📊 Sunburst Chart: Gender → GPA Band → Field of Study")

# Đọc dữ liệu
df = pd.read_excel("education_career_success.xlsx")

# Nhóm GPA theo mốc tròn
gpa_bins = [0, 2.0, 2.5, 3.0, 3.5, 4.0]
gpa_labels = ["≤2.0", "2.0–2.5", "2.5–3.0", "3.0–3.5", "3.5–4.0"]
df["GPA_Band"] = pd.cut(df["University_GPA"], bins=gpa_bins, labels=gpa_labels)

# Tạo biểu đồ Sunburst
fig = px.sunburst(
    df,
    path=["Gender", "GPA_Band", "Field_of_Study"],
    values=None,  # tự động đếm số lượng
    title="Sunburst Chart: Gender → GPA Band → Field of Study"
)
fig.update_traces(textinfo="label+percent parent")

st.plotly_chart(fig, use_container_width=True)
