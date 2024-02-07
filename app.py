import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

from matplotlib.ticker import MaxNLocator

st.set_page_config(layout='wide',page_title='Startup Analysis')

df=pd.read_csv('combined.csv')
repair=pd.read_csv('repair_logs.csv')

#df['date']=pd.to_datetime(df['date'],errors='coerce')
#_____data cleaning____

#__________________________________________
st.header('Laptop Inventory Dashboard')

st.sidebar.title('')

option=st.sidebar.selectbox('Select One',['Overall','Repair Logs','Free Laptops'])

if option=='Overall':
    st.title('')
    col1,col2=st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        st.subheader('Job Type Distribution')
        sns.countplot(x='Job Type', data=df, ax=ax)
        st.pyplot(fig)
        total=len(df)
        st.text(f'Total Employees: {total}')
        st.title('')
        b=df.groupby('Brand')['Laptop S/N'].count()

        fig4,ax4=plt.subplots(figsize=(8, 8))
        ax4.pie(b, labels=b.index, autopct=lambda p: '{:.0f}'.format(p * sum(b) / 100), startangle=90, counterclock=False)
        plt.title('Count of Laptops')
        st.pyplot(fig4)

    with col2:

        st.subheader('Laptop conditions')
        fig3, ax3 = plt.subplots()
        sns.countplot(x='New/Refurbished', data=df, ax=ax3)
        st.pyplot(fig3)



elif option=='Repair Logs':
    st.title('Logs')
    st.dataframe(repair)
    st.title('Average repairing Time')
    fig1, ax1 = plt.subplots(figsize=(10,4))
    sns.barplot(data=repair, x='Issue', y='ETA days',ci=None,ax=ax1)
    st.pyplot(fig1)
else:
    df['Job Type'].fillna('No',inplace=True)
    filter = df[df['Job Type']=='No']

    brand_counts = filter['Brand'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(4,5))
    ax2.pie(brand_counts, labels=brand_counts.index, autopct='%1.1f%%', startangle=90, counterclock=False)
    plt.title('Count of Brands that are available')
    st.pyplot(fig2)
    st.title('Free Laptops')

    st.dataframe(filter[['Laptop S/N','Brand']])


