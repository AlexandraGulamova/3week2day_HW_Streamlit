import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from random import randint
import datetime
from random import randint
import datetime
st.title('Гистограмма, общая сумма чека')


path = '/home/alexandra/Documents/ds_bootcamp/HW/datasets/'
df=pd.read_csv(path+'tips.csv')
df['time_order']=[datetime.datetime(2023, 1 , randint(1,31),12,0) for i in range(df.shape[0])] 
df.loc[df['time']=='Dinner','time_order']+=pd.Timedelta(hours=6)
df['percent']=df['tip']/df['total_bill']


plot=sns.displot(df,x='total_bill', bins=20,kind='hist')
st.pyplot(plot.fig)