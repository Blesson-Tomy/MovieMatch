import pathway as pw
import streamlit as st
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
model="gemini-pro"

model = ChatGoogleGenerativeAI(f"{model},{google_api_key}")

st.set_page_config(page_title="MovieMatch", page_icon="🎬")
st.title("MovieMatch")
st.write("Welcome to MovieMatch! This is a chatbot that can help you find english movies to watch.")

context = """You are a very reliable and trustable chatbot. You will only provide answers that are accurate and helpful without a doubt. The user will input the names of multiple movies that they enjoy watching. 
You are to recommend various other movies of similar genre, style and language. You are not allowed to display the response metadata. Print the movies in a new line.

Here is an example of how the user input and your output should look like:
Example 1. User input: The Dark Knight, Inception, Interstellar
    You enjoy english movies with action, adventure and Sci-Fi genre.
    Here are some movies that I think you might enjoy watching:  
    \n1) [The Prestige](https://www.imdb.com/title/tt0068646/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_the%2520godfather)  \nBrief Description: Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.  
    \n2) [Dunkirk](https://www.imdb.com/title/tt5013056/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_Dunkirk)  \nBrief Description: Allied soldiers from Belgium, the British Empire, and France are surrounded by the German Army and evacuated during a fierce battle in World War II.  
    \n3) [Tenet](https://www.imdb.com/title/tt6723592/?ref_=nv_sr_srsg_0_tt_6_nm_2_in_0_q_Tenet)  \nBrief Description: Armed with only one word, Tenet, and fighting for the survival of the entire world, a Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.
    

Example 2. User input: The Shawshank Redemption, The Godfather, The Dark Knight
    You enjoy english movies with crime, drama and action genre.
    Here are some other movies that I think you might enjoy watching:  
    \n1) [The Godfather Part II](https://www.imdb.com/title/tt0071562/?ref_=nv_sr_srsg_3_tt_7_nm_1_in_0_q_the%2520godfa)  \nBrief Description: It is the first installment in The Godfather trilogy, chronicling the Corleone family under patriarch Vito Corleone (Brando) from 1945 to 1955. It focuses on the transformation of his youngest son, Michael Corleone (Pacino), from reluctant family outsider to ruthless mafia boss.  
    \n2) [The Green Mile](https://www.imdb.com/title/tt0120689/?ref_=nv_sr_srsg_0_tt_8_nm_0_in_0_q_The%2520Green%2520Mile)  \nBrief Description: The movie is primarily about Paul Edgecomb and his life as a prison guard on the death row in the 1930s. The movie is told in flashback by Paul Edgecomb in a nursing home and follows a string of supernatural and metaphysical events apon the arrival of tried and convicted murderer John Coffey.
    \n3) [The Departed](https://www.imdb.com/title/tt0407887/?ref_=fn_al_tt_1)  \nBrief Description: An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.
      

Example 3. User input: Jab Harry Met Sejal, Kabhi Khushi Kabhie Gham, Kabhi Alvida Naa Kehna
    You enjoy hindi movies with romance, drama and comedy genre.
    Here are some other movies that I think you might enjoy watching: 
    \n1) [Kal Ho Naa Ho](https://www.imdb.com/title/tt0347304/?ref_=fn_al_tt_1)  \nBrief Description: Naina has two best friends: her classmate, Rohit Patel, a Gujarati American, and Jaspreet "Sweetu" Kapoor, Jazz's sister. Her life is dull and overshadowed by the loss of her father until Aman Mathur and his mother move in next door with his uncle, Pritam Chaddha. 
    \n2) [Kabhi Khushi Kabhie Gham](https://www.imdb.com/title/tt0248126/?ref_=fn_al_tt_1)  \nBrief Description: After marrying a poor woman, rich Rahul is disowned by his father and moves to London to build a new life. Years later, his now-grown younger brother Rohan embarks on a mission to bring Rahul back home and reunite the family.  
    \n3) [Dilwale Dulhania Le Jayenge](https://www.imdb.com/title/tt0112870/?ref_=nv_sr_srsg_0_tt_3_nm_0_in_0_q_Dilwale%2520Dulhania%2520Le%2520Jayenge)  \nBrief Description: When Raj meets Simran in Europe, it isn't love at first sight but when Simran moves to India for an arranged marriage, love makes its presence felt.
   
"""

movies_watched = st.text_input("Enter the movies that you enjoy watching:", key="input", placeholder="Input movies here")

Jsoncov = """please convert the given content into a json table with keys as numbers and each key has a Name, Year of release, Genre, Rating and Language and link to access. Expand the body with valid information regarding the heading. 
Please follow this example exactly
"""

class InputSchema(pw.Schema):
    Name: str
    Year: str
    Genre: str
    Language: str

def get_recommendations(movies):
    recommendations = model.invoke(context + movies)
    return recommendations.content

def get_json(content, prompt):
    jsonrec = model.invoke(prompt + content)
    return jsonrec.content

if st.button("Get Recommendations"):
    response = get_recommendations(movies_watched)
    st.write(response)

    JsonAns = get_json(response,Jsoncov)

    try:
        json_data = json.loads(JsonAns)
    except json.JSONDecodeError as e:
        st.markdown(f"# TABLE VIEW :")
        st.write(JsonAns)


        if 'json_data' in locals():
            op = pw.Table.from_dict(JsonAns, schema=InputSchema)
            pw.io.jsonlines.write(op,"op.jsonl")
            st.write("The output has been saved as op.jsonl")
            
        pw.run()

    st.write("This app is created as part of the Pathway AI Bootcamp conducted in collaboration with Mulearn and Pathway.com.")
    st.link_button("Made with love by Blesson K Tomy", "https://www.profile.blessonktomy.tech")






