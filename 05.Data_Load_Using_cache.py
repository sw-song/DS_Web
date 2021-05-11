import streamlit as st 
import pandas as pd 
import numpy as np

st.title('Data Load Using cache - Uber pickups in NYC')
st.markdown('''
1. Make Function with cache
2. Load Data
'''
)
st.markdown("---")

# 1. Make Function with cache
st.subheader('1. Make Function')
date_column = 'date/time'
data_url = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

@st.cache 
def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x : str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_column] = pd.to_datetime(data[date_column])
    return data
st.code('''
@st.cache 
date_column = 'date/time'
data_url = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x : str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_column] = pd.to_datetime(date[date_column])
    return data
''')

# 2. Load Data
st.subheader('2. Load Data')
## Create a text element and let the reader know the data is loading
data_load_state = st.info('Loading Data...')
## Load 10,000 rows of data into the DataFrame
data = load_data(10000)
## Notify the reader that the data was successfully loaded.
data_load_state.success('The data has already been loaded (using st.cache)')
st.code('''
## Create a text element and let the reader know the data is loading
data_load_state = st.info('Loading Data...')
## Load 10,000 rows of data into the DataFrame
data = load_data(10000)
## Notify the reader that the data was successfully loaded.
data_load_state.success('Done! (using st.cache')
''')