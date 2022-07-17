import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def getFruityviceData(choice):
  fruityviceResponse = requests.get(f'https://fruityvice.com/api/fruit/{choice}')
  return pandas.json_normalize(fruityviceResponse.json())
  

streamlit.title("My Mom's New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")


myFruitList = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
myFruitList = myFruitList.set_index('Fruit')


streamlit.header("🍌 🥭 Build Your OwnFruit Smoothie 🥝 🍇")
fruitsSelected = streamlit.multiselect("Pick some fruits:", list(myFruitList.index), ['Avocado', 'Strawberries'])
fruitsToShow = myFruitList.loc[fruitsSelected]

streamlit.dataframe(fruitsToShow)

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruitChoice = streamlit.text_input("What fruit would you like informantion about?")
  
  if not fruitChoice:
    streamlit.error("Please select a fruit to get information")
  
  else:  
    streamlit.dataframe(getFruityviceData(fruitChoice))
    
except URLError as e:
  streamlit.error()  


def getFruitLoadList():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = getFruitLoadList()
  streamlit.dataframe(my_data_row)
  
streamlit.stop()
 

addMyFruit = streamlit.text_input("What fruit would you like to add?")

if addMyFruit:
  my_cur.execute(f"insert into fruit_load_list values ('{addMyFruit}')")
  streamlit.write(f"Thanks for adding {addMyFruit}")
