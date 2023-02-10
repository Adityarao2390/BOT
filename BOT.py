import streamlit
import pandas
import requests
#import snowflake.connector
from urllib.error import URLError
streamlit.title('Vegetable and Fruits Mart-sa')

streamlit.header('Vegetable Mart')
streamlit.text('{Patatos: High')
streamlit.text('Tomatos: Medium')
streamlit.text('Onion: Medium')
#streamlit.text('')
streamlit.header('Sabji Mart')
streamlit.text('Califlower: High')
streamlit.header('Fruits Mart')
streamlit.header('Apple: High')
"""
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # write your own comment - what does this do?
    return fruityvice_normalized
 
streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
  streamlit.error("Please Select a Fruit to get information")
# streamlit.write('The user entered ', fruit_choice)
 else:
   back_from_fumction=get_fruityvice_data(fruit_choice)
   streamlit.dataframe(back_from_fumction)

except URLError as e:
 streamlit.error()
# streamlit.stop()

streamlit.header("View our Fruit List - Add Your Fav !")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list" )
    return my_cur.fetchall()
   
# button
if streamlit.button('Get fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
# streamlit.header("The Fruit List Contains:")
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
# streamlit.stop()
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')" )
    return "Thanks for adding "+new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
# button
if streamlit.button('Add a Fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
# streamlit.write('Thanks for adding ', add_my_fruit)

"""
