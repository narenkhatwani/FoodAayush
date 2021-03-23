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
import seaborn as sns

# adding title in streamlit
st.sidebar.markdown(f"<span style='color: black;font-size: 36px;font-weight: bold;'>Food Aayush</span>", unsafe_allow_html=True)

st.sidebar.info("Welcome to Food Aayush Data Analytics. Here you can analyse the nutritional value of food and draw some schematics")

#read csv file
DATA_URL = ("resources/assets_modified/01.csv")

DATA_URL2 = ("resources/recipe_page/recipe.csv")


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

#global variable/dataframe
#path to the csv file of the ifct database for demographics page
df_demographics = pd.read_csv("resources/assets_modified/01cat.csv")
    
df_demographics.dropna()


def main():
    # Register your pages
    pages = {
        "About": about_page,
        "Ingredient Information": page_first,
        "IFCT Demographics": demographic_main,
        "Disease vala tab":disease_demographics,
        "Search for Recipe": page_second,
        "Calorie Calculator": page_three,
        "Heart Disease Map": page_fourth,
        "Food Matrix": page_five,
        
    }
    st.sidebar.title("Navigation 🧭")
    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    # Display the selected page
    pages[page]()

    st.sidebar.subheader("Check out our [Github Repository](https://github.com/narenkhatwani/FoodAayush)")
def about_page():
    st.markdown("<h1 style='text-align: center;'>Food Aayush 🍲 🩺</h1>", unsafe_allow_html=True)
    
    st.subheader("About FoodAayush 🤔")

    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial, sans-serif;line-height: 1.5;'>Food is an essential parameter that plays an important role in the survival of humans. It also plays a major part in depicting a country’s culture. Healthy, nutritious, and high-quality food results in not only a better lifestyle but also develops a person’s immunity and health. Likewise, the consumption of low-quality food which might be deprived of nutritional value impacts a person’s health negatively and makes them susceptible to all types of diseases. In India, there is a persistent complaint, in any civic body-related food section, about the quality of meals available. Likewise, the quality of the oil is also an important factor while cooking any meal. Therefore, the Quality of oil used in frying the food to affect its taste must be monitored too. Its continuous exposure to relatively high temperatures results in degradation of its quality. The purpose of this study is to build an application for the detection of the quality of food and also to detect repeated frying on cooking oils based on the visual properties of the oils. Classification of food items is done on the basis of time left for consumption, edibility, quality, color, and rancidity. The food items are further classified as stale or usable using artificial intelligence algorithms based on the images acquired through a Cell Phone’s camera.</h6>", unsafe_allow_html=True)
    st.markdown("")
    st.subheader("Activity Diagram ♺")
    st.image('resources/about_process_diagram/1.png')

    st.markdown("")
    st.subheader("Classification of food items and cooking oils based on quality")
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>Food becomes stale if there is excessive exposure to environmental factors such as heat and humidity. Similarly, if a cooking oil sample is exposed to heat, or is used in cooking repeatedly, it will become rancid. The second part of our application is the classification of food items based on their freshness and oils based on their rancidity. A classification model is developed for classifying food items into various freshness levels based on their visual properties. For oils, the classification is done on the basis of the visual properties as well as the pH value of the oil sample. The pH value is recorded using a pH sensor integrated with the application. These features are included in our mobile application which is developed using the Flutter toolkit.</h6>", unsafe_allow_html=True)
    
    #background image for the webapp
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://cutewallpaper.org/21/website-background-wallpaper/Geometric-abstract-grey-background-for-bussines-templates-.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


