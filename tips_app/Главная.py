import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from random import randint
import datetime

st.write (f"""
# Простое исследование Dataframe tips.csv
        
""")

uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df['time_order']=[datetime.datetime(2023, 1 , randint(1,31),12,0) for i in range(df.shape[0])] 
    df.loc[df['time']=='Dinner','time_order']+=pd.Timedelta(hours=6)
    df['percent']=df['tip']/df['total_bill']
    st.write(df.head(10))
else:
    st.stop()


#path = '/home/alexandra/Documents/ds_bootcamp/HW/datasets/'
#df=pd.read_csv(path+'tips.csv')
#df['time_order']=[datetime.datetime(2023, 1 , randint(1,31),12,0) for i in range(df.shape[0])] 
#df.loc[df['time']=='Dinner','time_order']+=pd.Timedelta(hours=6)
#df['percent']=df['tip']/df['total_bill']
#st.write(df.head(10))
