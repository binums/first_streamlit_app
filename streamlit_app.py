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


streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")

my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")

streamlit.dataframe(my_data_row)

addMyFruit = streamlit.text_input("What fruit would you like to add?")

if addMyFruit:
  my_cur.execute(f"insert into fruit_load_list values ('{addMyFruit}')")
  streamlit.write(f"Thanks for adding {addMyFruit}")
