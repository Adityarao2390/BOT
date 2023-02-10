import streamlit
import pandas
import requests
#import snowflake.connector
#from urllib.error import URLError
streamlit.title('Vegetable and Fruits Mart-sa')

streamlit.header('Vegetable Mart')
streamlit.markdown('Patatos: High')
streamlit.markdown('Tomatos: Medium ')
streamlit.markdown('Onion: Medium')
streamlit.markdown('Capsicum Medium')

#streamlit.text('')
streamlit.header('Sabji Mart')
streamlit.markdown('Califlower: High')
streamlit.header('Main Cource Mart')
streamlit.markdown('Jackfruit: High')
streamlit.markdown('Palak: Medium')

streamlit.header('Spices Mart')
streamlit.markdown('Garlic High')


streamlit.header('Fruits Mart')
streamlit.markdown('Apple: High')

streamlit.sidebar.radio('Select one:', [1, 2])

