import streamlit as st 
import numpy as np
import pandas as pd


st.title('Start Streamlit')
st.markdown('''
0. Progress Bar
1. write + text
2. write + DataFrame
3. No write + DataFrame
4. line chart
5. Display Map
6. show data with checkbox
7. show data with selectbox
8. show data with sidebar
9. slider with sidebar
10. show text when clicked
11. show text list when clicked
''')
st.markdown("---")

## progress bar
st.subheader('0. Progress Bar')
import time
st.info('Downloading data from server...')

### Add a placeholder 
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    ### Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

st.success('All data has been loaded!')

## write + text
st.subheader('1. write + text')
st.write('This is text')
st.code('''
st.write('This is text')
''')

## write + DataFrame
st.subheader('2. write + DataFrame')
st.write({
    'fruit' : ['apple', 'banana', 'kiwi'],
    'sugar' : [26, 66, 17]
})
st.code('''
st.write({
    'fruit' : ['apple', 'banana', 'kiwi'],
    'sugar' : [26, 66, 17]
})
''')

## No write + DataFrame
st.subheader('3. No write + DataFrame')
df = pd.DataFrame({
    'fruit' : ['apple', 'banana', 'kiwi'],
    'sugar' : [26, 66, 17]
})
df
st.code('''
df = pd.DataFrame({
    'fruit' : ['apple', 'banana', 'kiwi'],
    'sugar' : [26, 66, 17]
})
df
''')

## line chart
st.subheader('4. line chart')
chart_data = pd.DataFrame(
    columns = ['apple', 'banana', 'kiwi'],
    data=
    [[25,65,16],
     [26,66,17],
     [27,67,17],
     [27,65,17],
     [27,66,17],
     [27,66,18],
     [27,65,17],
     [28,66,17],
     [26,66,16],]
)
st.line_chart(chart_data)
st.code('''
chart_data = pd.DataFrame(
    columns = ['apple', 'banana', 'kiwi'],
    data=
    [[25,65,16],
     [26,66,17],
     [27,67,17],
     [27,65,17],
     [27,66,17],
     [27,66,18],
     [27,65,17],
     [28,66,17],
     [26,66,16],]
)
st.line_chart(chart_data)
''')

## Display Map
st.subheader('5. Display Map')
map_data = pd.DataFrame(
    columns = ['lat', 'lon'],
    data = np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4]
    )
st.map(map_data)
st.code('''
map_data = pd.DataFrame(
    columns = ['lat', 'lon'],
    data = np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4]
    )
st.map(map_data)
''')

## show data with checkbox
st.subheader('6. show data with checkbox')
if st.checkbox('Show DataFrame'):
    chart_data = pd.DataFrame(
        columns = ['apple', 'banana', 'kiwi'],
        data = [[25,65,16],
                [26,66,17],
                [27,67,17],
                [27,65,17],
                [27,66,17],
                [27,66,18],
                [27,65,17],
                [28,66,17],
                [26,66,16]]
        )
    chart_data
st.code('''
if st.checkbox('Show DataFrame'):
    chart_data = pd.DataFrame(
        columns = ['apple', 'banana', 'kiwi'],
        data = [[25,65,16],
                [26,66,17],
                [27,67,17],
                [27,65,17],
                [27,66,17],
                [27,66,18],
                [27,65,17],
                [28,66,17],
                [26,66,16]]
        )
    chart_data
''')
    

## show data with selectbox
st.subheader('7. show data with selectbox')
option = st.selectbox(
    'Choose fruit', df['fruit']
    # df = pd.DataFrame({
    #       'fruit' : ['apple', 'banana', 'kiwi'],
    #       'sugar' : [26, 66, 17]
    # })
)
st.info('Do you like "{}" ?'.format(option))
st.code('''
option = st.selectbox(
    'Choose fruit', df['fruit']
    # df = pd.DataFrame({
    #       'fruit' : ['apple', 'banana', 'kiwi'],
    #       'sugar' : [26, 66, 17]
    # })
)
st.info('Do you like "{}" ?'.format(option))    
''')

## show data with sidebar
st.subheader('8. show data with sidebar')
sidebar_option = st.sidebar.selectbox(
    'sidebar_selectbox', df['fruit'], key='<sidebar>'
)
st.info('<sidebar> Do you like "{}" ?'.format(sidebar_option))    
st.code('''
sidebar_option = st.sidebar.selectbox(
    'Choose fruit', df['fruit'], key='<sidebar>'
)
st.info('<sidebar> Do you like "{}" ?'.format(sidebar_option))    
''')

## slider with sidebar
st.subheader('9. slider with sidebar')
select_number = st.sidebar.slider(
    'sidebar_slider', min_value=0, max_value=500
    )
st.info('<sidebar> You select number "{}" in sidebar_slider'.format(select_number))

## show text when clicked
st.subheader('10. show text when clicked')
left_columns, right_columns = st.beta_columns(2)
clicked = left_columns.button('click')
if clicked:
    right_columns.write("Hi! Streamlit! I'm right column")
    left_columns.write("hello! I'm left column")
st.code('''
left_columns, right_columns = st.beta_columns(2)
clicked = left_columns.button('click')
if clicked:
    right_columns.write("Hi! Streamlit! I'm right column")
    left_columns.write("hello! I'm left column")
''')

## show text list when clicked
st.subheader('11. show text list when clicked')
expander = st.beta_expander("FAQ")
expander.write('1th')
expander.write('2th')
expander.write('3th')
st.code('''
expander = st.beta_expander("FAQ")
expander.write('1th')
expander.write('2th')
expander.write('3th')
''')
