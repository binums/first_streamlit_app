import streamlit
import pandas

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
