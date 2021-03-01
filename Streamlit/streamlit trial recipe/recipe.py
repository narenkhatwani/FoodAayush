#import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import altair as alt
import json
import matplotlib.patches as mpatches
from matplotlib import cm
from matplotlib.font_manager import FontProperties


# adding title
st.sidebar.markdown(f"<span style='color: black;font-size: 36px;font-weight: bold;'>Food Aayush</span>", unsafe_allow_html=True)

st.sidebar.info("Welcome to Food Aayush Data Analytics. Here you can analyse the nutritional value of food and draw some schematics")


DATA_URL2 = ("recipe.csv")


#for data caching
#in streamlit the whole code is rerun everytime so cache would be stored and some error might occur in rare cases
@st.cache(persist=True)
#the above line is to clear the cache on every run command execution

#to load the csv file


def load_data2():
    data2 = pd.read_csv(DATA_URL2)
    return data2


#to load the csv file and display it

data2= load_data2()



#sidebar title
st.title("Search for a Recipe 😋")
st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>All recipes require a variety of ingredients, such as vegetables, flour, spices and milk products. Here, you can search the possible dishes with any desired combination of ingredients. You can also view the calories in the dish and the cuisine. Please enter a minimum of two ingredients to search for dishes.</h6>",unsafe_allow_html=True)
st.markdown("")

st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Dataset Preview</span>", unsafe_allow_html=True)
data2

all_ingredients1 = ["NA"]
gg = data2.loc[:, data2.columns != 'Name of Dish'].values.tolist()


ingredient_1 = st.selectbox('Search for 1st Ingredient',([
  "NA",
  "Potato",
  "Tomato",
  "Cilantro(Coriander leaves)",
  "Brinjal",
  "Carrot",
  "Coriander",
  "Onion",
  "Drumsticks",
  "Capsicum",
  "None",
  "Cabbage",
  "Peas",
  "Fenugreek",
  "Mushrooms",
  "Spinach",
  "Olives",
  "Sweet corn",
  "Kidney beans(Rajma)",
  "Zucchini",
  "Cauliflower",
  "Bitter Gourd",
  "Cucumber",
  "Beetroot",
  "Garlic",
  "Pumpkin",
  "Beans",
  "Green chilli",
  "Broccoli",
  "Bottle Gourd",
  "Sweet potato",
  "Baby corn",
  "Cluster Beans(Gavar)",
  "Colocasia",
  "Radish",
  "Turnip",
  "Ladyfinger(Okra)",
  "Celery",
  "Soyabean",
  "Mint",
  "Ginger",
  "Black Beans",
  "Lemon juice",
  "Lettuce",
  "Spring Onion",
  "Fennel Bulbs",
  "White Beans",
  "Asparagus",
  "Jalapenos",
  "Leek",
  "Brussels Sprouts",
  "Artichoke",
  "Curry leaves",
  "Ivy Gourd (Tendli)",
  "Yam"
]))
st.write('You selected:', ingredient_1)


ingredient_2 = st.selectbox('Search for 2nd Ingredient',([
  "NA",
  "Tomato",
  "Beans",
  "Garlic",
  "Onion",
  "Peas",
  "Capsicum",
  "Baby corn",
  "Carrot",
  "Curry leaves",
  "Coriander",
  "Potato",
  "None",
  "Bottle Gourd",
  "Cabbage",
  "Mint",
  "Jalapenos",
  "Brinjal",
  "Cucumber",
  "Cauliflower",
  "Ginger",
  "Olives",
  "Fenugreek",
  "Green chilli",
  "Spinach",
  "Sweet corn",
  "Lemon juice",
  "Cilantro(Coriander leaves)",
  "Beetroot",
  "Spring Onion",
  "Mustard Greens",
  "Mushrooms",
  "Leek",
  "Fennel Bulbs",
  "Broccoli",
  "Celery",
  "White Beans",
  "Turnip"
]))
st.write('You selected:', ingredient_2)



