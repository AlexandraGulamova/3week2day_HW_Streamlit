import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from random import randint
import datetime
from random import randint
import datetime
import matplotlib.colors as mcolors
import io

def run(df):
    
    # Загрузка данных
    #path = '/home/alexandra/Documents/ds_bootcamp/HW/datasets/'
    #df = pd.read_csv(path + 'tips.csv')

    # Создание колонки time_order
    df['time_order'] = [datetime.datetime(2023, 1, randint(1, 31), 12, 0) for i in range(df.shape[0])] 
    df.loc[df['time'] == 'Dinner', 'time_order'] += pd.Timedelta(hours=6)

    # Создание новых признаков
    df['percent'] = df['tip'] / df['total_bill']

    df['smoker2'] = 0
    idx = df[df['smoker'] == 'Yes'].index
    df.loc[idx, 'smoker2'] = 1

    # Создание копий данных по полам
    df_female = df[df['sex'] == 'Female']
    df_male = df[df['sex'] == 'Male']

    # Цветовая карта для обозначения курильщиков и некурильщиков
    cmap = mcolors.ListedColormap(['blue', 'red'])
    smoker_labels = ['Non-smoker', 'Smoker']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # График для женщин
    scatter1 = ax1.scatter(df_female['total_bill'], df_female['tip'], c=df_female['smoker2'], cmap=cmap)
    ax1.set_title('Female')
    ax1.set_xlabel('Сумма счета')
    ax1.set_ylabel('Сумма чаевых')

    # Добавляем легенду для женщин
    legend1 = ax1.legend(handles=scatter1.legend_elements()[0], labels=smoker_labels, title="Smoker Status")
    ax1.add_artist(legend1)

    # График для мужчин
    scatter2 = ax2.scatter(df_male['total_bill'], df_male['tip'], c=df_male['smoker2'], cmap=cmap)
    ax2.set_title('Male')
    ax2.set_xlabel('Сумма счета')
    ax2.set_ylabel('Сумма чаевых')

    # Добавляем легенду для мужчин
    legend2 = ax2.legend(handles=scatter2.legend_elements()[0], labels=smoker_labels, title="Smoker Status")
    ax2.add_artist(legend2)

    # Отображение графиков
    plt.tight_layout()
    st.pyplot(fig)

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    st.sidebar.download_button("Скачать график", buf, "tips_sex_smokers.png", "image/png")