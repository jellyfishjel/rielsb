
import streamlit as st
import pandas as pd
import plotly.express as px

# Đọc dữ liệu
@st.cache_data
def load_data():
    df = pd.read_excel("education_career_success.xlsx")
    
    # Tạo nhóm tuổi phù hợp với dữ liệu 18–29
    bins = [17, 21, 25, 29]
    labels = ['18–21', '22–25', '26–29']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)
    
    return df

df = load_data()

st.title("🎓👥 Salary Analysis theo Age Group, Job Level, Field of Study")
st.markdown("Khám phá mức lương khởi điểm theo **nhóm tuổi**, **cấp bậc công việc** và **ngành học**.")

# Chọn thang màu
color_scale = st.selectbox(
    "🎨 Chọn bảng màu:",
    ["Viridis", "Cividis", "Plasma", "Inferno", "Magma", "Turbo", "IceFire", "Bluered", "YlGnBu"],
    index=0
)

# Biểu đồ sunburst
fig = px.sunburst(
    df,
    path=["Age_Group", "Current_Job_Level", "Field_of_Study"],
    values=None,
    color="Starting_Salary",
    color_continuous_scale=color_scale,
    color_continuous_midpoint=df["Starting_Salary"].mean(),
    title="Sunburst Chart - Starting Salary theo Nhóm Tuổi → Cấp bậc Công việc → Ngành học"
)

fig.update_traces(maxdepth=3)

# Hiển thị biểu đồ
st.plotly_chart(fig, use_container_width=True)

# Xem dữ liệu
with st.expander("📊 Xem dữ liệu gốc"):
    st.dataframe(df)
