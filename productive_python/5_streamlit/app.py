import datetime

from magical_thinking import PaLMBackend

import streamlit as st

st.title("🈲 noname security")

# st.write('')

# age = st.slider('How old is Ben?', 0, 255, 25)
# st.write('Ben is', age, 'years old')

# ipod = st.date_input('Enter the IPO date:', datetime.date(2024, 7, 12))
# st.write('Buying an RTX 4090 in ', ipod - datetime.date.today())

text = st.text_input('Contact support:')
if text:
    backend = PaLMBackend()
    result = backend.request(text)
    st.write(result)
