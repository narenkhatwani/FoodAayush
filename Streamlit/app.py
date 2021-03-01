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

#read csv file
DATA_URL = ("resources/assets_modified/01.csv")
#DATA_URL2 = ("resources/assets_modified/ingredient.csv")

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


def main():
    # Register your pages
    pages = {
        "About": about_page,
        "Ingredient Information": page_first,
        "Search for Recipe": page_second,
        "Calorie Calculator": page_three,
        "Heart Disease Map": page_fourth,
        "Food Matrix": page_five
    }

    st.sidebar.title("Navigation 🧭")

    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.radio("(Choose an option to get redirected)", tuple(pages.keys()))
    
    # Display the selected page
    pages[page]()

def about_page():
    st.markdown("<h1 style='text-align: center;'>Food Aayush 🍲 🩺</h1>", unsafe_allow_html=True)
    
    st.subheader("About FoodAayush 🤔")

    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial, sans-serif;line-height: 1.5;'>Food is an essential parameter that plays an important role in the survival of humans. It also plays a major part in depicting a country’s culture. Healthy, nutritious, and high-quality food results in not only a better lifestyle but also develops a person’s immunity and health. Likewise, the consumption of low-quality food which might be deprived of nutritional value impacts a person’s health negatively and makes them susceptible to all types of diseases. In India, there is a persistent complaint, in any civic body-related food section, about the quality of meals available. Likewise, the quality of the oil is also an important factor while cooking any meal. Therefore, the Quality of oil used in frying the food to affect its taste must be monitored too. Its continuous exposure to relatively high temperatures results in degradation of its quality. The purpose of this study is to build an application for the detection of the quality of food and also to detect repeated frying on cooking oils based on the visual properties of the oils. Classification of food items is done on the basis of time left for consumption, edibility, quality, color, and rancidity. The food items are further classified as stale or usable using artificial intelligence algorithms based on the images acquired through a Cell Phone’s camera.</h6>", unsafe_allow_html=True)
    st.markdown("")
    st.subheader("Activity Diagram ♺")
    st.image('resources/about_process_diagram/1.png')

    st.markdown("")
    st.subheader("Some other content")
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>Some explanation</h6>", unsafe_allow_html=True)
    
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
    #to print a small iframe of the csv file
    #format is 'name displayed above dataset','variable in which csv is loaded'

    st.title("Ingredient Information 🍅 🥕 🥒 ")

    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.0;'>In order to ensure proper development and growth of the body, immunity against diseases, and energy to function throughout the day, it is necessary to consume adequate amounts of all nutrients, including proteins, carbohydrates, fats, vitamins, minerals and water. Therefore, the  nutritional value of any food item being consumed is a very important parameter. The content of different nutrients in various foods, consumed either individually or as ingredients in dishes can be found here.</h6>",unsafe_allow_html=True)

    
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

    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Water- {count_water}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Protein- {count_protein}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Ash- {count_ash}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Fat- {count_fat}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Total Fibre- {count_fibretotal}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Insoluble Fibre- {count_fibreinsoluble}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Soluble Fibre- {count_fibresoluble}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Carbohydrates- {count_carbohydrate}g</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color: blue;font-size: 22px;font-weight: bold;'>Energy- {count_energy}kJ</span>", unsafe_allow_html=True)
    

    #infct information
    st.subheader("Some Information about the data source")
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>The above data is taken from the dataset “Indian Food Composition Tables, 2017”, of the National Institute of Nutrition. The approach taken for creation of this dataset was to sample the key foods from all over India which contribute to the nutrient intake of 75% of the population. The consumption data and nutrient composition for the various foods is found and the foods have been ranked according to their contribution to the diet in terms of nutrients.</h6>", unsafe_allow_html=True)
    st.markdown("")
    
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
    st.markdown("Minimum Two ingredients required")

    st.markdown(f"<span style='color: #000080;font-size: 24px;font-weight: bold;'>Dataset Preview</span>", unsafe_allow_html=True)
    data2

    #Ingredient 1
    all_ingredients1 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 1 (Vegetable)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients1.append(j)

    #To remove Duplicates
    all_ingredients1 = list(dict.fromkeys(all_ingredients1))

    #Ingredient 2
    all_ingredients2 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 2 (Vegetable)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients2.append(j)

    #To remove Duplicates
    all_ingredients2 = list(dict.fromkeys(all_ingredients2))
    
    #Ingredient 3
    all_ingredients3 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 3 (Vegetable)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients3.append(j)

    #To remove Duplicates
    all_ingredients3 = list(dict.fromkeys(all_ingredients3))
    
    #Ingredient 4
    all_ingredients4 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 4 (Vegetable)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients4.append(j)

    #To remove Duplicates
    all_ingredients4 = list(dict.fromkeys(all_ingredients4))

    #Ingredient 5
    all_ingredients5 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 5 (Grains, pulses and flour )'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients5.append(j)

    #To remove Duplicates
    all_ingredients5 = list(dict.fromkeys(all_ingredients5))

    #Ingredient 6
    all_spices = ["NA"]
    spices = data2.loc[:, data2.columns == 'Ingredient 6 (Spices)'].values.tolist()


    
    for i in spices:
        for j in i:
            all_spices.append(j)

    #To remove Duplicates
    all_spices = list(dict.fromkeys(all_spices))

    #Ingredient 7
    all_ingredients7 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 7 (Spices)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients7.append(j)

    #To remove Duplicates
    all_ingredients7 = list(dict.fromkeys(all_ingredients7))

    #Ingredient 8
    all_ingredients8 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 8 (Spices)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients8.append(j)

    #To remove Duplicates
    all_ingredients8 = list(dict.fromkeys(all_ingredients8))

    #Ingredient 9
    all_ingredients9 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 9 (Spices)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients9.append(j)

    #To remove Duplicates
    all_ingredients9 = list(dict.fromkeys(all_ingredients9))

    #Ingredient 10
    all_ingredients10 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 10 (Breads)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients10.append(j)

    #To remove Duplicates
    all_ingredients10 = list(dict.fromkeys(all_ingredients10))

    #Ingredient 11
    all_ingredients11 = ["NA"]
    gg = data2.loc[:, data2.columns == 'Ingredient 11 (Milk products)'].values.tolist()

    for i in gg:
        for j in i:
            all_ingredients11.append(j)

    #To remove Duplicates
    all_ingredients11 = list(dict.fromkeys(all_ingredients11))

    #Dropdown for ingredients
    st.subheader("Search for 1st Ingredient")
    ingredient_1 = st.selectbox("1st ingredient name", all_ingredients1)
    st.subheader("Search for 2nd Ingredient")
    ingredient_2 = st.selectbox("2nd ingredient name", all_ingredients2)
    st.subheader("Search for 3rd Ingredient")
    ingredient_3 = st.selectbox("3rd ingredient name", all_ingredients3)
    st.subheader("Search for 4th Ingredient")
    ingredient_4 = st.selectbox("4th ingredient name", all_ingredients4)
    st.subheader("Search for 5th Ingredient")
    ingredient_5 = st.selectbox("5th ingredient name", all_ingredients5)
    st.subheader("Search for 6th Ingredient")
    ingredient_6 = st.selectbox("6th ingredient name", all_spices)
    st.subheader("Search for 7th Ingredient")
    ingredient_7 = st.selectbox("7th ingredient name", all_ingredients7)
    st.subheader("Search for 8th Ingredient")
    ingredient_8 = st.selectbox("8th ingredient name", all_ingredients8)
    st.subheader("Search for 9th Ingredient")
    ingredient_9 = st.selectbox("9th ingredient name", all_ingredients9)
    st.subheader("Search for 10th Ingredient")
    ingredient_10 = st.selectbox("10th ingredient name", all_ingredients10)
    st.subheader("Search for 11th Ingredient")
    ingredient_11 = st.selectbox("11th ingredient name", all_ingredients11)
    

    ingredient_list = [ingredient_1,ingredient_2,ingredient_3,ingredient_4,ingredient_5,ingredient_6,ingredient_7,ingredient_8,ingredient_9,ingredient_10,ingredient_11]

    #Remove NA keyword from list
    ingredient_list = set(filter(lambda x: x != 'NA', ingredient_list))
    ingredient_list = list(ingredient_list)
    # st.markdown(ingredient_list)

    #got all recipe names
    all_recipes = list(x for x in data2['Name of Dish'])
    
    
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
    

    recipe = ", ".join(most_prob)

    st.markdown(f"<span style='color: black;font-size: 22px;font-weight: bold;'>Possible Dishes- {recipe}</span>", unsafe_allow_html=True)
    
    
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
    st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.0;'>The disability-adjusted life year (DALY) is a measure of overall disease burden, expressed as the number of years lost due to ill-health, disability or early death. The below map shows the DALY associated with heart disease for each state in India.</h6>",unsafe_allow_html=True)
    st.markdown("")
    #loading Map data from CSV file
    df = pd.read_csv("resources/streamlit_map/cases2.csv")

    raw_data=st.checkbox('See Raw Data')
    if raw_data: 
        st.write(df)
    
    
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

    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>One of the major causes of heart disease is the consumption of unhealthy food. In India, heart disease is a serious and widespread problem due to the excessive use of oil, spices and salt in cooking. Excessive use of oil increases cholesterol, which contributes to heart disease. Although spices are good for health, excessive consumption of chilli peppers is not good for the heart. Excessive consumption of salt increases blood pressure which also leads to coronary heart disease.</h6",unsafe_allow_html=True)

    st.subheader("Calorie Content of Heart Disease causing Foods in each Indian State")
   
    st.markdown("<h6 style='text-align: justify;font-size:110%;font-family:Arial,sans-serif;line-height: 1.5;'>There are many cuisines in India, as each state has its own popular foods. In each of these cuisines, there are many unhealthy food items which may contribute to heart disease. The below data shows popular food items from each of the Indian states which contribute to heart disease, along with their calorie content.</h6",unsafe_allow_html=True)

    st.markdown("")
    
    st.write(df_statefood)  # visualize my dataframe in the Streamlit app


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

    st.subheader("Visualization of the raw data")  # add a title
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


    #plt.legend(handles = [blue_patch , white_patch],title='title', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size':15}) 

    #legend inside
    #plt.legend(handles = [blue_patch , white_patch])

    plt.xlabel('Food Compatibility Matrix (Food Categories)')


    st.pyplot(plt,dpi=100)

    st.subheader("2. Food compatibility matrix (For harmful combinations of specific food items)")
    st.markdown("Apart from the above generalized categories, there are some specific food items which are harmful when consumed together. Most people are not aware of these combinations. A prominent example is banana milkshake. It is a popular beverage but most people are not aware that milk should not be consumed with bananas as it causes heaviness and may also lead to lethargy. Such combinations of food items are indicated in the below data.")

    df2 = pd.read_csv("resources/Food_Matrix/Food_Matrix2.csv")  # read a CSV file inside the 'data" folder next to 'app.py'

    df21 = pd.read_csv("resources/Food_Matrix/Food_Matrix2.csv")

    raw_data2= st.checkbox('See Raw Data ')
    if raw_data2: 
        st.write(df21)


    st.subheader("Visualization of the above given data")  # add a title
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
if __name__ == "__main__":
    main()







