import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Sunburst Chart by Field with RdBu Color Scale")

# Upload file
uploaded_file = st.file_uploader("Upload the Excel file", type="xlsx")

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file, sheet_name='education_career_success')
    except Exception as e:
        st.error(f"Error loading Excel sheet: {e}")
    else:
        # Categorize salary ranges
        def categorize_salary(salary):
            if salary < 30000:
                return '<30K'
            elif salary < 50000:
                return '30K–50K'
            elif salary < 70000:
                return '50K–70K'
            else:
                return '70K+'

        df['Salary_Group'] = df['Starting_Salary'].apply(categorize_salary)

        # Group and count
        sunburst_data = df.groupby(['Entrepreneurship', 'Field_of_Study', 'Salary_Group']).size().reset_index(name='Count')

        # Label hierarchy
        sunburst_data['Entrepreneurship_Label'] = sunburst_data['Entrepreneurship']
        sunburst_data['Field_Label'] = sunburst_data['Field_of_Study']
        sunburst_data['Salary_Label'] = sunburst_data['Salary_Group']

        # Dùng Field_of_Study để tô màu (dù là không nằm trong path)
        sunburst_data['Color_Group'] = sunburst_data['Field_of_Study']

        # Lấy danh sách ngành duy nhất
        unique_fields = sunburst_data['Field_of_Study'].unique()

        # Tạo bảng màu riêng từ RdBu (discrete)
        from plotly.colors import diverging
        rd_bu_palette = diverging.RdBu[::-1]  # Đảo ngược nếu thích xanh dương đầu
        color_map = {field: rd_bu_palette[i % len(rd_bu_palette)] for i, field in enumerate(unique_fields)}

        # Gán màu tương ứng
        sunburst_data['Color'] = sunburst_data['Color_Group'].map(color_map)

        # Vẽ biểu đồ
        fig = px.sunburst(
            sunburst_data,
            path=['Entrepreneurship_Label', 'Field_Label', 'Salary_Label'],
            values='Count',
            color='Color_Group',
            color_discrete_map=color_map,
            title='Sunburst Chart by Field (Colored by Field using RdBu scale)'
        )

        st.plotly_chart(fig)
