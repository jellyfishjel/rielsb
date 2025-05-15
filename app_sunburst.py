
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

# Thêm cột đếm để làm giá trị cho biểu đồ phần trăm
df["Count"] = 1

# Tạo biểu đồ sunburst theo phần trăm (tỷ lệ phân phối)
fig = px.sunburst(
    df,
    path=["Gender", "Current_Job_Level", "Field_of_Study"],
    values="Count",  # Dựa trên số lượng
    title="Sunburst Chart - Phân phối theo Giới tính, Cấp bậc Công việc và Ngành học"
)

fig.update_traces(maxdepth=2)

# Hiển thị biểu đồ
st.plotly_chart(fig, use_container_width=True)
