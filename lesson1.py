import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel(r"D:/KieuAnh/VGU/BUSINESS IT/MATLAB PYTHON/education_career_success.xlsx")



sns.histplot(data=df,
             x="High_School_GPA",
             stat="density",
             bins=[1.75, 2.25, 2.75, 3.25, 3.75, 4.25],
             color="#8fd5ff",
             edgecolor="#215e99",
             alpha=0.6)
sns.kdeplot(data=df,
            x="High_School_GPA",
            color="#fe5f5e",
            linewidth=2,
            clip=(2, 4))


plt.title("Histogram and Density curve: Distribution of High School GPA",
          fontsize=14,
          fontweight="bold",
          ha='center')
plt.xlabel("High School GPA")
plt.ylabel("Density")
plt.xlim(1.75, 4.25)
plt.xticks([2.0, 2.5, 3.0, 3.5, 4.0])  
plt.tight_layout()


ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


plt.show()

