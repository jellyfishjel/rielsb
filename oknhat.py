import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Sunburst Chart by Field with RdBu Color Coding")

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

        # Define fixed numerical codes for salary levels
        salary_map = {'<30K': 0, '30K–50K': 1, '50K–70K': 2, '70K+': 3}
        df['Salary_Code'] = df['Salary_Group'].map(salary_map)

        # Group data
        sunburst_data = df.groupby(['Entrepreneurship', 'Field_of_Study', 'Salary_Group', 'Salary_Code']).size().reset_index(name='Count')

        # Labels
        sunburst_data['Entrepreneurship_Label'] = sunburst_data['Entrepreneurship']
        sunburst_data['Field_Label'] = sunburst_data['Field_of_Study']
        sunburst_data['Salary_Label'] = sunburst_data['Salary_Group']

        # Color by salary code to maintain consistent colors across all fields
        sunburst_data['ColorValue'] = sunburst_data['Salary_Code']

        # Plot
        fig = px.sunburst(
            sunburst_data,
            path=['Entrepreneurship_Label', 'Field_Label', 'Salary_Label'],
            values='Count',
            color='ColorValue',  # Color by numerical salary group
            color_continuous_scale=px.colors.diverging.RdBu[::-1],
            title='Entrepreneurship → Field → Salary (Color by Salary Group using RdBu scale)'
        )

        fig.update_traces(maxdepth=2, branchvalues="remainder")
        st.plotly_chart(fig)
