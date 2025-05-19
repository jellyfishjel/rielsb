import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# 1. Load the data
df = pd.read_excel(r"C:/Users/Admin/Desktop/VGU/Math/phase 4/education_career_success.xlsx")


# 2. Define job levels and color palette
job_level_order = ['Entry', 'Mid', 'Senior', 'Executive']
custom_palette = {
    'Entry': '#8fd5ff',
    'Mid': '#fccc38',
    'Senior': '#d81159',
    'Executive': '#cbf275'
}


# 3. Create violin plot with transparency
plt.figure(figsize=(10, 6))
sns.violinplot(
    data=df,
    x='Current_Job_Level',
    y='University_GPA',
    order=job_level_order,
    palette=custom_palette,
    cut=2,
    inner=None,
    bw=0.2,
    scale='width',
    linewidth=1.2,
    alpha=0.7  # Violin mờ hơn
)


# 4. Overlay a boxplot with same colors
sns.boxplot(
    data=df,
    x='Current_Job_Level',
    y='University_GPA',
    order=job_level_order,
    width=0.15,
    showcaps=True,
    palette=custom_palette,
    boxprops={'edgecolor': 'black', 'linewidth': 1.5},
    whiskerprops={'color': 'black', 'linewidth': 1.5},
    medianprops={'color': 'black', 'linewidth': 1.5},
    flierprops={'markerfacecolor': 'black', 'markeredgecolor': 'black'},
    showfliers=False
)


# 5. Customize the plot appearance
plt.title("Violin Chart of University GPA by Job Level", fontsize=14, fontweight='bold')
plt.xlabel("Job Level", fontsize=12)
plt.ylabel("University GPA", fontsize=12)
plt.xticks(fontsize=18)


# Make grid boxes bigger by reducing number of ticks on y-axis
min_gpa = df['University_GPA'].min()
max_gpa = df['University_GPA'].max()
plt.yticks(np.arange(round(min_gpa, 1), round(max_gpa + 0.1, 1), 0.5), fontsize=18)


# Add thinner grid lines