def page_first():
    
    st.title("Ingredient Information 🍅 🥕 🥒 ")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.2;'>In order to ensure proper development and growth of the body, immunity against diseases, and energy to function throughout the day, it is necessary to consume adequate amounts of all nutrients, including proteins, carbohydrates, fats, vitamins, minerals and water. Therefore, the nutritional value of any food item being consumed is a very important parameter. The content of different nutrients in various foods, consumed either individually or as ingredients in dishes can be found here.</h6>",unsafe_allow_html=True)

    
    food_list = st.selectbox("Search your ingredient here:", data["name"].unique())


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Filter Data Results are :</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>You selected- {food_list}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Nutritional Analysis for your selection is as follows-</span>", unsafe_allow_html=True)

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

    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Water- {count_water}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Protein- {count_protein}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Ash- {count_ash}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Fat- {count_fat}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Total Fibre- {count_fibretotal}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Insoluble Fibre- {count_fibreinsoluble}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Soluble Fibre- {count_fibresoluble}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Carbohydrates- {count_carbohydrate}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Energy- {count_energy}kJ</span>", unsafe_allow_html=True)
    

    #infct information
    st.subheader("Some Information about the data source 📊")
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>The above data is taken from the dataset “Indian Food Composition Tables, 2017”, of the National Institute of Nutrition. The approach taken for creation of this dataset was to sample the key foods from all over India which contribute to the nutrient intake of 75% of the population. The consumption data and nutrient composition for the various foods is found and the foods have been ranked according to their contribution to the diet in terms of nutrients.</h6>", unsafe_allow_html=True)
    st.markdown("")
    
    #to print a small iframe of the csv file
    raw_data=st.checkbox('See Raw Data')
    if raw_data: 
        st.write(data)

    

    #ifct image
    st.image("resources/ingredient_page/ifct_cover.png")
    #background image for the webapp
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://cutewallpaper.org/21/website-background-wallpaper/Geometric-abstract-grey-background-for-bussines-templates-.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)



def page_second():
    #sidebar title
    st.title("Search for a Recipe 😋")
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>All recipes require a variety of ingredients, such as vegetables, flour, spices and milk products. Here, you can search the possible dishes with any desired combination of ingredients. You can also view the calories in the dish and the cuisine. Please enter a minimum of two ingredients to search for dishes.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Dataset Preview 📋</span>", unsafe_allow_html=True)
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
    
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Possible Dishes ⬇️ </span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #000080;font-size: 22px;font-weight: bold;'>{recipe}</span>", unsafe_allow_html=True)
    

    st.title("View calories and cuisine of a dish 🥗 🧑🏾‍🤝‍🧑🏼")

    dish_name = st.selectbox("Search your dish here:", data2["Name of Dish"].unique())


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Filter Data Results are :</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>You selected- {dish_name}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Analysis for your selection is as follows-</span>", unsafe_allow_html=True)

    #counts of various nutritional contents of a food item
    count_calories = data2.loc[(data2["Name of Dish"] == dish_name) , 'Calories'].iloc[0]
    cuisine = data2.loc[(data2["Name of Dish"] == dish_name) , 'Cuisine'].iloc[0]
    
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Calorie Count - {count_calories} kCal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Cuisine - {cuisine}</span>", unsafe_allow_html=True)
  
    

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
    
 
def page_three():
    st.title("Calorie Calculator 🍲 🧮")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Nutrients are classified into two categories, macronutrients and micronutrients. Macronutrients are those nutrients which are required in large quantities, and include carbohydrates, proteins, fats and water. Micronutrients are those which are required in relatively small quantities, and include vitamins and minerals. Adequate amounts of these nutrients are required to maintain good health. The adequate amounts vary from person to person, and also depend on the person’s daily calorie consumption. Moreover, the ideal calorie consumption for a person also depends on various factors, including gender. Here, you can find your ideal consumption of various nutrients depending on your daily calorie consumption, and can also find your ideal daily calorie consumption based on your gender.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Add your total daily intake of calories</span>", unsafe_allow_html=True)

    x = st.slider('(in terms of Calories)',0,3000)

    fat_value= x*(30/100)
    sat_fat_value= x*(7/100)
    trans_fat_value= x*(1/100)
    total_carbs_value= x*(50/100)
    protein_value= x*(20/100)

    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Total Fat count should be- {fat_value} Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Saturated Fat count should be- {sat_fat_value} Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Trans Fat count should be- {trans_fat_value} Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Total Carbohydrates count should be- {total_carbs_value} Cal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Protein count should be- {protein_value} Cal</span>", unsafe_allow_html=True)


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Want to know your ideal calorie intake ??</span>", unsafe_allow_html=True)

    st.markdown(f"<span style='color: black;font-size: 20px;font-weight: bold;'>Choose your gender ⚥</span>", unsafe_allow_html=True)
    gender = st.selectbox('*Your calorie intake depends on your gender',('Male', 'Female', 'Other','Rather Not Say'))

    st.markdown(f"<span style='color: black;font-size: 20px;font-weight: bold;'>You selected: {gender}</span>", unsafe_allow_html=True)

    if (gender == 'Male'):
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Your ideal daily calorie intake should be 2500 Cal</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Your ideal daily water intake should be 3.7 L</span>", unsafe_allow_html=True)
    elif (gender == 'Female'):
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Your ideal daily calorie intake should be 2000 Cal</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Your ideal daily water intake should be 2.7 L</span>", unsafe_allow_html=True)
    elif (gender == 'Other'):
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Sorry, info not available :)</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='color: #367588;font-size: 19px;font-weight: bold;'>Sorry, info not available :)</span>", unsafe_allow_html=True)
    #background image for the webapp
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://cutewallpaper.org/21/website-background-wallpaper/Geometric-abstract-grey-background-for-bussines-templates-.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


