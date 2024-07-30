import pathway as pw
import streamlit as st
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="GEMINI_API_KEY")

st.set_page_config(page_title="MovieMatch", page_icon="🎬")
st.title("MovieMatch")
st.write("Welcome to MovieMatch! This is a chatbot that can help you find english movies to watch.")

context = """You are a very reliable and trustable chatbot. You will only provide answers that are accurate and helpful without a doubt. The user will input the names of multiple movies that they enjoy watching. 
You are to recommend various other movies of similar genre, style and language. You are not allowed to display the response metadata. Print the movies in a new line.

Here is an example of how the user input and your output should look like:
Example 1. User input: The Dark Knight, Inception, Interstellar
    You enjoy english movies with action, adventure and Sci-Fi genre.
    Here are some movies that I think you might enjoy watching:  \n1) [The Prestige](https://www.imdb.com/title/tt0068646/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_the%2520godfather)  \n2) [Dunkirk](https://www.imdb.com/title/tt5013056/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_Dunkirk)  \n3) [Tenet](https://www.imdb.com/title/tt6723592/?ref_=nv_sr_srsg_0_tt_6_nm_2_in_0_q_Tenet)

Example 2. User input: The Shawshank Redemption, The Godfather, The Dark Knight
    You enjoy english movies with crime, drama and action genre.
    Here are some other movies that I think you might enjoy watching:  \n1) [The Godfather Part II](https://www.imdb.com/title/tt0071562/?ref_=nv_sr_srsg_3_tt_7_nm_1_in_0_q_the%2520godfa)  \n2) [The Green Mile](https://www.imdb.com/title/tt0120689/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_The%2520Green%2520Mile)  \n3) [The Departed](https://www.imdb.com/title/tt0407887/?ref_=fn_al_tt_1)

Example 3. User input: Jab Harry Met Sejal, Kabhi Khushi Kabhie Gham, Kabhi Alvida Naa Kehna
    You enjoy hindi movies with romance, drama and comedy genre.
    Here are some other movies that I think you might enjoy watching: \n1) [Kal Ho Naa Ho](https://www.imdb.com/title/tt0347304/?ref_=fn_al_tt_1)  \n2) [Kabhi Khushi Kabhie Gham](https://www.imdb.com/title/tt0248126/?ref_=fn_al_tt_1)  \n3) [Dilwale Dulhania Le Jayenge](https://www.imdb.com/title/tt0112870/?ref_=nv_sr_srsg_0_tt_3_nm_0_in_0_q_Dilwale%2520Dulhania%2520Le%2520Jayenge)
   
"""

movies_watched = st.text_input("Enter the movies that you enjoy watching:", key="input", placeholder="Input movies here")

Jsoncov = "please convert the given content into a json table with keys as numbers and each key has a Name, Year, Genre and Languages. Expand the body with valid information regarding the heading.  \n{  \n  \"movies\": [  \n    {  \n      \"name\": \"Input name of the movie\",  \n      \"year\": year of release,  \n      \"genre\": \"Genre of release of the movie\",  \n      \"language\": \"Language Medium of the movie\" \n    } You are to display the JSON output of each movie in a new line."

class InputSchema(pw.Schema):
    Name: str
    Year: int
    Genre: str
    Language: str

def get_recommendations(movies):
    recommendations = model.invoke(context + movies)
    return recommendations.content

def get_json(prompt):
    jsonrec = model.invoke(Jsoncov + prompt)
    return jsonrec.content

if st.button("Get Recommendations"):
    response = get_recommendations(movies_watched)
    st.write(response)
    st.write(get_json(response))
    
    #try:
    json_data = json.loads(get_json(response))
    #except json.JSONDecodeError as e:
    st.markdown(f"# TABLE VIEW :")
    st.write(get_json(response))
    if 'json_data' in locals():
        op = pw.Table.from_dict(json.loads(get_json(response)), schema=InputSchema)
        pw.io.jsonlines.write(op,"/mnt/data/newsdoc.jsonl")
    pw.run()

    st.write("This app is created as part of the Pathway AI Bootcamp conducted in collaboration with Mulearn and Pathway.com.")
    st.link_button("Made with love by Blesson K Tomy", "https://www.profile.blessonktomy.tech")






