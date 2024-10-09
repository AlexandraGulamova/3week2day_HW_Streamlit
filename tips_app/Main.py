import streamlit as st
import pandas as pd
import datetime
from random import randint
import pages.Heat_map as Heat_map  # Импорт дополнительной страницы
import pages.Tips_dynamics as Tips_dynamics  # Импорт дополнительной страницы
import pages.Tips_sex_smokers as Tips_sex_smokers  # Импорт дополнительной страницы
import pages.Total_bills as Total_bills  # Импорт дополнительной страницы
import io

st.title('Главная страница')
# Загрузка файла через сайдбар
data = st.sidebar.file_uploader('Загрузите CSV файл', type='csv')

if data is not None:
    df = pd.read_csv(data)
    st.session_state.data = df

    if 'data' in st.session_state:
        df = st.session_state.data

        # Создание колонки time_order и новых признаков
        df['time_order'] = [datetime.datetime(2023, 1, randint(1, 31), 12, 0) for i in range(df.shape[0])]
        df.loc[df['time'] == 'Dinner', 'time_order'] += pd.Timedelta(hours=6)
        df['percent'] = df['tip'] / df['total_bill']

        # Отображение данных
        st.write(df.head(10))

        # Выбор страницы
        page = st.sidebar.selectbox("Выберите страницу", ["Главная", "Тепловая карта","Динамика % чаевых во времени","Чаевые и счет в зависимости от пола и курения","Гистограмма, общая сумма чека"])

        if page == "Тепловая карта":
            title=page
            st.title(title)
            Heat_map.run(df)  # Переход на страницу heatmap
        if page == "Динамика % чаевых во времени":
            title=page
            st.title(title)
            Tips_dynamics.run(df)  # Переход на страницу 
        if page == "Чаевые и счет в зависимости от пола и курения":
            title=page
            st.title(title)
            Tips_sex_smokers.run(df)  # Переход на страницу 
        if page == "Гистограмма, общая сумма чека":
            title=page
            st.title(title)
            Total_bills.run(df)  # Переход на страницу 
    else:
        st.warning('Сначала загрузите файл')
        
        
   
else:
    st.stop()