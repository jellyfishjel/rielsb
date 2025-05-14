import streamlit as st
import pandas as pd
import plotly.express as px

# Đọc dữ liệu
@st.cache_data
def load_data():
    df = pd.read_excel("education_career_success.xlsx")
    return df

df = load_data()

st.title("🎓📈 Gender-based Sunburst Comparison")
st.markdown("So sánh mối liên hệ giữa **Cấp bậc công việc**, **Ngành học** và **Mức lương khởi điểm** theo từng giới tính.")

# Lấy danh sách giới tính duy nhất
genders = df["Gender"].dropna().unique()

# Tạo biểu đồ cho từng giới tính
for gender in genders:
    st.subheader(f"🔍 {gender}")
    filtered_df = df[df["Gender"] == gender]

    fig = px.sunburst(
        filtered_df,
        path=["Current_Job_Level", "Field_of_Study"],
        values=None,
        color="Starting_Salary",
        color_continuous_scale="RdBu",
        color_continuous_midpoint=filtered_df["Starting_Salary"].mean(),
        title=f"Sunburst - {gender}: Starting Salary theo Job Level và Field of Study"
    )
    
    fig.update_traces(maxdepth=2)
    st.plotly_chart(fig, use_container_width=True)

# Bảng dữ liệu gốc (tuỳ chọn)
with st.expander("📊 Xem dữ liệu gốc"):
    st.dataframe(df)
