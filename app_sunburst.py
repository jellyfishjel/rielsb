import streamlit as st
import pandas as pd
import plotly.express as px

# Đọc dữ liệu
@st.cache_data
def load_data():
    df = pd.read_excel("education_career_success.xlsx")
    return df

df = load_data()

# Thêm cột đếm để biểu diễn số lượng
df["Count"] = 1

# Giao diện
st.title("🎓📊 Gender & Career Path Sunburst")
st.markdown("Phân tích **tỷ lệ phân phối** theo **giới tính**, **cấp bậc công việc** và **ngành học**.")

fig = px.sunburst(
    df,
    path=["Gender", "Current_Job_Level", "Field_of_Study"],
    values="Count",
    color="Gender",  # Dựa theo Gender để tô màu
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title="Sunburst Chart - Phân phối theo Giới tính, Cấp bậc Công việc và Ngành học"
)

fig.update_traces(maxdepth=2)

# Hiển thị biểu đồ
st.plotly_chart(fig, use_container_width=True)

# Tuỳ chọn hiển thị bảng dữ liệu
with st.expander("📊 Xem dữ liệu gốc"):
    st.dataframe(df)
