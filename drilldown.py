import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.colors import diverging

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

        # Group data
        sunburst_data = df.groupby(['Entrepreneurship', 'Field_of_Study', 'Salary_Group']).size().reset_index(name='Count')

        # Labels
        sunburst_data['Entrepreneurship_Label'] = sunburst_data['Entrepreneurship']
        sunburst_data['Field_Label'] = sunburst_data['Field_of_Study']
        sunburst_data['Salary_Label'] = sunburst_data['Salary_Group']
        sunburst_data['Color_Group'] = sunburst_data['Field_of_Study']

        # Color mapping
        unique_fields = sunburst_data['Field_of_Study'].unique()
        rd_bu_palette = diverging.RdBu[::-1]
        color_map = {field: rd_bu_palette[i % len(rd_bu_palette)] for i, field in enumerate(unique_fields)}

        # Plot
        fig = px.sunburst(
            sunburst_data,
            path=['Entrepreneurship_Label', 'Field_Label', 'Salary_Label'],
            values='Count',
            color='Color_Group',  # Mỗi ngành có một màu riêng
            color_discrete_map=color_map,
            title='Entrepreneurship → Field → Salary (Color by Field using RdBu palette)'
        )

        fig.update_traces(maxdepth=2, branchvalues="remainder")


        st.plotly_chart(fig)