ingredient_3 = st.selectbox('Search for 3rd Ingredient',([
  "NA",
  "Onion",
  "Carrot",
  "Mushrooms",
  "Garlic",
  "Pickles",
  "Cabbage",
  "Capsicum",
  "Ginger",
  "Green chilli",
  "Olives",
  "None",
  "Cauliflower",
  "Coriander",
  "Tomato",
  "Pumpkin",
  "Potato",
  "Jalapenos",
  "Curry leaves",
  "Peas",
  "Fenugreek",
  "Beetroot",
  "Sweet corn",
  "Celery",
  "Lemon juice",
  "Cilantro(Coriander leaves)",
  "Lettuce",
  "Kidney beans(Rajma)",
  "Spring Onion",
  "Mint",
  "Spinach",
  "Artichoke"
]))
st.write('You selected:', ingredient_3)

ingredient_4 = st.selectbox('Search for 4th Ingredient',([
  "NA",
  "Peas",
  "None",
  "Olives",
  "Lemon juice",
  "Tomato",
  "Green chilli",
  "Jalapenos",
  "Garlic",
  "Capsicum",
  "Beetroot",
  "Ladyfinger(Okra)",
  "Sweet corn",
  "Beans",
  "Coriander",
  "Onion",
  "Ginger",
  "Cauliflower",
  "Mushrooms",
  "Baby corn",
  "Curry leaves",
  "Cabbage",
  "Carrot",
  "Pickles",
  "Kidney beans(Rajma)",
  "Celery",
  "Mint",
  "Potato",
  "White Beans",
  "Cilantro(Coriander leaves)",
  "Broccoli",
  "Spring Onion",
  "Spinach",
  "Soyabean",
  "Radish"
]))
st.write('You selected:', ingredient_4)

ingredient_5 = st.selectbox('Search for 5th Ingredient',([
  "NA",
  "Moong dal",
  "Whole wheat flour(Atta)",
  "White flour(Maida)",
  "Chickpeas(Chhole)",
  "Rice",
  "Masoor dal",
  "None",
  "Gram(Chana)",
  "Toor dal",
  "Gram flour(Besan)",
  "Urad dal",
  "Chana dal",
  "Oats",
  "Corn flour",
  "Bajra(Millet Flour)",
  "Sabudana",
  "Jowar Flour",
  "Rice Flour",
  "Rawa(Semolina)"
]))
st.write('You selected:', ingredient_5)

ingredient_6 = st.selectbox('Search for 6th Ingredient',([
  "NA",
  "Red Chilli",
  "Garam Masala",
  "Black Pepper",
  "Turmeric",
  "Cumin",
  "Oregano",
  "Cardamom",
  "None",
  "Mustard",
  "Cinnamon",
  "Bay leaves",
  "Parsley",
  "Garlic Cloves",
  "Basil",
  "Coriander seeds",
  "Thyme",
  "Dill",
  "Onion",
  "Fennel seeds",
  "Coriander",
  "Green Chilli",
  "Asafoetida",
  "Ginger",
  "Vanilla",
  "Rosemary",
  "Sesame seeds",
  "Flax Seeds",
  "Saffron",
  "Quinoa",
  "Nigella Seeds",
  "Nutmeg"
]))
st.write('You selected:', ingredient_6)

ingredient_7 = st.selectbox('Search for 7th Ingredient',([
  "NA",
  "Turmeric",
  "Paprika",
  "Black Pepper",
  "Cumin",
  "Cinnamon",
  "Garam Masala",
  "Red Chilli",
  "Oregano",
  "Asafoetida",
  "None",
  "Mustard",
  "Nutmeg",
  "Cardamom",
  "Bay leaves",
  "Garlic Cloves",
  "Fennel seeds",
  "Cloves",
  "Basil",
  "Parsley",
  "Onion",
  "Dill",
  "Green Chilli",
  "Coriander",
  "Sesame seeds",
  "Fenugreek seeds",
  "Ginger",
  "Poppy seeds",
  "Thyme",
  "Cayenne Peppers",
  "Sunflower Seeds",
  "Rosemary"
]))
st.write('You selected:', ingredient_7)

