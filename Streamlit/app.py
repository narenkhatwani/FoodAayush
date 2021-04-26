#import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
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
df_demographics_nonveg= pd.read_csv("resources/assets_modified/02cat.csv")

#drop row/column if all values there are NA
df_demographics.dropna()


#the main function that is called first and foremost with the navigation options in the sidebar
def main():
    # Register your pages
    pages = {
        "About": about_page,
        "Ingredient Information": page_first,
        "IFCT Demographics": demographic_main,
        "Medical Condition Demographics":disease_demographics,
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

    #github repository link to the whole project in the sidebar
    st.sidebar.subheader("Check out our [Github Repository](https://github.com/narenkhatwani/FoodAayush)")


#function for the about page
def about_page():
    st.markdown("<h1 style='text-align: center;'>Food Aayush 🍲 🩺</h1>", unsafe_allow_html=True)
    
    st.subheader("About FoodAayush 🤔")

    #all the necessary descriptions
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial, sans-serif;line-height: 1.5;'>Food is an essential parameter that plays an important role in the survival of humans. It also plays a major part in depicting a country’s culture. Healthy, nutritious, and high-quality food results in not only a better lifestyle but also develops a person’s immunity and health. Likewise, the consumption of low-quality food which might be deprived of nutritional value impacts a person’s health negatively and makes them susceptible to all types of diseases. In India, there is a persistent complaint, in any civic body-related food section, about the quality of meals available. Likewise, the quality of the oil is also an important factor while cooking any meal. Therefore, the Quality of oil used in frying the food to affect its taste must be monitored too. Its continuous exposure to relatively high temperatures results in degradation of its quality. The purpose of this study is to build an application for the detection of the quality of food and also to detect repeated frying on cooking oils based on the visual properties of the oils. Classification of food items is done on the basis of time left for consumption, edibility, quality, color, and rancidity. The food items are further classified as stale or usable using artificial intelligence algorithms based on the images acquired through a Cell Phone’s camera.</h6>", unsafe_allow_html=True)
    st.markdown("")
    st.subheader("Activity Diagram ♺")
    st.image('resources/about_process_diagram/1.png')

    st.markdown("")
    st.subheader("Classification of food items and cooking oils based on quality")
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>Food becomes stale if there is excessive exposure to environmental factors such as heat and humidity. Similarly, if a cooking oil sample is exposed to heat, or is used in cooking repeatedly, it will become rancid. The second part of our application is the classification of food items based on their freshness and oils based on their rancidity. A classification model is developed for classifying food items into various freshness levels based on their visual properties. For oils, the classification is done on the basis of the visual properties as well as the pH value of the oil sample. The pH value is recorded using a pH sensor integrated with the application. These features are included in our mobile application which is developed using the Flutter toolkit.</h6>", unsafe_allow_html=True)
    
    #using the layout customization features of streamlit for expanders - to show sources of data which are collapsible in nature
    st.title("For Data Sources ")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        '[Click to view the accesible page of the below source](http://www.ifct2017.com/frame.php?page=home)'
        '[Click to view the credibility of the below source](https://www.icrisat.org/india-releases-the-worlds-most-advanced-and-comprehensive-analytical-data-base-of-national-food-nutritional-composition/)'
        '---------------------------------------------------------------'
        "Indian Food Composition Tables 2017"
        "T. Longvah, R. Ananthan, K. Bhaskarachary and K. Venkaiah"

        "Copyright  © 2017 by National Institute of Nutrition"
        "Indian Council of Medical Research"
        "Department of Health Research Ministry of Health and Family Welfare, Government of India"
        "Jamai Osmania (PO), Hyderabad – 500 007"
        "Telangana, India Phone: +91 40 27197334, Fax: +91 40 27000339, Email: nin@ap.nic.in"
        "------------------------------------------------------------------------------------------"
        "Columns abbreviation and units (used in the demographics and analysis):"
        "water - Moisture [g]"
        "protcnt - Protein [g]"
        "ash - Ash [g]"
        "fatce - Total Fat [g]"
        "fibtg - Total fibre[g]"
        "fibins - Insoluble fibre[g]"
        "fibsol - Soluble [g]"
        "choavldf - Carbohydrate [g]"
        "enerc - Energy [kJ]"
        "cholc - Cholesterol [mg]"
        "fasat - Total Saturated Fatty Acids (TSFA) [mg]"
        "fams - Total Mono Unsaturated Fatty Acids (TMUFA) [mg]"
        "fapu - Total Poly Unsaturated Fatty Acids (TPUFA) [mg]"
        "starch - Total Starch [g]"
        "frus - Fructose [g]"
        "glus - Glucose [g]"
        "sucs - Sucrose [g]"
        "mals - Maltose [g]"
        "fsugar - Total Free Sugars [g]"
        "lactose - Lactose content (g/100) [g]"
        "fe - Iron (Fe) [mg]"
        "ca - Calcium (Ca) [mg]"
        "zn - Zinc (Zn) [mg]"
        "k - Potassium (K) [mg]"

    #this function works on streamlit==0.71.0
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
    

#first page function
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

    #displaying the corresponding values to the above parameters
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Water- {count_water}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Protein- {count_protein}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Ash- {count_ash}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Fat- {count_fat}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Total Fibre- {count_fibretotal}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Insoluble Fibre- {count_fibreinsoluble}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Soluble Fibre- {count_fibresoluble}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Carbohydrates- {count_carbohydrate}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Energy- {count_energy}kJ</span>", unsafe_allow_html=True)
    

    #ifct database information
    st.subheader("Some Information about the data source 📊")
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>The above data is taken from the dataset “Indian Food Composition Tables, 2017”, of the National Institute of Nutrition. The approach taken for creation of this dataset was to sample the key foods from all over India which contribute to the nutrient intake of 75% of the population. The consumption data and nutrient composition for the various foods is found and the foods have been ranked according to their contribution to the diet in terms of nutrients.</h6>", unsafe_allow_html=True)
    st.markdown("")
    
    #to print a small iframe of the csv file using the checkbox
    raw_data=st.checkbox('See Raw Data')
    if raw_data: 
        st.write(data)

    
def page_second():

    #sidebar title
    st.title("Search for a Recipe 😋")
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>All recipes require a variety of ingredients, such as vegetables, flour, spices and milk products. Here, you can search the possible dishes with any desired combination of ingredients. You can also view the calories in the dish and the cuisine. Please enter a minimum of two ingredients to search for dishes.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Dataset Preview 📋</span>", unsafe_allow_html=True)
    data2

    #default value is NA for the choice
    all_ingredients1 = ["NA"]
    gg = data2.loc[:, data2.columns != 'Name of Dish'].values.tolist()

    #printed a list first in streamlit of the unique values in the particular choice and then copied it to give the options here
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

    #printed a list first in streamlit of the unique values in the particular choice and then copied it to give the options here
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


    #printed a list first in streamlit of the unique values in the particular choice and then copied it to give the options here
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

    #printed a list first in streamlit of the unique values in the particular choice and then copied it to give the options here
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

    #take user input to select the dish from the name column (used unique function for non repetition of values)
    dish_name = st.selectbox("Search your dish here:", data2["Name of Dish"].unique())


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Filter Data Results are :</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>You selected- {dish_name}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Analysis for your selection is as follows-</span>", unsafe_allow_html=True)

    #counts of various nutritional contents of a food item
    count_calories = data2.loc[(data2["Name of Dish"] == dish_name) , 'Calories'].iloc[0]
    cuisine = data2.loc[(data2["Name of Dish"] == dish_name) , 'Cuisine'].iloc[0]
    
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Calorie Count - {count_calories} kCal</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 22px;font-weight: bold;'>Cuisine - {cuisine}</span>", unsafe_allow_html=True)
  
#clorie calculator function
def page_three():
    st.title("Calorie Calculator 🍲 🧮")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Nutrients are classified into two categories, macronutrients and micronutrients. Macronutrients are those nutrients which are required in large quantities, and include carbohydrates, proteins, fats and water. Micronutrients are those which are required in relatively small quantities, and include vitamins and minerals. Adequate amounts of these nutrients are required to maintain good health. The adequate amounts vary from person to person, and also depend on the person’s daily calorie consumption. Moreover, the ideal calorie consumption for a person also depends on various factors, including gender. Here, you can find your ideal consumption of various nutrients depending on your daily calorie consumption, and can also find your ideal daily calorie consumption based on your gender.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Add your total daily intake of calories</span>", unsafe_allow_html=True)

    #slider for user input
    x = st.slider('(in terms of Calories)',0,3000)

    #the generalised ideal percentages considered from various data sources
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

    #display selected choice
    st.markdown(f"<span style='color: black;font-size: 20px;font-weight: bold;'>You selected: {gender}</span>", unsafe_allow_html=True)

    #if else use for all the possible variations - hard coded because choice are very few 
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
    
    st.subheader("To view the sources of this data:")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "1: [What should my daily intake of calories be?](https://www.nhs.uk/common-health-questions/food-and-diet/what-should-my-daily-intake-of-calories-be/#:~:text=Generally%2C%20the%20recommended%20daily%20calorie,women%20and%202%2C500%20for%20men.)"
        "2: [How Much Water Should You Drink Per Day?](https://www.healthline.com/nutrition/how-much-water-should-you-drink-per-day#how-much-you-need)"
        
        

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
  
    st.subheader("To view the sources of this data:")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "1: [Source 1](https://www.factchecker.in/punjab-tamil-nadu-haryana-have-highest-burden-of-heart-disease-in-india/)"
        "2: [Source 2](https://traveltriangle.com/blog/assam-food/)"
        "3: [Source 3](https://www.holidify.com/pages/food-of-meghalaya-1672.html)"
        "4: [Source 4](https://www.holidify.com/pages/food-of-tripura-1692.html)"
        "5: [Source 5](https://timesofindia.indiatimes.com/life-style/food-news/7-dishes-from-nagaland-that-are-worth-trying/photostory/78618476.cms?picid=78618690)"
        "6: [Source 6](https://food.ndtv.com/food-drinks/7-delectable-mizoram-foods-you-should-definitely-try-once-1813228)"
        "7: [Source 7](https://pickyourtrail.com/blog/dishes-in-arunachal-pradesh/)"
        "8: [Source 8](https://www.holidify.com/pages/food-of-manipur-1659.html)"
        "9: [Source 9](https://www.tarladalal.com/calories-for-vada-pav-2811#:~:text=One%20serving%20of%20Vada%20Pav%20gives%20197%20calories.,adult%20diet%20of%202%2C000%20calories.)"
        "10: [Source 10](https://m.tarladalal.com/calories-for-dabeli--mumbai-roadside-recipes--33401#:~:text=One%20Dabeli%20gives%20199%20calories,adult%20diet%20of%202%2C000%20calories.)"
        "11: [Source 11](https://recipes.timesofindia.com/recipes/babru/rs71608958.cms)"
        "12: [Source 12](https://www.tarladalal.com/calories-for-puttu-kerala-homemade-rice-puttu-for-breakfast-41331)"
        "13: [Source 13](https://www.yowangdu.com/tibetan-food/calories-in-momos-steamed.html)"
        "14: [Source 14](https://www.myweekendkitchen.in/spicy-mashed-potato-indian/)"
        "15: [Source 15](https://www.latimes.com/food/la-fo-watchrec2nov01-story.html#:~:text=Each%20samosa%3A%20184%20calories%3B%205,cholesterol%3B%20134%20mg.)"
        "16: [Source 16](https://www.vahrehvah.com/chenna-jhili)"
        "17: [Source 17](https://m.tarladalal.com/calories-for-malai-kofta-2174#:~:text=How%20many%20calories%20does%20one,fat%20which%20is%20220%20calories.)"
        "18: [Source 18](https://recipes.timesofindia.com/recipes/arsa/rs58975118.cms)"
        "19: [Source 19](https://www.myfitnesspal.com/food/calories/kajjikayalu-87321333)"
        "20: [Source 20](https://www.fitbit.com/foods/Mutton+Roasted/19687)"
				
			

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

    st.subheader("To view the sources of this data:")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "1: [Source 1](https://www.foreversunday.org/food-combinations-ayurveda/)"
        "2: [Source 2](https://parenting.firstcry.com/articles/magazine-food-combinations-you-should-strictly-avoid-eating/)"
        "3: [Source 3](https://parenting.firstcry.com/articles/magazine-food-combinations-you-should-strictly-avoid-eating/)"
        "4: [Source 4](https://www.scoopwhoop.com/toxic-food-combinations/)"

def demographic_main():
    # Register your pages
    pages = {
        "1. Dataset Pruning and Exploration": demographic_pruning_page,
        "2. Correlation between presence of Nutrients":demographic_correlation_page,
        "3. Analysis of Nutrient Content":demographic_nutrient_analysis_page,
        "4. Categorized distribution of Nutrients":demographic_categorized_page,
        "5. Evaluation of Non Vegetarian Food":demographic_dimensional_page,
        "6. Variation in nutrient content":demographic_foodgroup_page
    }


    st.title("Navigate through demographics 🧭 📊")

    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    # Display the selected page
    pages[page]()

def demographic_pruning_page():
    st.title("Dataset Pruning and Exploration 🧹 🔍")

    #description of the demographics page
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Before performing any analysis on the data, it is necessary to prune the dataset. This is mainly done to remove any discrepancies in the data, which may cause a hindrance to the data analysis.The following are some ways in which the dataset can be pruned to make it fit for analysis.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #display the data frame with checkbox
    raw_data=st.checkbox('See Raw Data')
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The following are some of the steps undertaken by us in order to make the dataset fit for analysis.</h6>",unsafe_allow_html=True)

    if raw_data: #checkbox true or not 
        st.write(df_demographics.head(10))

    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>1. Checking the data types 📋</span>", unsafe_allow_html=True)
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>In this step, we check the data types of all the parameters before moving ahead with the analysis. This is done to ensure that the analysis is done smoothly without the hassle of getting any data type errors during visualization.</h6>",unsafe_allow_html=True)
    
    st.markdown("")

    #print data types of columns
    st.write(df_demographics.dtypes)

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'> Therefore, all our data is in desired datatypes.</h6>",unsafe_allow_html=True)

    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>2. Quick last checks on data quality </span>", unsafe_allow_html=True)
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>To obtain accurate results, it is necessary to ensure that the dataset is complete and of good quality.</h6>",unsafe_allow_html=True)
    
    st.subheader("Null Value Check #️⃣")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The next step is checking the presence of null values in the dataset. This is important to avoid obtaining biased results due to missing data. The dataset is checked column-wise for null values, and no null values are found.</h6>",unsafe_allow_html=True)
    
    st.markdown("")
    
    #null values check
    st.write(df_demographics.isnull().any())
    
    st.subheader("Descriptions of all the parameters")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Now, to analyze the parameters (columns) in the dataset, which are the quantities of various nutrients present in the food items, some mathematical operations have been performed on the columns. The count, the mean and standard deviation, the minimum and maximum of the values in each column are calculated as shown below.</h6>",unsafe_allow_html=True)

    st.markdown("")

    #values 
    st.write(df_demographics.describe())
    
    #expander feature of streamlit layout functionality for data sources - collapsible expander
    st.subheader("For the abbreviation and units used in the upcoming features")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "Columns abbreviation and units (used in the demographics and analysis):"
        "water - Moisture [g]"
        "protcnt - Protein [g]"
        "ash - Ash [g]"
        "fatce - Total Fat [g]"
        "fibtg - Total fibre[g]"
        "fibins - Insoluble fibre[g]"
        "fibsol - Soluble [g]"
        "choavldf - Carbohydrate [g]"
        "enerc - Energy [kJ]"
        "cholc - Cholesterol [mg]"
        "fasat - Total Saturated Fatty Acids (TSFA) [mg]"
        "fams - Total Mono Unsaturated Fatty Acids (TMUFA) [mg]"
        "fapu - Total Poly Unsaturated Fatty Acids (TPUFA) [mg]"
        "starch - Total Starch [g]"
        "frus - Fructose [g]"
        "glus - Glucose [g]"
        "sucs - Sucrose [g]"
        "mals - Maltose [g]"
        "fsugar - Total Free Sugars [g]"
        "lactose - Lactose content (g/100) [g]"
        "fe - Iron (Fe) [mg]"
        "ca - Calcium (Ca) [mg]"
        "zn - Zinc (Zn) [mg]"
        "k - Potassium (K) [mg]"



def demographic_correlation_page():
    st.title("Correlation between presence of nutrients 🥒 🔛 🥔 ")
    
    #description of the demographics page
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>There is a relationship between the amounts of different nutrients present in food items. Every food item is not rich in all nutrients. Certain food items are richer in proteins, while others may be abundant in carbohydrates and so on. Here, we show the relationship between different nutrients in the food items present in the dataset.</h6>",unsafe_allow_html=True)
    st.markdown("")


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>1. Variation of Protein Content with Carbohydrate Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Protein (grams) & Carbohydrates (grams)</span>", unsafe_allow_html=True)

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The graph shown below is the plot of protein v/s carbohydrates. It shows the trend between the amount of protein and the amount of carbohydrates in the food items present in the dataset.</h6>",unsafe_allow_html=True)
    

    #kde plots are used here - A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analagous to a histogram
    #1st plot
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.0, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['choavldf'],df_demographics['protcnt'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Carbohydrates (g)")

    #kde plot title Y axis
    plt.ylabel("Protein (g)")

    #kde plot title    
    plt.title("Carbohydrates and Protein")

    st.pyplot(plt,dpi=100)

    st.markdown(f"<span style='color: #367588;font-size: 18px;font-weight: bold;'>Inference:</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Foods high in carbohydrates are usually low in protein and vice versa. We can see an inverse variation between carbohydrates and protein in the above graph</h6>",unsafe_allow_html=True)
    #kde plot invoke  

    #2nd plot

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>2. Variation of Carbohydrate Content with Fat Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Carbohydrates (grams) and Fat (grams)</span>", unsafe_allow_html=True)

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The graph shown below is the plot of carbohydrates v/s fat. It shows the trend between the amount of carbohydrates and the amount of fat in the food items present in the dataset.</h6>",unsafe_allow_html=True)
    
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.25, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['fatce'],df_demographics['choavldf'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Fats (g)")

    #kde plot title Y axis
    plt.ylabel("Carbohydrates (g)")

    #kde plot title    
    plt.title("Fats and Carbohydrates")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  
    st.markdown(f"<span style='color: #367588;font-size: 18px;font-weight: bold;'>Inference:</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>A food item would either be high in carbohydrates or high in fat content. Thus, we can see from the graph that as the carbohydrate content in a food item increases, the fat content decreases. Having a high fat, low carbohydrate diet is found to be healthier, as it is better for blood glucose control and weight loss, as compared to a low fat, high carbohydrate diet.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #3rd plot

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>3. Variation of Fibre Content with Carbohydrate Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Fiber (grams) & Carbohydrates (grams)</span>", unsafe_allow_html=True)

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The graph shown below is the plot of fiber v/s carbohydrates. It shows the trend between the amount of fiber and the amount of carbohydrates in the food items present in the dataset.</h6>",unsafe_allow_html=True)
    
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.33, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['choavldf'],df_demographics['fibtg'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Carbohydrates (g)")

    #kde plot title Y axis
    plt.ylabel("Fiber (g)")

    #kde plot title    
    plt.title("Carbohydrates and Fiber")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  
    st.markdown(f"<span style='color: #367588;font-size: 18px;font-weight: bold;'>Inference:</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Fiber is a type of carbohydrate that the body cannot digest. It is of two types, soluble and insoluble. Soluble fiber dissolves in water, and it is useful for lowering blood glucose and cholesterol levels. Insoluble fiber does not dissolve in water. It helps in clearing the intestines and prevents constipation. We can see from the above graph that the fiber content is increasing along with the total carbohydrate content in the food item. The net carbohydrate content is the total carbohydrate content minus the fiber content.</h6>",unsafe_allow_html=True)
    
    #4th plot

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>4. Variation of Fat Content with Fibre Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Fat (grams) & Fiber (grams)</span>", unsafe_allow_html=True)

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The graph shown below is the plot of fat v/s fiber. It shows the trend between the amount of fat and the amount of fiber in the food items present in the dataset.</h6>",unsafe_allow_html=True)
    
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.45, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['fibtg'],df_demographics['fatce'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Fiber (g)")

    #kde plot title Y axis
    plt.ylabel("Fat (g)")

    #kde plot title    
    plt.title("Fiber and Fat")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  
    st.markdown(f"<span style='color: #367588;font-size: 18px;font-weight: bold;'>Inference:</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Foods high in fiber are generally low in fat. We can observe a decrease in fat content as the amount of fibre increases.</h6>",unsafe_allow_html=True)
    
    #5th plot

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>5. Variation of Saturated Fat Content with Total Fat Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Saturated Fat (milligrams) & Total Fat (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>There are four types of fats: saturated fats, trans fats, monounsaturated fats, and polyunsaturated fats. The graph shown below is the plot of saturated fat v/s total fat. It shows the trend between the amount of saturated fat and the total fat content in the food items present in the dataset. </h6>",unsafe_allow_html=True)
    
    st.markdown("")

    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.56, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['fatce'],df_demographics['fasat'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Total Fat (g)")

    #kde plot title Y axis
    plt.ylabel("Saturated Fat (mg)")

    #kde plot title    
    plt.title("Total Fat and Saturated Fat")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  

    st.markdown(f"<span style='color: #367588;font-size: 18px;font-weight: bold;'>Inference:</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Saturated fat is 'bad' fat, as it causes obesity and increases the levels of LDL cholesterol in the blood, thus increasing the risk of cardiovascular disease. The consumption of saturated fats should therefore be kept as low as possible. Unsaturated fats, on the other hand, help to reduce inflammation and also lower LDL cholesterol. Also, they help to build healthy cell membranes in the body. Thus, unsaturated fats are healthy.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #6th plot

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>6. Variation of Energy with Carbohydrate Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Energy (Kilo Joules) & Total Carbohydrates (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The graph shown below is the plot of energy v/s carbohydrates. It shows the trend between the total energy (in kJ)  and the amount of carbohydrates in the food items present in the dataset. </h6>",unsafe_allow_html=True)
    
    #kde plot
    fig, ax = plt.subplots(figsize=(12,3))

    cmap = sns.cubehelix_palette(start=0.68, light=1, as_cmap=True)

    sns.kdeplot(df_demographics['choavldf'],df_demographics['enerc'],cmap=cmap,shade=True)

    #kde plot title X axis
    plt.xlabel("Carbohydrates (g)")

    #kde plot title Y axis
    plt.ylabel("Energy (kJ)")

    #kde plot title    
    plt.title("Carbohydrates and Energy")

    st.pyplot(plt,dpi=100)
    #kde plot invoke  

    st.markdown(f"<span style='color: #367588;font-size: 18px;font-weight: bold;'>Inference:</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The primary function of carbohydrates is to provide energy to the body. We can infer from the graph that the amount of energy in the food items increases with the carbohydrate content.</h6>",unsafe_allow_html=True)


def demographic_nutrient_analysis_page():
    st.title("Analysis of Nutrient content 🧑‍🔬")
    
    #description of the demographics page
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Certain foods have higher proportions of specific nutrients than others. The most notable example is that meat, fish, and eggs contain higher amounts of protein than plant-based foods. Here, the data is analyzed to find the foods with the highest amounts of various nutrients, including proteins, carbohydrates, and fats. This is explained with the help of graphical representations.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Analysis of Protein Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Protein (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>First, we have found the foods having the highest amounts of protein and have represented the amounts of protein in these foods graphically.</h6>",unsafe_allow_html=True)
    st.markdown("")
    #Based on categories
    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #protein

    prot= df_demographics[df_demographics['category'].isin(categories)]

    protein_rich= prot.sort_values(by='protcnt', ascending= False)
    
    top_20=protein_rich.head(20)
    
    fig = px.bar(top_20, x='name', y='protcnt', color='protcnt')
    fig.update_layout(title='Top 20 Protein Rich Foods', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)

    #fat
    
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Analysis of Fat Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Fat (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Next, we have found the foods having the highest amounts of fat. We can see that the highest amounts of fat are in mostly in nuts and seeds, closely followed by eggs and red meat.</h6>",unsafe_allow_html=True)
    st.markdown("")

    fat= df_demographics[df_demographics['category'].isin(categories)]

    fat_rich= fat.sort_values(by='fatce', ascending= False)
    
    top_20_fat=fat_rich.head(20)
    
    fig1 = px.bar(top_20_fat, x='name', y='fatce', color='fatce')
    fig1.update_layout(title='Top 20 Foods High in Fat', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig1)
    
    #carbohydrates

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Analysis of Carbohydrate Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Carbohydrates (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Here, the foods highest in carbohydrate content are displayed. Jaggery, which is a form of cane sugar, has the highest amount of carbohydrates among the food items present in the dataset. Most of the high-carbohydrate foods include grains, some fruits such as dates, raisins, and apricot, and some nuts such as areca nut.</h6>",unsafe_allow_html=True)
    
    st.markdown("")
    
    
    carbs= df_demographics[df_demographics['category'].isin(categories)]

    carbs_rich= carbs.sort_values(by='choavldf', ascending= False)
    
    top_20_carbs=carbs_rich.head(20)
    
    fig1 = px.bar(top_20_carbs, x='name', y='choavldf', color='choavldf')
    fig1.update_layout(title='Top 10 Foods High in Carbohydrates', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig1)


def demographic_categorized_page():
    st.title("Categorized distribution of Nutrients 🧮")
    
    #description of the demographics page
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Here, for each nutrient, the quantities of that nutrient present in each food item in the dataset are summed up to find that nutrient’s total quantity.  Then, the percentage of this total quantity present in each food category is found. These percentages are represented graphically in the form of a pie chart. This process is carried out for each nutrient. The pie charts for each nutrient are displayed below.</h6>",unsafe_allow_html=True)
    st.markdown("")
    
    

    #category wise statistics
    category_dist= df_demographics.groupby(['category']).sum()
    st.write(category_dist)

    st.markdown("")
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Visualization :</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>    The following pie charts show the distribution of the total quantity of each nutrient across the food categories present in the dataset.</h6>",unsafe_allow_html=True)

    fig = make_subplots(rows=3, cols=2,specs=[[{"type": "domain"},{"type": "domain"}],[{"type": "domain"},{"type": "domain"}],[{"type": "domain"},{"type": "domain"}]])
    
    fig.add_trace(go.Pie(values=category_dist['enerc'].values, title='CALORIES', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=1, col=1)
    
    fig.add_trace(go.Pie(values=category_dist['fatce'].values,title='FAT', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=3, col=1)

    fig.add_trace(go.Pie(values=category_dist['protcnt'].values,title='PROTEIN', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=1, col=2)

    fig.add_trace(go.Pie(values=category_dist['fibtg'].values,title='FIBER', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=2, col=2)

    
    fig.add_trace(go.Pie(values=category_dist['fasat'].values,title='SATURATED FAT', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=3, col=2)

    fig.add_trace(go.Pie(values=category_dist['choavldf'].values,title='CARBOHYDRATES', labels=category_dist.index,marker=dict(colors=['#100b','#f00560'], line=dict(color='#FFFFFF', width=2.5))),row=2, col=1)
    
    fig.update_layout(title_text="Category wise distribution of all metrics",height=1200, width=800)
    
    st.plotly_chart(fig)

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Top 10 Protein Rich Seafood Items</span>", unsafe_allow_html=True)

    #high protein seafood items 
    seafood= df_demographics[df_demographics['category'].isin(['Seafood'])]

    seafood_top=seafood.sort_values(by='protcnt', ascending= False)
    
    seafood_top=seafood_top.head(10)

    fig_protein_seafood = go.Figure(go.Funnelarea(values=seafood_top['protcnt'].values, text=seafood_top['name'],title = { "text": "Seafood with high protein percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_protein_seafood.update_layout(height=620, width=700)

    st.plotly_chart(fig_protein_seafood)

    #description
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Seafood and meat are sources of high protein. Among these, seafood is an excellent option, as it also contains higher amounts of omega-3 fatty acids, which is a type of unsaturated fat that is beneficial for the heart. Seafood is healthier than red meat, as red meat has much higher amounts of saturated fat. The seafood items having the highest protein content have been displayed here.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #title 2nd pyramid graph blue text
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Alternatives to seafood for Vegetarians</span>", unsafe_allow_html=True)

    #high protein legumes (for vegetarians)
    legumes= df_demographics[df_demographics['category'].isin(['Legumes'])]

    legumes_top=legumes.sort_values(by='protcnt', ascending= False)
    
    legumes_top=legumes_top.head(10)

    fig_protein_seafood = go.Figure(go.Funnelarea(values=legumes_top['protcnt'].values, text=legumes_top['name'],title = { "text": "Legumes with high protein percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_protein_seafood.update_layout(height=620, width=700)

    st.plotly_chart(fig_protein_seafood)

    #description
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Vegetarians often have protein deficiencies as they do not consume animal protein. Therefore, they must consume vegetarian alternatives to incorporate the necessary amount of protein in their diet. Among vegetarian foods, legumes such as soyabean, gram, and lentils are very good protein sources. The legumes having highest protein content are shown below.</h6>",unsafe_allow_html=True)
    st.title("")


    
def demographic_dimensional_page():
    st.title("Evaluation of Non Vegetarian Food 🥚 🦀")
    
    #subtitle
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Protein and Cholesterol levels</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Cholesterol (grams) and Protein (grams)</span>", unsafe_allow_html=True)
    
    #description
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Non-vegetarian foods are excellent protein sources. However, foods such as red meat are also high in cholesterol. The nutritional value of non-vegetarian foods (including eggs) is evaluated here based on their protein and cholesterol levels. The cholesterol level should be low and the protein content should be high.</h6>",unsafe_allow_html=True)


    trace1 = go.Scatter3d(
    x=(df_demographics_nonveg['category']).values,
    y=df_demographics_nonveg['protcnt'].values,
    z=df_demographics_nonveg['cholc'].values,
    text=df_demographics_nonveg['name'].values,
    mode='markers',
    marker=dict(
        sizemode='diameter',
         sizeref=750,
        color = df_demographics_nonveg['fasat'].values,
        colorscale = 'Portland',
        colorbar = dict(title = 'Cholesterol (% Daily Value)'),
        line=dict(color='rgb(255, 255, 255)')
        )
    )
    data=[trace1]
    layout=dict(scene = dict(xaxis_title='',yaxis_title='Protein (g)',zaxis_title='Cholesterol (g)'),height=800, width=800, title='3D Scatter Plot of Protein and Cholesterol Content in Non-vegetarian Foods')
    fig=dict(data=data, layout=layout) 

    st.plotly_chart(fig)

def demographic_foodgroup_page():
    st.title("Variation in nutrient content 📈 📉")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Fat (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Here, we have shown the variation in the percentage of fat in all food items present in each category with the help of boxplots. Each boxplot represents one food category. The percentage of fat is shown on the y-axis. The food categories are shown on the x-axis, and the width of the boxplot at a particular y-coordinate represents the number of food items in that particular food category that have that particular percentage of fat. We can see from the graph that the maximum variation in the percentage of fat is in the nuts category.</h6>",unsafe_allow_html=True)
    st.markdown("")

    sns.set_style("whitegrid")
    plt.figure(figsize=(19,10))
    #plt.figure()

    ax = sns.boxenplot(x="category", y='fatce', data=df_demographics, color='#eeeeee', palette="tab10")

    # Add transparency to colors
    for patch in ax.artists:
        r, g, b, a = patch.get_facecolor()
        patch.set_facecolor((r, g, b, .9))
        
    #ax = sns.stripplot(x='Category', y='Cholesterol (% Daily Value)', data=menu, color="orange", jitter=0.5, size=5,alpha=0.15)
    
    plt.title("Total Fat Content \n", loc="center",size=32,color='#be0c0c',alpha=0.6)
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
        "1. Food Suggestions for Diabetic Patients": diabetes_page,
        "2. Food Suggestions for Lactose Intolerance":lactose_page,
        "3. Food Suggestions for Anaemia Patients":anaemia_page,
        "4. Food Suggestions for patients suffering from Kidney Stones":kidneystones_page,
        "5. Food Suggestions for patients suffering from Gallbladder Stones":gallstones_page
    }

    #title 
    st.title("Navigate through demographics 🧭 ")

    #Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    #Display the selected page
    pages[page]()

def diabetes_page():
    st.title("Diabetes")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Diabetes is a condition in which the glucose level in blood (also called as blood sugar level) is too high. The pancreas produces a hormone called insulin which helps in the generation of energy from glucose. When the insulin produced is not sufficient to generate energy from glucose, the glucose stays in blood, which ultimately leads to diabetes. Diabetes is of two types, type 1 and type 2 diabetes. While the cause of type 1 diabetes is unknown, obesity and excessive consumption of sugar is one of the causes of type 2 diabetes. Diabetic patients need to control their sugar consumption, so as not to increase the glucose level in the blood. Also, since carbohydrates are broken down into glucose, they increase the glucose level in blood. Therefore, carbohydrate consumption also needs to be controlled. Carbohydrates also include fiber, but fiber does not raise blood sugar levels as it is expelled from the body undigested.</h6>",unsafe_allow_html=True)
    st.markdown("")

    glus_largest=df_demographics.groupby('category')['glus'].nlargest(5)
    st.write(glus_largest)

    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #diabetes

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Analysis of Glucose Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Glucose (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Here, the food items in the dataset which are highest in glucose are displayed. Raisins and tamarind are at the top of the list. People having diabetes should consume these food items in very controlled quantities, in order to avoid raising their blood sugar level.</h6>",unsafe_allow_html=True)
    
    st.markdown("")
    
    carbs= df_demographics[df_demographics['category'].isin(categories)]

    carbs_rich= carbs.sort_values(by='glus', ascending= False)
    
    top_20_carbs=carbs_rich.head(20)
    
    fig1 = px.bar(top_20_carbs, x='name', y='glus', color='glus')
    fig1.update_layout(title='Top 20 Foods High in Glucose', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig1)
    
    st.subheader("To view the sources of this data:")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "1: [Types of Diabetes: Causes, Identification, and More](https://www.healthline.com/health/diabetes/types-of-diabetes)"
        

def lactose_page():
    st.title("Food Suggestions for Lactose Intolerant Patients")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Lactose is a sugar present in milk and dairy products. Lactose intolerance is a digestive problem which is caused due to low amounts of an enzyme called lactase. Lactase helps in digestion of lactose, and therefore when this enzyme is deficient, then lactose passes undigested through the intestines, possibly causing symptoms such as nausea, diarrhoea, and gas. People having lactose intolerance do not need to completely avoid dairy products, however, they can consume only upto 12 grams of lactose at a time safely.  </h6>",unsafe_allow_html=True)
    st.markdown("")
    
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Analysis of Lactose Content</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Lactose (grams)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The amounts of lactose in some common dairy products are displayed here with the help of a bar graph.</h6>",unsafe_allow_html=True)
    st.markdown("")
    #Based on categories
    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #lactose

    lact= df_demographics[df_demographics['category'].isin(categories)]

    lactose_rich= lact.sort_values(by='lactose', ascending= False)
    
    top_20=lactose_rich.head(4)
    
    fig = px.bar(top_20, x='lactose', y='name', color='lactose')
    fig.update_layout(title='Foods with Lactose Content', autosize=False,width=750, height=700,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)


    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>People with lactose intolerance should consume small amounts of milk or products at a time. Also, there are some dairy products that have low amounts of lactose. These include:</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Dairy products with less amount of lactose</span>", unsafe_allow_html=True)

    
    cols = st.beta_columns(2)
    
    
    cols[0].write(f"<h6 style='text-align: left;font-size:22px;font-weight: bold;line-height: 1.3;'>Food items</h6>",unsafe_allow_html=True)

    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Butter</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Ghee</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Parmesan Cheese</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Cheddar Cheese</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Swiss Cheese</h6>",unsafe_allow_html=True)    
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Heavy Cream</h6>",unsafe_allow_html=True)
    cols[0].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>Probiotic Yoghurt</h6>",unsafe_allow_html=True)

    cols[1].write(f"<h6 style='text-align: left;font-size:22px;font-weight: bold;line-height: 1.3;'>Lactose Content (per 100grams)</h6>",unsafe_allow_html=True)

    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0.688 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0.0029 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0.1 g</h6>",unsafe_allow_html=True)    
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>0.1 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>3 g</h6>",unsafe_allow_html=True)
    cols[1].write(f"<h6 style='text-align: left;font-size:120%;font-family:Arial,sans-serif;line-height: 1.5;'>5 g</h6>",unsafe_allow_html=True)

    st.write("")
    st.subheader("Data Source of the above given data")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        'The above values of lactose content have been obtained from the following sources:'
        '1. [Click to view the accesible page](https://www.dairy.com.au/dairy-matters/you-ask-we-answer/what-is-the-lactose-content-of-different-dairy-products)'
     
        '2. [Click to view the accesible page](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5471386/)'

    st.write("")
    st.title("Alternatives to compensate for other nutrients present in dairy products")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Milk products should not be completely avoided, as it can cause deficiencies of calcium and vitamin D. Calcium deficiency can cause easy occurrence of bone fractures, weak and brittle nails, and muscle cramps while deficiency of vitamin D can cause osteoporosis, increased risk of heart disease, muscle pain and hair loss. People having lactose intolerance should make sure that they consume enough calcium and Vitamin D from other foods that do not contain lactose.</h6>",unsafe_allow_html=True)
    st.markdown("")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Top Calcium Rich Food Items</span>", unsafe_allow_html=True)

    #high calcium items 
    calcium= df_demographics[df_demographics['category'].isin(['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Eggs', 'White Meat', 'Red Meat', 'Seafood'])]

    calcium_top=calcium.sort_values(by='ca', ascending= False)
    
    calcium_top=calcium_top.head(15)

    fig_calcium_food = go.Figure(go.Funnelarea(values=calcium_top['ca'].values, text=calcium_top['name'],title = { "text": "Food items with high Calcium percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_calcium_food.update_layout(height=800, width=700)

    st.plotly_chart(fig_calcium_food)

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Top Foods rich in Vitamin D</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>There are five forms of vitamin D, of which vitamin D2 and D3 are the most common. Vitamin D2 is found in plant-based foods while vitamin D3 is found in animal-sourced foods.</h6>",unsafe_allow_html=True)
    st.markdown("")
    

    #d2
    st.markdown(f"<span style='color:#367588;font-size: 24px;font-weight: bold;'>Top Foods rich in Vitamin D2</span>", unsafe_allow_html=True)

    vitd2= df_demographics[df_demographics['category'].isin(['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar'])]

    vitd2_top=vitd2.sort_values(by='ergcal', ascending= False)
    
    vitd2_top=vitd2_top.head(15)

    fig_vitd2_food = go.Figure(go.Funnelarea(values=vitd2_top['ergcal'].values, text=vitd2_top['name'],title = { "text": "Food items with high Vitamin D2 percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_vitd2_food.update_layout(height=800, width=700)

    st.plotly_chart(fig_vitd2_food)

    #d3
    st.markdown(f"<span style='color: #367588;font-size: 24px;font-weight: bold;'>Top Foods rich in Vitamin D3</span>", unsafe_allow_html=True)

    vitd3= df_demographics[df_demographics['category'].isin(['Eggs', 'White Meat', 'Red Meat', 'Seafood'])]

    vitd3_top=vitd3.sort_values(by='chocal', ascending= False)
    
    vitd3_top=vitd3_top.head(15)

    fig_vitd3_food = go.Figure(go.Funnelarea(values=vitd3_top['chocal'].values, text=vitd3_top['name'],title = { "text": "Food items with high Vitamin D3 percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_vitd3_food.update_layout(height=800, width=700)

    st.plotly_chart(fig_vitd3_food)

    st.subheader("To view the sources of this data:")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "1: [Everything You Need to Know About Lactose Intolerance](https://www.healthline.com/health/lactose-intolerance#TOC_TITLE_HDR_1)"
        "2: [Eating, Diet, & Nutrition for Lactose Intolerance](https://www.niddk.nih.gov/health-information/digestive-diseases/lactose-intolerance/eating-diet-nutrition)"
        "3: [Hypocalcemia (Calcium Deficiency Disease)](https://www.healthline.com/health/calcium-deficiency-disease#symptoms)"
        "4: [8 Signs and Symptoms of Vitamin D Deficiency](https://www.healthline.com/nutrition/vitamin-d-deficiency-symptoms)"
        "5: [Vitamin D Deficiency](https://www.webmd.com/diet/guide/vitamin-d-deficiency#1)"
                

def anaemia_page():
    st.title("Iron deficiency Anaemia")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Haemoglobin is the protein in the red blood cells that is responsible for carrying oxygen to the tissues. Anaemia occurs when the level of haemoglobin in the blood is low.  The symptoms of anaemia include headaches, fatigue, weakness, dizziness, shortness of breath, and various other symptoms. Iron is needed to make haemoglobin. Thus, when there is a deficiency of iron, it leads to low levels of haemoglobin in the blood, causing anaemia. It may be caused by low consumption of iron, internal bleeding, and inability to absorb iron. Also, it is especially common in women, due to pregnancy and blood loss during menstruation. It is therefore necessary, especially for women, to consume foods that are rich in iron. The below pyramid shows the foods which have highest amounts of iron.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #iron deficiency
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Top Foods rich in Iron</span>", unsafe_allow_html=True)

    iron= df_demographics

    iron_top=iron.sort_values(by='fe', ascending= False)
    
    iron_top=iron_top.head(15)

    fig_iron_food = go.Figure(go.Funnelarea(values=iron_top['fe'].values, text=iron_top['name'],title = { "text": "Food items with high Vitamin D3 percentages"},marker = {"colors": ["deepskyblue", "lightsalmon", "tan", "teal", "silver","deepskyblue", "lightsalmon", "tan", "teal", "silver"],"line": {"color": ["wheat", "wheat", "blue", "wheat", "wheat","wheat", "wheat", "blue", "wheat", "wheat"]}}))

    fig_iron_food.update_layout(height=800, width=700)

    st.plotly_chart(fig_iron_food)

    st.subheader("To view the sources of this data:")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "1: [10 Signs and Symptoms of Iron Deficiency](https://www.healthline.com/nutrition/iron-deficiency-signs-symptoms)"
        

def kidneystones_page():
    st.title("Kidney Stones")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Kidney stones are caused due to accumulation of certain minerals in the urine. The most prominent cause of kidney stones is dehydration. Dehydration causes an increase in the concentrations of minerals in the urine. There are 4 types of kidney stones: calcium oxalate and calcium phosphate stones, uric acid stones, struvite stones, and cystine stones. Calcium oxalate stones are the most common.</h6>",unsafe_allow_html=True)

    st.header("Excessive consumption of the following nutrients can cause kidney stones:")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>1. Oxalate: Foods such as nuts, chocolate, tea, spinach are high in oxalate. Consuming these foods excessively can increase the amounts of oxalate in the urine and thereby increase the risk of calcium oxalate stones.</h6>",unsafe_allow_html=True)
    st.markdown("")
    

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>2. Sodium: High consumption of sodium can increase the formation of calcium in the urine. Therefore, to avoid kidney stones, the consumption of salt should be limited. Processed foods, canned foods, and fast food should be avoided as they are high in sodium. Baking soda should also be avoided.</h6>",unsafe_allow_html=True)
    st.markdown("")
    
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>3. Animal Protein: Excessive consumption of animal protein can increase the amounts of uric acid in the urine, thus increasing the risk of uric acid stones.</h6>",unsafe_allow_html=True)
    st.markdown("")

    #1st graph

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in oxalate (should not be consumed)</span>", unsafe_allow_html=True)

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Consumption of foods high in oxalate raises the urinary oxalate levels. This increases the risk of calcium oxalate stones. Therefore, consumption of oxalate-containing foods should be minimized. The below graph shows the foods in the dataset which have highest oxalate levels.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Oxalates (milligrams)</span>", unsafe_allow_html=True)
    
    #Based on categories
    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #oxalates

    oxalates= df_demographics[df_demographics['category'].isin(categories)]

    oxalates_rich= oxalates.sort_values(by='oxalt', ascending= False)
    
    top_20=oxalates_rich.head(10)
    
    fig1 = px.bar(top_20, x='name', y='oxalt', color='oxalt')
    fig1.update_layout(title='Foods having highest amounts of Oxalate', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig1)

    #2nd graph

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in citric acid (should be consumed)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>For prevention of kidney stones, one must stay adequately hydrated. Also, the consumption of citrus fruits should be increased. Citrus fruits have high amounts of citric acid, which is beneficial for people having kidney stones as it increases the amounts of citrate in the urine. Citrate binds with calcium oxalate and prevents the formation of crystals. The below graph shows the foods from the dataset having the highest amounts of citric acid.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Citric Acid (milligrams)</span>", unsafe_allow_html=True)
    #citric acid

    citric= df_demographics[df_demographics['category'].isin(categories)]

    citric_rich= citric.sort_values(by='citac', ascending= False)
    
    top_20=citric_rich.head(10)
    
    fig2 = px.bar(top_20, x='name', y='citac', color='citac')
    fig2.update_layout(title='Top Foods rich in Citric Acid', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig2)

    #3rd graph

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in calcium (should be consumed) </span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>It is a common misconception that calcium intake should be reduced in order to prevent kidney stones. However, calcium binds with oxalate in the intestine, and leads to the formation of calcium oxalate in the intestine, which in turn reduces the oxalate absorption and urinary oxalate excretion. Therefore, calcium intake should be kept sufficiently high. Following are some calcium-rich foods from the dataset.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Calcium (milligrams)</span>", unsafe_allow_html=True)
    #calcium

    calc= df_demographics[df_demographics['category'].isin(categories)]

    calc_rich= calc.sort_values(by='ca', ascending= False)
    
    top_20=calc_rich.head(10)
    
    fig3 = px.bar(top_20, x='name', y='ca', color='ca')
    fig3.update_layout(title='Top Foods rich in Calcium', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig3)

    st.subheader("To view the sources of this data:")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "1: [Kidney Stone Diet: Foods to Eat and Avoid](https://www.healthline.com/health/kidney-stone-diet)"
        "2: [5 steps for preventing kidney stones - Harvard Health Blog](https://www.health.harvard.edu/blog/5-steps-for-preventing-kidney-stones-201310046721#:~:text=Avoid%20stone%2Dforming%20foods%3A%20Beets,consume%20them%20in%20smaller%20amounts.)"
        "3: [Medical and dietary therapy for kidney stone prevention](https://doi.org/10.4111/kju.2014.55.12.775)"
        
    

def gallstones_page():
   #gall stones

    st.title("Gallbladder Stones")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>The gallbladder is an organ that stores bile, which is a fluid that is produced by the liver and used for digestion.  According to Harvard Health Publications, 80% of gallbladder stones, or gallstones, are formed when the amount of cholesterol in the bile is high. There are several risk factors that may lead to the formation of gallstones. Among these, the diet related risk factors include excessive consumption of high-fat or high-cholesterol foods, or low consumption of fibrous foods.  To avoid formation of gallstones, it is recommended to consume high-fiber foods, whole grains, healthy (unsaturated) fats, and foods high in vitamin C. Consumption of refined carbohydrates, sugar, and saturated fats should be reduced.</h6>",unsafe_allow_html=True)
    st.markdown("")
    
    #Based on categories
    categories=['Grains', 'Legumes', 'Vegetables', 'Fruits', 'Spices', 'Nuts', 'Seeds', 'Juice', 'Sugar', 'Dairy', 'Eggs', 'White Meat', 'Red Meat', 'Seafood']
    
    #4th graph
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in saturated fat (should not be consumed)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Higher consumption of saturated fats increases levels of bad cholesterol, which in turn increases the risk of gallstones. Following are the foods from the dataset having highest amounts of saturated fat. The consumption of these foods should be minimized.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Saturated Fat (milligrams)</span>", unsafe_allow_html=True)
    
    #saturated fat

    fasat= df_demographics[df_demographics['category'].isin(categories)]

    fasat_rich= fasat.sort_values(by='fasat', ascending= False)
    
    top_20=fasat_rich.head(20)
    
    fig4 = px.bar(top_20, x='name', y='fasat', color='fasat')
    fig4.update_layout(title='Foods having highest amounts of Saturated Fat', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig4)

    #5th graph

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in fiber (should be consumed)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Dietary fiber, especially insoluble fiber, reduces bile acids and the levels of cholesterol in bile. Therefore, consumption of a high-fiber diet can prevent formation of gallstones. The foods in the dataset that are highest in fiber are shown in the graph below.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Fiber (grams)</span>", unsafe_allow_html=True)


    #fiber

    fibtg= df_demographics[df_demographics['category'].isin(categories)]

    fibtg_rich= fibtg.sort_values(by='fibtg', ascending= False)
    
    top_20=fibtg_rich.head(20)
    
    fig5 = px.bar(top_20, x='name', y='fibtg', color='fibtg')
    fig5.update_layout(title='Top Foods rich in Fiber', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig5)


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Foods highest in Vitamin C (should be consumed)</span>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>Vitamin C helps to break down cholesterol in the gallbladder and regulates its conversion into bile acids. Therefore, lack of vitamin C increases the risk of gallstones. The graph shows the foods in the dataset that have the highest levels of vitamin C. Adequate amounts of vitamin C should be consumed to reduce the risk of gallstones.</h6>",unsafe_allow_html=True)
    st.markdown("")
    st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Vitamin C (milligrams)</span>", unsafe_allow_html=True)
    
    #vitamin c

    vitc= df_demographics[df_demographics['category'].isin(categories)]

    vitc_rich= vitc.sort_values(by='vitc', ascending= False)
    
    top_20=vitc_rich.head(20)
    
    fig6 = px.bar(top_20, x='name', y='vitc', color='vitc')
    fig6.update_layout(title='Top Foods rich in Vitamin C', autosize=False,width=800, height=800,margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig6)

    st.subheader("To view the sources of this data:")
    my_expander=st.beta_expander("Click Here !!")
    with my_expander:
        "1: [Gallstones: Symptoms, Causes, Risks, Treatment, Diet, & More](https://www.healthline.com/health/gallstones)"
        "2: [Gallstones - Symptoms and causes](https://www.mayoclinic.org/diseases-conditions/gallstones/symptoms-causes/syc-20354214)"
        "3: [Eating, Diet, & Nutrition for Gallstones](https://doi.org/10.1016/j.ymgmr.2015.10.001)"
        

#calling the main function to basically invoke the whole code 
#https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    main()





#code to be used to text display with html properties
#st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.3;'>description</h6>",unsafe_allow_html=True)
#st.markdown("")

#blue title
#st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>1</span>", unsafe_allow_html=True)

#units of parameters
#st.markdown(f"<span style='color: #367588;font-size: 12px;font-weight: bold;'>Units: Protein (grams) & Carbohydrates (grams)</span>", unsafe_allow_html=True)