def page_fourth():
    st.title('Indian Map for Heart Disease 🫀')
    st.header("Data from 2017 - In DALYs Per 100,000 People")
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The disability-adjusted life year (DALY) is a measure of overall disease burden, expressed as the number of years lost due to ill-health, disability or early death. The below map shows the DALY associated with heart disease for each state in India.</h6>",unsafe_allow_html=True)
    st.markdown("")
    #loading Map data from CSV file
    df = pd.read_csv("resources/streamlit_map/cases2.csv")
    df2 = pd.read_csv("resources/streamlit_map/Heart_disease_display.csv")

    #to print a small iframe of the csv file
    raw_data=st.checkbox('See Raw Data')
    if raw_data: 
        st.write(df2)
    
    #Data Source
    #https://www.factchecker.in/punjab-tamil-nadu-haryana-have-highest-burden-of-heart-disease-in-india/

    #For plotly visuals
    #https://plotly.com/python/builtin-colorscales/

    #Loading JSON file
    #File Source: https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson
    with open("resources/streamlit_map/india_states.geojson") as json_file:
        indian_map = json.load(json_file)

    fig11 = go.Figure(data=go.Choropleth(
        geojson=indian_map,
        featureidkey='properties.ST_NM',
        locationmode='geojson-id',
        locations=df['state'],
        z=df['active cases'],

        autocolorscale=False,
        colorscale='darkmint',
        marker_line_color='black',

        colorbar=dict(
            title={'text': "No of patients"},

            thickness=15,
            len=0.35,
            bgcolor='rgba(255,255,255,0.6)',

            tick0=0,
            dtick=20000,

            xanchor='left',
            x=0.01,
            yanchor='bottom',
            y=0.05
        )
    ))

    fig11.update_geos(
        visible=False,
        projection=dict(
            type='conic conformal',
            parallels=[12.472944444, 35.172805555556],
            rotation={'lat': 24, 'lon': 80}
        ),
        lonaxis={'range': [68, 98]},
        lataxis={'range': [6, 38]}
    )

    fig11.update_layout(
        title=dict(
            text="",
            xanchor='center',
            x=0.5,
            yref='paper',
            yanchor='bottom',
            y=1,
            pad={'b': 10}
        ),
        margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
        height=550,
        width=550
    )


    st.plotly_chart(fig11)


    df_statefood = pd.read_csv("resources/streamlit_map/State_food.csv")  # read a CSV file inside the 'data" folder next to 'app.py'


    st.title("Prominent Heart Disease causing Foods")  # add a title
    st.subheader("(Example- 🍟,🍕,🧁)")
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>One of the major causes of heart disease is the consumption of unhealthy food. In India, heart disease is a serious and widespread problem due to the excessive use of oil, spices and salt in cooking. Excessive use of oil increases cholesterol, which contributes to heart disease. Although spices are good for health, excessive consumption of chilli peppers is not good for the heart. Excessive consumption of salt increases blood pressure which also leads to coronary heart disease.</h6",unsafe_allow_html=True)

    st.subheader("Calorie Content of Heart Disease causing Foods in each Indian State ✔️")
   
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>There are many cuisines in India, as each state has its own popular foods. In each of these cuisines, there are many unhealthy food items which may contribute to heart disease. The below data shows popular food items from each of the Indian states which contribute to heart disease, along with their calorie content.</h6",unsafe_allow_html=True)

    st.markdown("")
    
    st.write(df_statefood)  # visualize my dataframe in the Streamlit app

    st.title("View Statewise food trend 🥗 ")
    
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>Each state in India has its own unique cuisine. In all Indian cuisines, there are food items that are high in fat, or consist of other ingredients that may contribute to heart disease. Here are some popular  Indian food items that can increase a person’s risk of heart disease. Please enter a state in the dropdown below. You can find an unhealthy food item specific to that state, along with its calorie content and the reason why it may contribute to heart disease.</h6",unsafe_allow_html=True)

    state_name = st.selectbox("Search your state here:", df_statefood["States"].unique())

    

    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>You selected- {state_name}</span>", unsafe_allow_html=True)
    
    #counts of various nutritional contents of a food item
    item_name = df_statefood.loc[(df_statefood["States"] == state_name) , 'Food Items'].iloc[0]
    calorie_count = df_statefood.loc[(df_statefood["States"] == state_name) , 'Calories'].iloc[0]
    reason_item = df_statefood.loc[(df_statefood["States"] == state_name) , 'Reason '].iloc[0]

    st.subheader("Popular dish in this state is :")
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>{item_name}</span>", unsafe_allow_html=True)
    st.subheader("Its calorie count is:")
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>{calorie_count} kCal </span>", unsafe_allow_html=True)
    st.subheader("Reason for possible contribution to heart disease -")
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'> {reason_item}</span>", unsafe_allow_html=True)
  

