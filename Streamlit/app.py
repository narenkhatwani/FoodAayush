#import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import altair as alt
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
DATA_URL = ("resources/assets/demo.csv")
DATA_URL2 = ("resources/assets/ingredient.csv")

#for data caching
#in streamlit the whole code is rerun everytime so cache would be stored and some error might occur in rare cases
@st.cache(persist=True)
#the above line is to clear the cache on every run command execution

#to load the csv file
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

def load_data2():
    data2 = pd.read_csv(DATA_URL2)
    return data2

#to load the csv file and display it
data = load_data()
data2= load_data2()

#to print a small iframe of the csv file 
#format is 'name displayed above dataset','variable in which csv is loaded'
'Dataset Preview',data

subset_data=data

### MULTISELECT
food_name_input = st.multiselect('Food name',data.groupby('name').count().reset_index()['name'].tolist())

# by food name
if len(food_name_input) > 0:
    subset_data = data[data['name'].isin(food_name_input)]

#sidebar title
st.sidebar.title("Filter data")

#Checkbox for Hospitals
food_list = st.sidebar.selectbox("Select food name", data["name"].unique())



st.markdown(f"<span style='color: black;font-size: 24px;font-weight: bold;'>You selected- {food_list}</span>", unsafe_allow_html=True)


#counts of various nutritional contents of a food item
count_water = data.loc[(data["name"] == food_list) , 'water'].iloc[0]
count_protein = data.loc[(data["name"] == food_list) , 'protcnt'].iloc[0]
count_ash = data.loc[(data["name"] == food_list) , 'ash'].iloc[0]
count_fat = data.loc[(data["name"] == food_list) , 'fatce'].iloc[0]
count_fibretotal = data.loc[(data["name"] == food_list) , 'fibtg'].iloc[0]
count_fibreinsoluble = data.loc[(data["name"] == food_list) , 'fibins'].iloc[0]
count_fibresoluble = data.loc[(data["name"] == food_list) , 'fibsol'].iloc[0]
count_carbohydrate = data.loc[(data["name"] == food_list) , 'choavldf'].iloc[0]
count_energy = data.loc[(data["name"] == food_list) , 'enerc'].iloc[0]

st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Water- {count_water}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Protein- {count_protein}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Ash- {count_ash}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Fat- {count_fat}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Total Fibre- {count_fibretotal}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Insoluble Fibre- {count_fibreinsoluble}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Soluble Fibre- {count_fibresoluble}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Carbohydrates- {count_carbohydrate}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>Energy- {count_energy}kJ</span>", unsafe_allow_html=True)

#sidebar title
st.sidebar.title("Search for Recipe")

'Dataset Preview',data2

#Checkbox for Hospitals
ingredient_1 = st.sidebar.selectbox("Select 1st ingredient name", data2["ing1"].unique())
ingredient_2 = st.sidebar.selectbox("Select 2nd ingredient name", data2["ing2"].unique())
ingredient_3 = st.sidebar.selectbox("Select 3rd ingredient name", data2["ing3"].unique())
ingredient_4 = st.sidebar.selectbox("Select 4th ingredient name", data2["ing4"].unique())
ingredient_5 = st.sidebar.selectbox("Select 5th ingredient name", data2["ing5"].unique())

recipe = data2.loc[(data2['ing1'] == ingredient_1) & (data2['ing2'] == ingredient_2), 'name'].iloc[0]

st.markdown(f"<span style='color: black;font-size: 24px;font-weight: bold;'>Possible Dishes- {recipe}</span>", unsafe_allow_html=True)
