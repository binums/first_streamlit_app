import streamlit
import pandas
import requests

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

fruitChoice = streamlit.text_input("What fruit would you like informantion about?", 'Kiwi')
streamlit.write('The user entered', fruitChoice)

fruityviceResponse = requests.get(f'https://fruityvice.com/api/fruit/{fruitChoice}')

fruityviceNormalized = pandas.json_normalize(fruityviceResponse.json())

streamlit.dataframe(fruityviceNormalized)

