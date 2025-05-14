import streamlit as st
import pandas as pd
import plotly.express as px

# Đọc dữ liệu
@st.cache_data
def load_data():
    df = pd.read_excel("education_career_success.xlsx")
    return df

df = load_data()

st.title("🔁 Career Path vs Soft Skills/Networking")
st.markdown("Biểu đồ **Sunburst** theo thứ tự: **Cấp bậc công việc → Ngành học → Giới tính**, với màu sắc theo yếu tố **Soft Skills / Networking**.")

# Tạo biểu đồ sunburst
fig = px.sunburst(
    df,
    path=["Current_Job_Level", "Field_of_Study", "Gender"],
    values=None,  # Tự động đếm
    color="Soft_Skills_or_Networking",
    color_discrete_sequence=px.colors.qualitative.Pastel,  # hoặc Vivid, Safe, Set3, v.v.
    title="Sunburst Chart - Job Level → Field → Gender (Color = Soft Skills / Networking)"
)

fig.update_traces(maxdepth=3)

# Hiển thị biểu đồ
st.plotly_chart(fig, use_container_width=True)

# Hiển thị bảng dữ liệu gốc
with st.expander("📊 Xem dữ liệu gốc"):
    st.dataframe(df)
