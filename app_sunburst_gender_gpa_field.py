import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sunburst Drilldown", layout="centered")

# Tải dữ liệu
@st.cache_data
def load_data():
    df = pd.read_excel("education_career_success.xlsx")
    bins = [0, 1000, 1300, df["SAT_Score"].max()]
    labels = ["Low", "Medium", "High"]
    df["SAT_Score_Group"] = pd.cut(df["SAT_Score"], bins=bins, labels=labels, include_lowest=True)
    return df

df = load_data()

# Tiêu đề ứng dụng
st.title("🎓 Sunburst Drilldown: Gender → Field → SAT Group")

# Hiển thị biểu đồ
fig = px.sunburst(
    df,
    path=["Gender", "Field_of_Study", "SAT_Score_Group"],
    maxdepth=2,  # chỉ hiện 2 vòng đầu
)

fig.update_layout(margin=dict(t=10, l=10, r=10, b=10))
st.plotly_chart(fig, use_container_width=True)
