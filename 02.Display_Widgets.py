import streamlit as st 

st.title('Display interactive widgets')
st.markdown('''
1. Button
2. Checkbox
3. Radio
4. Multiselect
5. Slider
6. Select Slider
7. Text Input
8. Number Input
9. Text Area
10. Data Input
11. Time Input
12. File Uploader
13. Color Picker
''')
st.markdown("---")

## Button
st.subheader("1. Button")
st.button('Click')
st.code('''
st.button('Click')
''')

## Checkbox
st.subheader("2. Checkbox")
st.checkbox('Check')
st.code('''
st.checkbox('Check')
''')

## Radio
st.subheader("3. Radio")
st.radio('Select', 
        ['apple','banana','kiwi'])
st.code('''
st.radio('Select', 
        ['apple','banana','kiwi'])
''')

## Multiselect
st.subheader("4. Multiselect")
st.multiselect('Drop Down', 
            ['bmw','benz', 'audi', 'hyundai', 'lexus'])
st.code('''
st.multiselect('Drop Down', 
            ['bmw','benz', 'audi', 'hyundai', 'lexus'])
''')

## Slider
st.subheader("5. Slider")
st.slider('Slider',
        min_value=0, max_value=500)
st.code('''
st.slider('Slider',
        min_value=0, max_value=500)
''')

## Select Slider
st.subheader("6. Select Slider")
st.select_slider('slider',
                options=['min', '1/3' , '2/3', 'max'])

st.code('''
st.select_slider('slider',
                options=['min', '1/3' , '2/3', 'max'])
''')

## Text Input
st.subheader("7. Text Input")
st.text_input('Enter Some Text')
st.code('''
st.text_input('Enter Some Text')
''')

## Number Input
st.subheader("8. Number Input")
st.number_input('Enter a Number')
st.code('''
st.number_input('Enter a Number')
''')

## Text Area
st.subheader("9. Text Area")
st.text_area('Text Zone')
st.code('''
st.text_area('Text Zone')
''')

## Date Input
st.subheader("10. Data Input")
st.date_input('Select Date')
st.code('''
st.date_input('Select Date')
''')

## Time Input
st.subheader("11. Time Input")
st.time_input('Time Entry')
st.code('''
st.time_input('Time Entry')
''')

## File Uploader
st.subheader("12. File Uploader")
st.file_uploader('File Uploader')
st.code('''
st.file_uploader('File Uploader')
''')

## Color Picker
st.subheader("13. Color Picker")
st.color_picker('Pick a Color')
st.code('''
st.color_picker('Pick a Color')
''')
