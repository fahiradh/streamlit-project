# Proyek Analisis Data: Bike Sharing Dataset
# Nama: Fahira Adindiah
# Email: m010d4kx1699@bangkit.academy

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

df_day = pd.read_csv("day.csv")

st.header('Bike Sharing Dataset')

season_counts = df_day.groupby(by="season").cnt.count()
season_counts.index = season_counts.index.map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
plt.bar(season_counts.index, season_counts)
plt.title('Jumlah Sewa Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sewa')
st.pyplot(plt)

weekday_counts = df_day.groupby(by="weekday").cnt.count()
weekday_counts.index = weekday_counts.index.map({0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'})
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(weekday_counts, labels=weekday_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Jumlah Sewa Berdasarkan Hari dalam Seminggu')
st.pyplot(fig)
