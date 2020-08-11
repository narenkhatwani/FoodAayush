import pandas as pd
import streamlit as st

@st.cache
def load_data():
    df = pd.DataFrame({'Hospital': ['Nick hospital', 'Nick hospital', 'Nick hospital',
                                'Krish hospital', 'Krish hospital', 'Krish hospital'],
                   'document_source': ['NAR', 'PAR', 'Free Text', 'NAR', 'PAR', 'Free Text'],
                   'document_count': [1200, 150, 3, 2500, 342, 300]})
    return df

df = load_data()

st.sidebar.title("Filter data")

#Checkbox for Hospitals
hosp_list = st.sidebar.selectbox("Select Hospital", df["Hospital"].unique())

#Chech box for Documents
doc_source = st.sidebar.selectbox("Select Document source", df["document_source"].unique())

st.subheader('Document Count')

count = df.loc[(df["Hospital"] == hosp_list) & (df["document_source"] == doc_source), 'document_count'].iloc[0]
count_2 = df.query(f"Hospital=='{hosp_list}' & document_source=='{doc_source}'")['document_count'].iloc[0]

st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>{count}</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: blue;font-size: 24px;font-weight: bold;'>{count_2}</span>", unsafe_allow_html=True)
