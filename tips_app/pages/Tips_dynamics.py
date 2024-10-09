import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from random import randint
import datetime
from random import randint
import datetime
import io

def run(df):
    
    #path = '/home/alexandra/Documents/ds_bootcamp/HW/datasets/'
    #df=pd.read_csv(path+'tips.csv')
    df['time_order']=[datetime.datetime(2023, 1 , randint(1,31),12,0) for i in range(df.shape[0])] 
    df.loc[df['time']=='Dinner','time_order']+=pd.Timedelta(hours=6)
    df['percent']=df['tip']/df['total_bill']



    #________________________
    #график 1, динамика чаевых  во времени
    df2=pd.pivot_table(df,index='time_order',values=['total_bill','tip'],aggfunc=np.sum).reset_index()
    df2['percent']=df2['tip']/df2['total_bill']
    x=df2['time_order']
    y=df2['percent']

    #plt.figure(figsize=(30,3))
    plt.plot(x,y)
    plt.ylabel('доля от счета')
    plt.title('Динамика доли от общего чека чаевых')
    st.pyplot(plt)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    st.sidebar.download_button("Скачать график", buf, "tips_dynamics.png", "image/png")

