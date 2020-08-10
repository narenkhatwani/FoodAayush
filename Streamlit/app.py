#import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
 
#https://github.com/MarcSkovMadsen/awesome-streamlit
#https://docs.streamlit.io/en/stable/api.html#display-text
#for widget types 
 

# adding title
st.title('Food Aayush')
# adding text    
st.markdown('Food Quality Analysis at your fingertips')



st.sidebar.info("Welcome to Food Aayush Data Analytics. Here you can analyse the nutritional value of food and draw some schematics")

#declare and add sidebar
st.sidebar.title("Menu")

#read csv file
DATA_URL = ("resources/assets/01.csv")


#for data caching
#in streamlit the whole code is rerun everytime so cache would be stored and some error might occur in rare cases
@st.cache(persist=True)
#the above line is to clear the cache on every run command execution

#to load the csv file
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

#to load the csv file and display it
data = load_data()

#to print a small iframe of the csv file 
#format is 'name displayed above dataset','variable in which csv is loaded'
'Dataset Preview',data


x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

water = st.slider("Slider check", 0, 23)

data1 = data[water]== water

"test",data1

