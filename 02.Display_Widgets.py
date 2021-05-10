import streamlit as st 

st.title('Display interactive widgets')
st.title('\n')

## Button
st.button('Click')
st.code('''
st.button('Click')
''')

## Checkbox
st.checkbox('Check')
st.code('''
st.checkbox('Check')
''')

## Radio
st.radio('Select', 
['apple','banana','kiwi'])
st.code('''
st.radio('Select', 
['apple','banana','kiwi'])
''')

## Multiselect
st.multiselect('Drop Down', 
['bmw','benz', 'audi', 'hyundai', 'lexus'])
st.code('''
st.multiselect('Drop Down', 
['bmw','benz', 'audi', 'hyundai', 'lexus'])
''')

## Slider
st.slider('Slider',
min_value=0, max_value=500)
st.code('''
st.slider('Slider',
min_value=0, max_value=500)
''')