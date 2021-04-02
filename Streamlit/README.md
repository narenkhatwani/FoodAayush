# About FoodAayush Data Analysis using Streamlit

This section of the FoodAayush application related to data analysis is developed using a Python framework called Streamlit and deployed on Heroku. In this WebApp, a study has been performed on data about various nutritional aspects of food items. The primary dataset used here is Indian Food Composition Tables (IFCT) 2017. Firstly, an analysis of the quantities of different nutrients present in each food item is performed. Next, there is a section related to IFCT Demographics, where there are several features that perform a complete analysis of the IFCT dataset, beginning with checking the data types and null values in the dataset and then going on to finding the correlations between the presence of various nutrients in food, the food items having the highest amounts of multiple nutrients, the distribution of numerous nutrients among the categories of food items present in the dataset, and different other parameters. After the IFCT Demographics section, there is a section called Medical Condition Demographics, where food suggestions are made for people suffering from specific medical conditions. These features use the IFCT dataset; the other features include a 'Search For Recipe' menu where the user can enter the desired ingredients to find the recipes that can be prepared with these ingredients. The calories and the cuisine of a particular dish can also be found. One of the critical features of the WebApp is the Food Matrix, where the user can check the compatibility of various food combinations and find out which varieties are harmful to health. There is also a calorie calculator, where ideal calorie and nutrient intake can be found for a particular user, and a heart disease map, where the number of heart disease cases in the various states of India have been displayed, and unhealthy food items from the cuisine of each state have been found whose consumption may contribute to heart disease.

## Requirements for the project

- streamlit==0.64.0
- matplotlib==3.2.2
- pandas==1.0.5
- plotly==4.9.0
- numpy==1.18.5
- dash==1.17.0

## How to Run the Project Locally

Open the terminal/cmd in the Streamlit Folder and run the following command

```bash
streamlit run app.py
```
