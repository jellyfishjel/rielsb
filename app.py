
import streamlit as st
import pandas as pd
import plotly.express as px

# Đọc dữ liệu
@st.cache_data
def load_data():
    df = pd.read_excel("education_career_success.xlsx")
    return df

df = load_data()

st.title("🎓📈 Career Outcomes Sunburst Explorer")
st.markdown("Phân tích mối liên hệ giữa **ngành học**, **cấp bậc công việc**, **khởi nghiệp** và **mức lương khởi điểm** hoặc **mức độ hài lòng nghề nghiệp**.")

# Lựa chọn giá trị đo
value_option = st.selectbox(
    "Chọn chỉ số để hiển thị:",
    ["Starting_Salary", "Career_Satisfaction"]
)

# Tạo biểu đồ sunburst
fig = px.sunburst(
    df,
    path=["Entrepreneurship", "Current_Job_Level", "Field_of_Study"],
    values=None,  # Không cộng, ta dùng avg ở màu
    color=value_option,
    color_continuous_scale="RdBu",
    color_continuous_midpoint=df[value_option].mean(),
    title=f"Sunburst Chart - {value_option} theo ngành, cấp độ công việc và khởi nghiệp"
)

fig.update_traces(maxdepth=2)

# Hiển thị biểu đồ
st.plotly_chart(fig, use_container_width=True)

# Hiển thị bảng dữ liệu (tuỳ chọn)
with st.expander("📊 Xem dữ liệu gốc"):
    st.dataframe(df)
