
import streamlit as st
import pandas as pd
import plotly.express as px

# Đọc dữ liệu
@st.cache_data
def load_data():
    df = pd.read_excel("education_career_success.xlsx")
    return df

df = load_data()

st.title("🎓📈 Gender & Career Path Sunburst")
st.markdown("Phân tích mối liên hệ giữa **giới tính**, **cấp bậc công việc**, **ngành học** và **mức lương khởi điểm**.")

# Tạo biểu đồ sunburst
fig = px.sunburst(
    df,
    path=["Gender", "Field_of_Study"],
    values=None,  # Không cộng dồn — màu thể hiện giá trị trung bình
    color="Starting_Salary",
    color_continuous_scale="Magma",
    color_continuous_midpoint=df["Starting_Salary"].mean(),
    title="Sunburst Chart - Starting Salary theo Giới tính, Cấp bậc Công việc và Ngành học"
)

fig.update_traces(maxdepth=2)

# Hiển thị biểu đồ
st.plotly_chart(fig, use_container_width=True)

# Hiển thị bảng dữ liệu (tuỳ chọn)
with st.expander("📊 Xem dữ liệu gốc"):
    st.dataframe(df)
