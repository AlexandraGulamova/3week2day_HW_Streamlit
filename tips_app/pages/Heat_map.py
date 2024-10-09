import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def run(df):

    # Создание новых признаков
    df['smoker2'] = df['smoker'].apply(lambda x: 1 if x == 'Yes' else 0)
    df['sex2'] = df['sex'].apply(lambda x: 1 if x == 'Male' else 0)

    # Отбор данных для корреляции
    df_corr = df[['total_bill', 'tip', 'sex2', 'smoker2']]
    correlation_matrix = df_corr.corr()
    # Построение тепловой карты
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, cmap='YlGn', annot=True, fmt='.2f', ax=ax)

    # Отображение графика в Streamlit
    st.pyplot(fig)

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    st.sidebar.download_button("Скачать график", buf, "heatmap.png", "image/png")