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



df = pd.read_csv("Food_Matrix - Sheet1 (2).csv")  # read a CSV file inside the 'data" folder next to 'app.py'


st.title("Food Matrix")  # add a title

st.write(df)  # visualize my dataframe in the Streamlit app


data = pd.read_csv('Food_Matrix - Sheet1 (2).csv' , na_values= "NaN")
data.fillna(0 , inplace = True)


id_labels = data.columns[1:]
print(id_labels)
# take the transpose since you want to see id on y-axis
id_matrix = np.array(data[id_labels].values, dtype=float).T

fig, ax = plt.subplots(figsize=(11,11))


mat = ax.imshow(id_matrix, cmap="Reds", interpolation='nearest')

plt.yticks(range(id_matrix.shape[0]), id_labels)
plt.xticks(range(id_matrix.shape[1]), id_labels)
plt.xticks(rotation=30)

blue_patch = mpatches.Patch(color='maroon', label='Toxic')
white_patch = mpatches.Patch(color='#FFF5F0', label='Non-Toxic')


fontP = FontProperties()
fontP.set_size('xx-small')

#legend outside
plt.legend(handles = [blue_patch , white_patch], bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size':15}) 


plt.rcParams['savefig.facecolor']='white'

#plt.legend(handles = [blue_patch , white_patch],title='title', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size':15}) 

#legend inside
#plt.legend(handles = [blue_patch , white_patch])

plt.xlabel('FOOD MATRIX') 


st.pyplot(plt,dpi=100)

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