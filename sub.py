import pandas as pd
import plotly.express as px

# Đọc file Excel
df = pd.read_excel(r"D:/KieuAnh/VGU/BUSINESS IT/MATLAB PYTHON/education_career_success.xlsx")

# Tạo nhóm điểm SAT
sat_bins = [0, 1000, 1200, 1400, 1600]
sat_labels = ["<1000", "1000–1199", "1200–1399", "1400+"]
df["SAT_Band"] = pd.cut(df["SAT_Score"], bins=sat_bins, labels=sat_labels)

# Tạo nhóm GPA
gpa_bins = [0, 2.5, 3.0, 3.5, 4.0]
gpa_labels = ["<2.5", "2.5–3.0", "3.0–3.5", "3.5–4.0"]
df["GPA_Band"] = pd.cut(df["University_GPA"], bins=gpa_bins, labels=gpa_labels)

# Tạo biểu đồ Sunburst
fig = px.sunburst(
    df,
    path=["Field_of_Study", "SAT_Band", "GPA_Band"],
    values="Job_Offers",
    title="Sunburst Chart: Field of Study → SAT Band → GPA Band → Job Offers"
)

fig.show()