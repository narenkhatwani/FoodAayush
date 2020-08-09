import streamlit as st

#https://docs.streamlit.io/en/stable/api.html#display-text
#for widget types 


# adding title
st.title('Food Aayush')
# adding text    
st.markdown('Food Quality Analysis at your fingertips')

#declare and add sidebar
st.sidebar.title("Menu")

st.sidebar.info("Welcome to Food Aayush Data Analytics. Here you can analyse the nutritional value of food and draw some schematics")
