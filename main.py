import streamlit as st 


## Title
st.title('Basic Syntax/Markdown Test')
st.title('Title')
st.code('''
st.title('Title)
'''
)

## Header
st.header('Header')
st.code('''
st.header('Header')
'''
)

## Sub Header
st.subheader('SubHeader')
st.code('''
st.subheader('SubHeader')
'''
)

## Text
st.text('Text')
st.code('''
st.text('Text')
'''
)

## Markdown
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
st.code("print('streamlit')")
st.code('''
st.code("print('streamlit')")
'''
)