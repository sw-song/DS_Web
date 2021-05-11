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

## Select Slider
st.select_slider('slider',
                options=['min', '1/3' , '2/3', 'max'])

## Select Slider
st.code('''
st.select_slider('slider',
                options=['min', '1/3' , '2/3', 'max'])
''')

## Text Input
st.text_input('Enter Some Text')
st.code('''
st.text_input('Enter Some Text')
''')

## Number Input
st.number_input('Enter a Number')
st.code('''
st.number_input('Enter a Number')
''')

## Text Area
st.text_area('Text Zone')
st.code('''
st.text_area('Text Zone')
''')

## Date Input
st.date_input('Select Date')
st.code('''
st.date_input('Select Date')
''')

## Time Input
st.time_input('Time Entry')
st.code('''
st.time_input('Time Entry')
''')

## File Uploader
st.file_uploader('File Uploader')
st.code('''
st.file_uploader('File Uploader')
''')

## Color Picker
st.color_picker('Pick a Color')
st.code('''
st.color_picker('Pick a Color')
''')
