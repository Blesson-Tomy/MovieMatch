# MovieMatch

### A movie recommendation system that reads your preferances of movies and recommends similar genre of movies for you. 

## Idea
A streamlit application for suggesting movies based on the genre, language and type of movies that you normally watch. The output is further converted into JSON and then further processed. This has been made possible by the integration of pathway. The large language model used is Google's GEMINI.

## Features
1) **User Interface:** Streamlit provides a simple and intuitive User Interface for the program.
2) **Easy Access to Movie Info:** LLM provides links to the rating and IMDB reference to the links.
3) **Multiple Language Support:** LLM provides updated knowledge of Movies and Series in major languages.
4) **Json Conversion:** The data output by the LLM is output in a JSON Format arranged by Key Value Pairs on Name, Year, Genre and Language

## Demo

https://drive.google.com/file/d/1USraSIJLgYTS5KwKmOuMJL3yQnig9EfQ/view?usp=sharing

## Technologies Used
**Frontend:** Streamlit

**Data Processing:** Pathway

**Programming Language:** Python

**Large Language Model:** Gemini

# Installation
1. **Clone the Repository**
    
    ```bash
    git clone
    ```

2. **Install the necessary dependencies**
    ```bash
        pip install -r requirements.txt
    ```

3. **Create a Google Gemini API Key**

    1. Create a '.env' file
    2. Add the created GEMINI_API_KEY to the '.env' file
    3. Do not share the GEMINI_API_KEY with anyone


4. **Run the Streamlit App on Localhost**
    ```bash
    streamlit run main.py
    ```

# Instructions for use
1. Follow the above instructions to accurately install the app

2. Run the app using Streamlit as shown above

3. Enter the names of the movies that you like to watch. Be as precise with the names as possible. Malayalam movies are not recommended due to the limited knowledge scope of the Gemini Model

4. Click 'Get Recommendations' button to generate the response

# Notes:
This is part of a AI Bootcamp that is conducted by Mulearn and Pathway.com. I am truly grateful to have been a part of this and look forward to more such opportunities.