ingredient_8 = st.selectbox('Search for 8th Ingredient',([
  "NA",
  "Asafoetida",
  "None",
  "Oregano",
  "Coriander seeds",
  "Nutmeg",
  "Cinnamon",
  "Fennel seeds",
  "Turmeric",
  "Black Pepper",
  "Garam Masala",
  "Red Chilli",
  "Cumin",
  "Mustard",
  "Saffron",
  "Cloves",
  "Onion",
  "Bay leaves",
  "Paprika",
  "Parsley",
  "Garlic Cloves",
  "Basil",
  "Coriander",
  "Green Chilli",
  "Thyme",
  "Sesame seeds",
  "Dill",
  "Cardamom",
  "Ginger",
  "Kasoori Methi",
  "Flax Seeds",
  "Rosemary",
  "Fenugreek seeds",
  "Sunflower Seeds"
]))
st.write('You selected:', ingredient_8)

ingredient_9 = st.selectbox('Search for 9th Ingredient',([
  "NA",
  "Garam Masala",
  "None",
  "Parsley",
  "Saffron",
  "Turmeric",
  "Bay leaves",
  "Oregano",
  "Mustard",
  "Cardamom",
  "Black Pepper",
  "Coriander seeds",
  "Red Chilli",
  "Fenugreek seeds",
  "Poppy seeds",
  "Cloves",
  "Cumin",
  "Cinnamon",
  "Asafoetida",
  "Basil",
  "Green Chilli",
  "Thyme",
  "Coriander",
  "Cayenne Peppers",
  "Fennel seeds",
  "Onion",
  "Garlic Cloves",
  "Sesame seeds",
  "Kasoori Methi",
  "Dill",
  "Sunflower Seeds",
  "Flax Seeds"
]))
st.write('You selected:', ingredient_9)

ingredient_10 = st.selectbox('Search for 10th Ingredient',([
  "NA",
  "White Bread",
  "None",
  "Pita Bread",
  "Whole Wheat Bread",
  "Baguette",
  "Bun",
  "Papad",
  "French Bread"
]))
st.write('You selected:', ingredient_10)

ingredient_11 = st.selectbox('Search for 11th Ingredient',([
  "NA",
  "Butter",
  "Cheese",
  "None",
  "Ghee",
  "Milk",
  "Paneer(Cottage cheese)",
  "Curd",
  "Sour cream",
  "Buttermilk",
  "Cream"
]))
st.write('You selected:', ingredient_11)


ingredient_list = [ingredient_1,ingredient_2,ingredient_3,ingredient_4,ingredient_5,ingredient_6,ingredient_7,ingredient_8,ingredient_9,ingredient_10,ingredient_11]

#Remove NA keyword from list
ingredient_list = set(filter(lambda x: x != 'NA', ingredient_list))
ingredient_list = list(ingredient_list)

#get all recipe names
all_recipes = list(x for x in data2['Name of Dish'])

#compare ingredients
def intersection(list1,list2):
    list3 = [value for value in list2 if value in list1]
    return list3

score = [0]*len(gg)
for i in range(len(gg)):
    score[i] = len(intersection(gg[i],ingredient_list))

max_score = max(score) if max(score) > 1 or len(ingredient_list)==1 else -999

#find the best match
most_prob = [all_recipes[x] for x in range(len(score)) if score[x] == max_score]
recipe = []

#join results with ,
recipe = ", ".join(most_prob)

st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Possible Dishes- {recipe}</span>", unsafe_allow_html=True)


#background image for the page
page_bg_img = '''
<style>
body {
background-image: url("https://cutewallpaper.org/21/website-background-wallpaper/Geometric-abstract-grey-background-for-bussines-templates-.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)






