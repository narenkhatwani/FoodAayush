# About FoodAayush Data Analysis using Streamlit

This section of the FoodAayush application related to data analysis is developed using a Python framework called Streamlit and deployed on Heroku. In this WebApp, a study has been performed on data about various nutritional aspects of food items. The primary dataset used here is Indian Food Composition Tables (IFCT) 2017. Firstly, an analysis of the quantities of different nutrients present in each food item is performed. Next, there is a section related to IFCT Demographics, where there are several features that perform a complete analysis of the IFCT dataset, beginning with checking the data types and null values in the dataset and then going on to finding the correlations between the presence of various nutrients in food, the food items having the highest amounts of multiple nutrients, the distribution of numerous nutrients among the categories of food items present in the dataset, and different other parameters. After the IFCT Demographics section, there is a section called Medical Condition Demographics, where food suggestions are made for people suffering from specific medical conditions. These features use the IFCT dataset; the other features include a 'Search For Recipe' menu where the user can enter the desired ingredients to find the recipes that can be prepared with these ingredients. The calories and the cuisine of a particular dish can also be found. One of the critical features of the WebApp is the Food Matrix, where the user can check the compatibility of various food combinations and find out which varieties are harmful to health. There is also a calorie calculator, where ideal calorie and nutrient intake can be found for a particular user, and a heart disease map, where the number of heart disease cases in the various states of India have been displayed, and unhealthy food items from the cuisine of each state have been found whose consumption may contribute to heart disease.

# Why Streamlit ?

Streamlit is an open-source Python framework that provides an advantageous way to build web apps without any knowledge of web development - having knowledge of Python is sufficient. It is beneficial for building data analysis-related applications because it allows the developer to focus more on the data analysis part, as the user interface design becomes very simple. Widgets are treated as variables, which eliminates the need for callbacks. Visually appealing, high-performance web apps can be built in Python with ease.

# Why plotly?

Plotly is a library that can be used for creating graphical representations of data. It is highly flexible, as any type of visual representation can be created, including scatterplots, box plots, bar graphs and even 3D graphs. Also, unlike the other libraries, plotly can use multiple data sources. Arithmetic operations can also be performed on the columns, and then visualizations can be created for these columns. We can zoom in and out on the graphs and hover over the graph’s values. These factors make it an excellent library to use if applications involving data analysis need to be developed. 

# Why matplotlib?

Matplotlib is the most popularly used library for making visual representations of data. It can be used for creating a wide variety of 2D graphical representations such as bar graphs, pie charts, histograms, and scatterplots. Matplotlib is also very convenient as very few lines of code are required to design these graphs, and also, it makes it very easy to customize the graphs. It is fast, efficient, versatile, and open-source. Therefore, it is an amazing data visualization tool and is very useful for data analysis applications.

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
## How to Deploy a Streamlit Project on Heroku
#### https://github.com/narenkhatwani/streamlit-deployment-heroku
