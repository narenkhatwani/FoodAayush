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




df = pd.read_csv("Food_Matrix - Sheet1.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Food Matrix")  # add a title
st.write(df)  # visualize my dataframe in the Streamlit app


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib.patches as mpatches
from matplotlib import cm
data = pd.read_csv('Food_Matrix - Sheet1.csv' , na_values= "NaN")
data.fillna(0 , inplace = True)


id_labels = data.columns[1:]
print(id_labels)
# take the transpose since you want to see id on y-axis
id_matrix = np.array(data[id_labels].values, dtype=float).T
#concert_dates = pd.to_datetime(data['concert_date'])
#concert_dates = [d.date() for d in concert_dates]

fig, ax = plt.subplots()
# cmap={}
# cmap["Sequentials"] = 'Reds'

mat = ax.imshow(id_matrix, cmap="Reds", interpolation='nearest')

plt.yticks(range(id_matrix.shape[0]), id_labels)
plt.xticks(range(id_matrix.shape[1]), id_labels)
plt.xticks(rotation=30)

blue_patch = mpatches.Patch(color='maroon', label='Toxic')
white_patch = mpatches.Patch(color='#FFF5F0', label='Non-Toxic')

plt.legend(handles = [blue_patch , white_patch])

plt.xlabel('FOOD MATRIX')


st.pyplot(plt)

