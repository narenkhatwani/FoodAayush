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
#for demo purpose 

# adding title
st.title('Food Aayush')
# adding text    
st.markdown('Food Quality Analysis at your fingertips')

st.sidebar.info("Welcome to Food Aayush Data Analytics. Here you can analyse the nutritional value of food and draw some schematics")

#declare and add sidebar
st.sidebar.title("Menu")

#read csv file
DATA_URL = ("resources/assets_modified/01.csv")
DATA_URL2 = ("resources/assets_modified/ingredient.csv")

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

st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'> ->Dataset Preview</span>", unsafe_allow_html=True)

data

subset_data=data

### MULTISELECT
#food_name_input = st.multiselect('Food name',data.groupby('name').count().reset_index()['name'].tolist())

# by food name
#if len(food_name_input) > 0:
 #   subset_data = data[data['name'].isin(food_name_input)]

#sidebar title
st.sidebar.title("Filter data")

#Checkbox for Hospitals
food_list = st.sidebar.selectbox("Select food name", data["name"].unique())


st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'> ->Filter Data Results</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>You selected- {food_list}</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Nutritional Analysis for filtered Data is as follows-</span>", unsafe_allow_html=True)

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

st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Water- {count_water}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Protein- {count_protein}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Ash- {count_ash}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Fat- {count_fat}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Total Fibre- {count_fibretotal}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Insoluble Fibre- {count_fibreinsoluble}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Soluble Fibre- {count_fibresoluble}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Carbohydrates- {count_carbohydrate}g</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Energy- {count_energy}kJ</span>", unsafe_allow_html=True)

#sidebar title
st.sidebar.title("Search for Recipe")
st.sidebar.markdown("Minimum Two ingredients required")

st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'> ->Dataset Preview</span>", unsafe_allow_html=True)
data2

#Get All Ingredients from CSV
all_ingredients = ["NA"]
gg = data2.loc[:, data2.columns != 'name'].values.tolist()
# all_dishes = list(x for x in data2['name'])

# dish_dict = dict(zip(all_dishes,gg))
# st.markdown(dish_dict)

for i in gg:
    for j in i:
        all_ingredients.append(j)

#To remove Duplicates
all_ingredients = list(dict.fromkeys(all_ingredients))
# st.markdown(all_ingredients)

#Dropdown for ingredients
ingredient_1 = st.sidebar.selectbox("Select 1st ingredient name", all_ingredients)
ingredient_2 = st.sidebar.selectbox("Select 2nd ingredient name", all_ingredients)
ingredient_3 = st.sidebar.selectbox("Select 3rd ingredient name", all_ingredients)
ingredient_4 = st.sidebar.selectbox("Select 4th ingredient name", all_ingredients)
ingredient_5 = st.sidebar.selectbox("Select 5th ingredient name", all_ingredients)

ingredient_list = [ingredient_1,ingredient_2,ingredient_3,ingredient_4,ingredient_5]

#Remove NA keyword from list
ingredient_list = set(filter(lambda x: x != 'NA', ingredient_list))
ingredient_list = list(ingredient_list)
# st.markdown(ingredient_list)

#got all recipe names
all_recipes = list(x for x in data2['name'])
# st.markdown(gg)

#compare ingredients
def intersection(list1,list2):
    list3 = [value for value in list2 if value in list1]
    return list3

score = [0]*len(gg)
for i in range(len(gg)):
    score[i] = len(intersection(gg[i],ingredient_list))
 
max_score = max(score) if max(score) > 1 or len(ingredient_list)==1 else -999

# st.markdown(max_score)

most_prob = [all_recipes[x] for x in range(len(score)) if score[x] == max_score]
recipe = []
# st.markdown(score)
# st.markdown(most_prob)
recipe = ", ".join(most_prob)

st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Possible Dishes- {recipe}</span>", unsafe_allow_html=True)

st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>->Add your total daily intake of calories</span>", unsafe_allow_html=True)

x = st.slider('(in terms of Calories)',0,3000)

fat_value= x*(30/100)
sat_fat_value= x*(7/100)
trans_fat_value= x*(1/100)
total_carbs_value= x*(50/100)
protein_value= x*(20/100)

st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Total Fat content should be- {fat_value} Cal</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Saturated Fat count should be- {sat_fat_value} Cal</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Trans Fat count should be- {trans_fat_value} Cal</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Total Carbohydrates count should be- {total_carbs_value} Cal</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Protein count should be- {protein_value} Cal</span>", unsafe_allow_html=True)


st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>->Want to know your ideal calorie intake ??</span>", unsafe_allow_html=True)

st.markdown(f"<span style='color: black;font-size: 20px;font-weight: bold;'>Choose your gender</span>", unsafe_allow_html=True)
gender = st.selectbox('*Your calorie intake depends on your gender',('Male', 'Female', 'Other','Rather Not Say'))

st.markdown(f"<span style='color: black;font-size: 20px;font-weight: bold;'>You selected: {gender}</span>", unsafe_allow_html=True)

if (gender == 'Male'):
    st.markdown(f"<span style='color: blue;font-size: 18px;font-weight: bold;'>Your ideal daily calorie intake should be 2500 Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 18px;font-weight: bold;'>Your ideal daily water intake should be 3.7 L</span>", unsafe_allow_html=True)
elif (gender == 'Female'):
    st.markdown(f"<span style='color: blue;font-size: 18px;font-weight: bold;'>Your ideal daily calorie intake should be 2000 Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 18px;font-weight: bold;'>Your ideal daily water intake should be 2.7 L</span>", unsafe_allow_html=True)
elif (gender == 'Other'):
    st.markdown(f"<span style='color: blue;font-size: 18px;font-weight: bold;'>Sorry, info not available :)</span>", unsafe_allow_html=True)
else:
    st.markdown(f"<span style='color: blue;font-size: 18px;font-weight: bold;'>Sorry, info not available :)</span>", unsafe_allow_html=True)





nutrition_labels = ['Protein','Fats','Fruits and Veg','Fibre Rich Carbs']

colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
fig5 = go.Figure(data=[go.Pie(labels=nutrition_labels, values=[25,10,40,25])])
fig5.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,marker=dict(colors=colors, line=dict(color='#000000', width=2)))
st.plotly_chart(fig5)