import streamlit
import pandas
import requests
#import snowflake.connector
#from urllib.error import URLError
streamlit.title('Vegetable and Fruits Mart-sa')

streamlit.header('Vegetable Mart')
streamlit.markdown('Patatos: High')
streamlit.text('Tomatos: Medium ')
streamlit.text('Onion: Medium')
streamlit.text('Capsicum Medium')

#streamlit.text('')
streamlit.header('Sabji Mart')
streamlit.text('Califlower: High')
streamlit.header('Main Cource Mart')
streamlit.text('Jackfruit: High')
streamlit.text('Palak: Medium')

streamlit.header('Spices Mart')
streamlit.text('Garlic High')


streamlit.header('Fruits Mart')
streamlit.text('Apple: High')

streamlit.sidebar.radio('Select one:', [1, 2])
#streamlit run BOT1.py

