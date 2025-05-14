
st.title("🚀 Sunburst Chart: Tác động của Khởi nghiệp đến Nghề nghiệp")

st.markdown("""
Phân tích mối quan hệ giữa:
- **Tình trạng khởi nghiệp**
- **Cấp độ công việc hiện tại**
- **Ngành học**
và các chỉ số như **Mức lương khởi điểm** hoặc **Mức độ hài lòng nghề nghiệp**.
""")

value_option = st.selectbox(
    "Chọn chỉ số để phân tích:",
    ["Starting_Salary", "Career_Satisfaction"]
)

fig = px.sunburst(
    df,
    path=["Entrepreneurship", "Current_Job_Level", "Field_of_Study"],
    values=None,
    color=value_option,
    color_continuous_scale="RdBu",
    color_continuous_midpoint=df[value_option].mean(),
    title=f"Sunburst Chart - {value_option} theo Khởi nghiệp, Cấp độ công việc và Ngành học"
)

fig.update_traces(maxdepth=2)

st.plotly_chart(fig, use_container_width=True)
