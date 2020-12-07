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

#https://github.com/MarcSkovMadsen/awesome-streamlit
#https://docs.streamlit.io/en/stable/api.html#display-text
#for widget types 
#for demo purpose 

# adding title
st.sidebar.markdown(f"<span style='color: black;font-size: 36px;font-weight: bold;'>Food Aayush</span>", unsafe_allow_html=True)

st.sidebar.info("Welcome to Food Aayush Data Analytics. Here you can analyse the nutritional value of food and draw some schematics")
# adding text
st.sidebar.markdown(f"<span style='color: black;font-size: 14px;'>Food Quality Analysis at your fingertips</span>", unsafe_allow_html=True)


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

#loading Map data from CSV file
df = pd.read_csv("resources/streamlit_map/cases2.csv")

def main():
    # Register your pages
    pages = {
        "About": about_page,
        "Ingredient Information": page_first,
        "Search for Recipe": page_second,
        "Calorie Calculator": page_three,
        "Heart Disease Map": page_fourth,
    }

    st.sidebar.title("Navigation")

    st.sidebar.subheader("Go To :")
    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    #page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))

    # Display the selected page
    pages[page]()

def about_page():
    st.title("Food Aayush")

    st.info("Welcome to Food Aayush Data Analytics. Here you can analyse the nutritional value of food and draw some schematics")

    st.subheader("About FoodAayush")

    st.write("Food is an essential parameter that plays an important role in the survival of humans. It also plays a major part in depicting a country’s culture. Healthy, nutritious, and high-quality food results in not only a better lifestyle but also develops a person’s immunity and health. Likewise, the consumption of low-quality food which might be deprived of nutritional value impacts a person’s health negatively and makes them susceptible to all types of diseases. In India, there is a persistent complaint, in any civic body-related food section, about the quality of meals available. Likewise, the quality of the oil is also an important factor while cooking any meal. Therefore, the Quality of oil used in frying the food to affect its taste must be monitored too. Its continuous exposure to relatively high temperatures results in degradation of its quality. The purpose of this study is to build an application for the detection of the quality of food and also to detect repeated frying on cooking oils based on the visual properties of the oils. Classification of food items is done on the basis of time left for consumption, edibility, quality, color, and rancidity. The food items are further classified as stale or usable using artificial intelligence algorithms based on the images acquired through a Cell Phone’s camera.")

    st.subheader("About Streamlit")

    st.write("""[Streamlit](https://streamlit.io/) is The fastest way to build and share data apps Turn data scripts into sharable web apps in minutes. All in Python. All for free. No front-end experience required.""")
    


def page_first():
    #to print a small iframe of the csv file
    #format is 'name displayed above dataset','variable in which csv is loaded'

    st.title("Ingredient Information")

    # st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'> ->Dataset Preview</span>", unsafe_allow_html=True)

    # data

    ### MULTISELECT
    #food_name_input = st.multiselect('Food name',data.groupby('name').count().reset_index()['name'].tolist())

    # by food name
    #if len(food_name_input) > 0:
     #   subset_data = data[data['name'].isin(food_name_input)]

    #Checkbox for Hospitals
    st.subheader("Search for an Ingredient")
    food_list = st.selectbox("Search Here:", data["name"].unique())


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Filter Data Results are :</span>", unsafe_allow_html=True)
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


def page_second():
    #sidebar title
    st.title("Search for Recipe")
    st.markdown("Minimum Two ingredients required")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Dataset Preview</span>", unsafe_allow_html=True)
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
    st.subheader("Search for 1st Ingredient")
    ingredient_1 = st.selectbox("1st ingredient name", all_ingredients)
    st.subheader("Search for 2nd Ingredient")
    ingredient_2 = st.selectbox("2nd ingredient name", all_ingredients)
    st.subheader("Search for 3rd Ingredient")
    ingredient_3 = st.selectbox("3rd ingredient name", all_ingredients)
    st.subheader("Search for 4th Ingredient")
    ingredient_4 = st.selectbox("4th ingredient name", all_ingredients)
    st.subheader("Search for 5th Ingredient")
    ingredient_5 = st.selectbox("5th ingredient name", all_ingredients)
    st.subheader("Search for 6th Ingredient")
    ingredient_5 = st.selectbox("6th ingredient name", all_ingredients)
    st.subheader("Search for 7th Ingredient")
    ingredient_5 = st.selectbox("7th ingredient name", all_ingredients)
    st.subheader("Search for 8th Ingredient")
    ingredient_5 = st.selectbox("8th ingredient name", all_ingredients)
    st.subheader("Search for 9th Ingredient")
    ingredient_5 = st.selectbox("9th ingredient name", all_ingredients)
    st.subheader("Search for 10th Ingredient")
    ingredient_5 = st.selectbox("10th ingredient name", all_ingredients)
    st.subheader("Search for 11th Ingredient")
    ingredient_5 = st.selectbox("11th ingredient name", all_ingredients)
    

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
    
def page_three():
    st.title("Calorie Calculator")
    
    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Add your total daily intake of calories</span>", unsafe_allow_html=True)

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


    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Want to know your ideal calorie intake ??</span>", unsafe_allow_html=True)

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

def page_fourth():
    st.title('Indian Map for Heart Disease')
    st.markdown("Data from 2017 - In DALYs Per 100,000 People")
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
            title={'text': "Active Cases"},

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

if __name__ == "__main__":
    main()







#background image for the webapp
page_bg_img = '''
<style>
body {
background-image: url("https://i.imgur.com/s372Lj3.png?1");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)