def page_five():
    df = pd.read_csv("resources/Food_Matrix/Food_Matrix1.csv")  # read a CSV file inside the 'data" folder next to 'app.py'


    st.title("Food Matrix 🍔")  # add a title
    st.markdown("There are many combinations of foods which are harmful to human health, and are still consumed by people due to lack of awareness. These include combinations of generalized food categories and also of specific food items. These combinations can be indicated using a matrix. There are two matrix representations below that indicate harmful combinations of foods. The first one is for generalized food categories while the second one is for specific food items.")

    st.subheader("1. Food Compatibility Matrix (Food Categories)")
    st.markdown("There are certain combinations of foods which are harmful to health when consumed together. They may become difficult to digest, and may cause problems such as acidity. They may even be toxic and lead to diseases. For example, fruits should be consumed separately and not with any meal. It is necessary for people to be aware of such food combinations, so that they do not consume them together, or use them together in cooking. The below data shows various combinations of generalized food categories, and indicates which of these combinations are harmful (toxic) or harmless (non-toxic). ")
    
    df_display1 = pd.read_csv("resources/Food_Matrix/Food_Matrix1.csv")
    
    df = pd.read_csv("resources/Food_Matrix/Food_Matrix1.csv")

    raw_data=st.checkbox('See Raw Data')
    if raw_data: 
        st.write(df)

    st.subheader("Visualization of the raw data 📈")  # add a title
    data = pd.read_csv('resources/Food_Matrix/Food_Matrix1.csv' , na_values= "NaN")
    data.fillna(0 , inplace = True)


    id_labels = data.columns[1:]
    
    # take the transpose since you want to see id on y-axis
    id_matrix = np.array(data[id_labels].values, dtype=float).T

    fig, ax = plt.subplots(figsize=(8,8))


    mat = ax.imshow(id_matrix, cmap="Reds", interpolation='nearest')

    plt.yticks(range(id_matrix.shape[0]), id_labels)
    plt.xticks(range(id_matrix.shape[1]), id_labels)
    plt.xticks(rotation=25)

    blue_patch = mpatches.Patch(color='maroon', label='Toxic')
    white_patch = mpatches.Patch(color='#FFF5F0', label='Non-Toxic')


    fontP = FontProperties()
    fontP.set_size('xx-small')

    #legend outside
    plt.legend(handles = [blue_patch , white_patch], bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size':15}) 

    plt.xlabel('Food Compatibility Matrix (Food Categories)')


    st.pyplot(plt,dpi=100)

    st.subheader("2. Food compatibility matrix (For harmful combinations of specific food items)")
    st.markdown("Apart from the above generalized categories, there are some specific food items which are harmful when consumed together. Most people are not aware of these combinations. A prominent example is banana milkshake. It is a popular beverage but most people are not aware that milk should not be consumed with bananas as it causes heaviness and may also lead to lethargy. Such combinations of food items are indicated in the below data.")

    df2 = pd.read_csv("resources/Food_Matrix/Food_Matrix2.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

    df21 = pd.read_csv("resources/Food_Matrix/Food_Matrix2.csv")

    raw_data2= st.checkbox('See Raw Data ')
    if raw_data2: 
        st.write(df21)


    st.subheader("Visualization of the above given data 📈")  # add a title
    data2 = pd.read_csv('resources/Food_Matrix/Food_Matrix2.csv' , na_values= "NaN")
    data2.fillna(0 , inplace = True)


    id_labels = data2.columns[1:]
    
    # take the transpose since you want to see id on y-axis
    id_matrix = np.array(data2[id_labels].values, dtype=float).T

    fig, ax = plt.subplots(figsize=(8,8))


    mat = ax.imshow(id_matrix, cmap="Blues", interpolation='nearest')

    plt.yticks(range(id_matrix.shape[0]), id_labels)
    plt.xticks(range(id_matrix.shape[1]), id_labels)
    plt.xticks(rotation=25)

    blue_patch = mpatches.Patch(color='#0b306b', label='Toxic')
    white_patch = mpatches.Patch(color='#f7fbff', label='Non-Toxic')


    fontP = FontProperties()
    fontP.set_size('xx-small')

    #legend outside
    plt.legend(handles = [blue_patch , white_patch], bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size':15}) 


    #plt.legend(handles = [blue_patch , white_patch],title='title', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size':15}) 

    #legend inside
    #plt.legend(handles = [blue_patch , white_patch])

    plt.xlabel('For harmful combinations of specific food items')


    st.pyplot(plt,dpi=100)


def demographic_main():
    # Register your pages
    pages = {
        "1. Dataset Pruning and Exploration": demographic_pruning_page,
        "2. Correlation between presence of Nutrients":demographic_correlation_page,
        "3. Analysis of Nutrient Content":demographic_nutrient_analysis_page,
        "4. Categorized distribution of Nutrients":demographic_categorized_page,
        "5. 3D relation":demographic_dimensional_page,
        "6. foodgroup":demographic_foodgroup_page
    }


    st.title("Navigate through demographics 🧭")

    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    # Display the selected page
    pages[page]()

def demographic_pruning_page():
    st.title("Dataset Pruning and Exploration")

    #description of the demographics page
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Before performing any analysis on the data, it is necessary to prune the dataset. This is mainly done to remove any discrepancies in the data, which may cause a hindrance to the data analysis.The following are some ways in which the dataset can be pruned to make it fit for analysis.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #display the data frame with checkbox
    raw_data=st.checkbox('See Raw Data')
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The following are some of the steps undertaken by us in order to make the dataset fit for analysis.</h6>",unsafe_allow_html=True)

    if raw_data: #checkbox true or not 
        st.write(df_demographics.head(10))

    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>1. Checking the data types</span>", unsafe_allow_html=True)
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>In this step, we check the data types of all the parameters before moving ahead with the analysis. This is done to ensure that the analysis is done smoothly without the hassle of getting any data type errors during visualization.</h6>",unsafe_allow_html=True)
    
    st.markdown("")

    #print data types of columns
    st.write(df_demographics.dtypes)

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'> Therefore, all our data is in desired datatypes.</h6>",unsafe_allow_html=True)

    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>2. Quick last checks on data quality</span>", unsafe_allow_html=True)
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>To obtain accurate results, it is necessary to ensure that the dataset is complete and of good quality.</h6>",unsafe_allow_html=True)
    
    st.subheader("Null Value Check")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The next step is checking the presence of null values in the dataset. This is important to avoid obtaining biased results due to missing data. The dataset is checked column-wise for null values, and no null values are found.</h6>",unsafe_allow_html=True)
    
    st.markdown("")
    
    #null values check
    st.write(df_demographics.isnull().any())
    
    st.subheader("Descriptions of all the parameters")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Now, to analyze the parameters (columns) in the dataset, which are the quantities of various nutrients present in the food items, some mathematical operations have been performed on the columns. The count, the mean and standard deviation, the minimum and maximum of the values in each column are calculated as shown below.</h6>",unsafe_allow_html=True)

    st.markdown("")

    #values 
    st.write(df_demographics.describe())
   
def demographic_correlation_page():
    st.title("Correlation between presence of nutrients")
    
    #description of the demographics page
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>There is a relationship between the amounts of different nutrients present in food items. Every food item is not rich in all nutrients. Certain food items are richer in proteins, while others may be abundant in carbohydrates and so on. Here, we show the relationship between different nutrients in the food items present in the dataset.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.0, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['choavldf'],df_demographics['protcnt'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Carbohydrates")

    #kde plot title Y axis
    plt.ylabel("Protein")

    #kde plot title    
    plt.title("Carbohydrates and Protein")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  

    #2nd plot

    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.25, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['fatce'],df_demographics['choavldf'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Fats")

    #kde plot title Y axis
    plt.ylabel("Carbohydrates")

    #kde plot title    
    plt.title("Fats and Carbohydrates")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  

    #3rd plot
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.33, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['choavldf'],df_demographics['fibtg'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Carbohydrates")

    #kde plot title Y axis
    plt.ylabel("Fiber")

    #kde plot title    
    plt.title("Carbohydrates and Fiber")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  

    #4th plot
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.45, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['fibtg'],df_demographics['fatce'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Fiber")

    #kde plot title Y axis
    plt.ylabel("Fat")

    #kde plot title    
    plt.title("Fiber and Fat")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  

    #5th plot
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.56, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['fatce'],df_demographics['fasat'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Total Fat")

    #kde plot title Y axis
    plt.ylabel("Saturated Fat")

    #kde plot title    
    plt.title("Total Fat and Saturated Fat")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  

    #6th plot
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.68, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['choavldf'],df_demographics['enerc'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Carbohydrates")

    #kde plot title Y axis
    plt.ylabel("Energy (in kJ)")

    #kde plot title    
    plt.title("Carbohydrates and Eneegy")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  


def demographic_nutrient_analysis_page():
    st.title("Analysis of Nutrient content")
    
    #description of the demographics page
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Certain foods have higher proportions of specific nutrients than others. The most notable example is that meat, fish, and eggs contain higher amounts of protein than plant-based foods. Here, the data is analyzed to find the foods with the highest amounts of various nutrients, including proteins, carbohydrates, and fats. This is explained with the help of graphical representations.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Analysis of Protein Content</span>", unsafe_allow_html=True)
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>First, we have found the foods having the highest amounts of protein and have represented the amounts of protein in these foods graphically.</h6>",unsafe_allow_html=True)
    st.markdown("")
    #Based on categories
    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']


    prot= df_demographics[df_demographics['category'].isin(categories)]

    protein_rich= prot.sort_values(by='protcnt', ascending= False)
    
    top_20=protein_rich.head(20)
    
    fig = px.bar(top_20, x='name', y='protcnt', color='protcnt', title=' Top 10 protein rich foods')
    fig.update_layout(title='Title', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)


def demographic_categorized_page():
    st.title("Categorized distribution of Nutrients")

    #description of the demographics page
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Here, for each nutrient, the quantities of that nutrient present in each food item in the dataset are summed up to find that nutrient’s total quantity.  Then, the percentage of this total quantity present in each food category is found. These percentages are represented graphically in the form of a pie chart. This process is carried out for each nutrient. The pie charts for each nutrient are displayed below.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #category wise statistics
    category_dist= df_demographics.groupby(['category']).sum()
    st.write(category_dist)

    fig = make_subplots(rows=3, cols=2,specs=[[{"type": "domain"},{"type": "domain"}],[{"type": "domain"},{"type": "domain"}],[{"type": "domain"},{"type": "domain"}]])
    
    fig.add_trace(go.Pie(values=category_dist['protcnt'].values, title='CALORIES', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=1, col=1)
    
    fig.add_trace(go.Pie(values=category_dist['protcnt'].values,title='FAT', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=1, col=2)

    fig.add_trace(go.Pie(values=category_dist['protcnt'].values,title='PROTEIN', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=2, col=1)

    fig.add_trace(go.Pie(values=category_dist['protcnt'].values,title='FIBER', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=2, col=2)

    fig.add_trace(go.Pie(values=category_dist['protcnt'].values,title='SAT.FAT', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=3, col=1)

    fig.add_trace(go.Pie(values=category_dist['protcnt'].values,title='CARBS', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=3, col=2)
    
    fig.update_layout(title_text="Category wise distribution of all metrics",height=1200, width=800)
    
    st.plotly_chart(fig)


    #high protein seafood items 
    seafood= df_demographics[df_demographics['category'].isin(['Seafood'])]

    seafood_top=seafood.sort_values(by='protcnt', ascending= False)
    
    seafood_top=seafood_top.head(10)

    fig_protein_seafood = go.Figure(go.Funnelarea(values=seafood_top['protcnt'].values, text=seafood_top['name'],title = { "text": "Seafood with high protein percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_protein_seafood.update_layout(height=600, width=700)

    st.plotly_chart(fig_protein_seafood)

    #high protein legumes (for vegetarians)
    legumes= df_demographics[df_demographics['category'].isin(['Legumes'])]

    legumes_top=legumes.sort_values(by='protcnt', ascending= False)
    
    legumes_top=legumes_top.head(10)

    fig_protein_seafood = go.Figure(go.Funnelarea(values=legumes_top['protcnt'].values, text=legumes_top['name'],title = { "text": "Legumes with high protein percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_protein_seafood.update_layout(height=600, width=700)

    st.plotly_chart(fig_protein_seafood)


def demographic_dimensional_page():
    st.title("3d relation")

    trace1 = go.Scatter3d(
    x=df_demographics['category'].values,
    y=df_demographics['name'].values,
    z=df_demographics['fasat'].values,
    text=df_demographics['name'].values,
    mode='markers',
    marker=dict(
        sizemode='diameter',
         sizeref=750,
        color = df_demographics['fasat'].values,
        colorscale = 'Portland',
        colorbar = dict(title = 'Total Fat (% Daily Value)'),
        line=dict(color='rgb(255, 255, 255)')
        )
    )
    data=[trace1]
    layout=dict(height=800, width=800, title='3D Scatter Plot of Fatty foods (% Daily Value)')
    fig=dict(data=data, layout=layout)

    st.plotly_chart(fig)

def demographic_foodgroup_page():
    
    sns.set_style("whitegrid")
    plt.figure(figsize=(19,10))
    #plt.figure()

    ax = sns.boxenplot(x="category", y='fasat', data=df_demographics, color='#eeeeee', palette="tab10")

    # Add transparency to colors
    for patch in ax.artists:
        r, g, b, a = patch.get_facecolor()
        patch.set_facecolor((r, g, b, .9))
        
    #ax = sns.stripplot(x='Category', y='Cholesterol (% Daily Value)', data=menu, color="orange", jitter=0.5, size=5,alpha=0.15)
    #
    plt.title("Total Calorie Content \n", loc="center",size=32,color='#be0c0c',alpha=0.6)
    plt.xlabel('Category',color='#34495E',fontsize=20) 
    plt.ylabel('Total Fat (% Daily Value)',color='#34495E',fontsize=20)
    plt.xticks(size=16,color='#008abc',rotation=90, wrap=True)  
    plt.yticks(size=15,color='#006600')

    #plt.text(2.5, 1, 'Courtesy: https://seaborn.pydata.org/examples/grouped_boxplot.html', fontsize=13,alpha=0.2)
    #plt.ylim(0,200)
    #plt.legend(loc="upper right",fontsize=14,ncol=5,title='Category',title_fontsize=22,framealpha=0.99)
    
    st.pyplot(plt,dpi=100)


def disease_demographics():
    # Register your pages
    pages = {
        "1. Dataset Pruning and Exploration": test_page,
        "2. Correlation between presence of Nutrients":test_page,
        "3. Analysis of Nutrient Content":test_page,
        "4. Categorized distribution of Nutrients":test_page,
        "5. 3D relation":test_page,
        "6. foodgroup":test_page
    }


    st.title("Navigate through demographics 🧭")

    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    # Display the selected page
    pages[page]()

def test_page():
    st.title("title test")




#https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    main()





#st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>description</h6>",unsafe_allow_html=True)
#st.markdown("")


