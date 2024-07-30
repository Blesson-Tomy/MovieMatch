import pathway as pw
import streamlit as st
import json
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyD1y1hnm74DsaC-kw1vxeXliv77pNWkoEg")

st.set_page_config(page_title="MovieMatch", page_icon="🎬")
st.title("MovieMatch")
st.write("Welcome to MovieMatch! This is a chatbot that can help you find a movie to watch.")

st.text_input("Enter the movies that you enjoy watching:", key="input", placeholder="Input movies here")
st.button("Get Recommendations")

st.write("Here are some movies that you might enjoy watching:")




#Once the output appears, my personal details should be able to appear.
st.write("This app is created as part of the Pathway AI Bootcamp conducted in collaboration with Mulearn and Pathway.com.")
st.link_button("Made with love by Blesson K Tomy", "https://www.profile.blessonktomy.tech")

