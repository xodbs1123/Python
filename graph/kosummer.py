import matplotlib.pyplot as plt
import pandas as pd

# 2020년 ~ 2022년까지의 기상청 기후통계자료를 가져옵니다.
df = pd.read_csv('https://raw.githubusercontent.com/kma-opendata/climate-data/main/average/avg_ta_year_2020_2022.csv')

# 여름 기간(6월 ~ 8월)의 평균 기온을 구합니다.
summer_df = df[df['month'].isin([6, 7, 8])]
summer_avg_ta = summer_df['ta'].mean()

# 막대 그래프를 그립니다.
plt.title("한국 여름 평균 기온")
plt.bar(['2020', '2021', '2022'], [summer_avg_ta[2020], summer_avg_ta[2021], summer_avg_ta[2022]], color = ['red', 'blue', 'green'])
plt.xlabel('연도')
plt.ylabel('평균 기온(℃)')
plt.show()