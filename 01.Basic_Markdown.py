import streamlit as st 

st.title('Basic Syntax & Markdown')
st.markdown('''
1. Title
2. Header
3. Sub Header
4. Text
5. Markdown
6. Message
7. Code
''')
st.markdown("---")
## Title
st.subheader('1. Title')
st.title('Title')
st.code('''
st.title('Title)
'''
)

## Header
st.subheader('2. Header')
st.header('Header')
st.code('''
st.header('Header')
'''
)

## Sub Header
st.subheader('3. Sub Header')
st.subheader('SubHeader')
st.code('''
st.subheader('SubHeader')
'''
)

## Text
st.subheader('4. Text')
st.text('Text')
st.code('''
st.text('Text')
'''
)

## Markdown
st.subheader('5. Markdown')
st.markdown('# Markdown Title')
st.code('''
st.markdown('# Markdown Title')
'''
)
st.markdown('## Markdown Header')
st.code('''
st.markdown('## Markdown Header')
'''
)
st.markdown('### Markdown SubHeader')
st.code('''
st.markdown('### Markdown SubHeader')
'''
)
# Message
st.subheader('6. Message')
st.success('Success')
st.code('''
st.success('Success')
'''
)
st.info('Info')
st.code('''
st.info('Info')
'''
)
st.warning('Warning')
st.code('''
st.warning('Warning')
'''
)
st.error('Error')
st.code('''
st.error('Error')
'''
)
# Code
st.subheader('7. Code')
st.code("print('streamlit')")
st.code('''
st.code("print('streamlit')")
'''
)