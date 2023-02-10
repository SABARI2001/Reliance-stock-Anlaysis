import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data 
import streamlit as st



df= pd.read_csv("C:\\Users\\DELL\\Downloads\\New folder (3)\\Reliance Industries 1996 to 2020.csv")

st.title('Reliance Stock prediction Analysis')

user_input = st.text_input('Enter Stock Ticker', 'RELIANCE')

df

#Describing Data
st.subheader('Data from Reliance 1996-2020')
st.write(df.describe())

#visualization
st.subheader('Closing Price vs Time chart')
fig = plt.figure(figsize =(12,6))
plt.plot(df.Close)
st.pyplot(fig)


st.subheader('Closing Price vs Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize =(12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)


st.subheader('Closing Price vs Time chart with 100MA & 200 MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize =(12,6))
plt.plot(ma100)
plt.plot(ma200)
plt.plot(df.Close)
st.pyplot(fig)

#Splitting the data into Training and Testing

data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing  = pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])
 