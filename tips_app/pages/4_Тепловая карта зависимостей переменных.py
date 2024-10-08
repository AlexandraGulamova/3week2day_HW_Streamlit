import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from random import randint
import datetime

st.title('Тепловая карта зависимостей численных переменных')

# Загрузка данных
path = '/home/alexandra/Documents/ds_bootcamp/HW/datasets/'
df = pd.read_csv(path + 'tips.csv')

# Создание колонки time_order
df['time_order'] = [datetime.datetime(2023, 1, randint(1, 31), 12, 0) for i in range(df.shape[0])] 
df.loc[df['time'] == 'Dinner', 'time_order'] += pd.Timedelta(hours=6)

# Создание новых признаков
df['percent'] = df['tip'] / df['total_bill']

df['smoker2'] = 0
idx = df[df['smoker'] == 'Yes'].index
df.loc[idx, 'smoker2'] = 1

df['sex2'] = 0
idx = df[df['sex'] == 'Male'].index
df.loc[idx, 'sex2'] = 1

# Отбор данных для корреляции
df4 = df[['total_bill', 'tip', 'sex2', 'smoker2']]
correlation_matrix = df4.corr()

# Построение тепловой карты
fig, ax = plt.subplots(figsize=(10, 6))  # Создание фигуры и осей
sns.heatmap(correlation_matrix, cmap='YlGn', annot=True, fmt='.2f', ax=ax)  # Тепловая карта

# Отображение графика в Streamlit
st.pyplot(fig)
