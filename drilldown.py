import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Sunburst Chart: Entrepreneurship → Field → Salary")

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

        # Group data
        sunburst_data = df.groupby(['Entrepreneurship', 'Field_of_Study', 'Salary_Group']).size().reset_index(name='Count')

        # Tổng số lượng để tính phần trăm
        total_count = sunburst_data['Count'].sum()
        sunburst_data['Percentage'] = (sunburst_data['Count'] / total_count * 100).round(2)

        # Gán màu cho Yes/No bằng giá trị số
        color_map = {'Yes': 1, 'No': -1}
        sunburst_data['ColorValue'] = sunburst_data['Entrepreneurship'].map(color_map)

        # Plot
        fig = px.sunburst(
            sunburst_data,
            path=['Entrepreneurship', 'Field_of_Study', 'Salary_Group'],
            values='Count',
            color='ColorValue',
            color_continuous_scale=px.colors.diverging.RdBu[::-1],
            title='Entrepreneurship → Field → Salary (Color by Yes/No)',
            custom_data=['Count', 'Percentage']
        )

        # Hiển thị số phần trăm trong hover
        fig.update_traces(
            hovertemplate='<b>%{label}</b><br>Count: %{customdata[0]}<br>Percentage: %{customdata[1]}%'
        )

        fig.update_traces(maxdepth=2, branchvalues="remainder")
        st.plotly_chart(fig)
