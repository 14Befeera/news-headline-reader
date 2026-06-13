import streamlit as st
import requests
import pyttsx3


import threading

st.title("News Headline Reader")

# Session state
if "headlines" not in st.session_state:
    st.session_state.headlines = []

API_KEY = "b61505ca88c943769025ebf5c8687ec0"

#  Speech function
def speak_news(headlines):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    engine.say("Here are the latest news headlines")

    for article in headlines:
        engine.say(article['title'])

    engine.runAndWait()

#  FORM
with st.form("news_form"):
    category = st.selectbox(
        "Select News Category",
        ["general", "technology", "sports", "business", "health"]
    )

    num_news = st.slider("Select number of news headlines", 1, 10, 5)

    submit = st.form_submit_button("Get News")

#  Fetch News
if submit:
    url = f"https://newsapi.org/v2/everything?q={category}&language=en&sortBy=publishedAt&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])

    #  Store FULL articles (not just title)
    st.session_state.headlines = articles[:num_news]

#  Display News
if st.session_state.headlines:
    st.subheader("Latest Headlines")

    for i, article in enumerate(st.session_state.headlines):
        title = article['title']
        source = article['source']['name']
        date = article['publishedAt'][:10]

        st.write(f"{i+1}. {title}")
        st.caption(f"Source: {source} | Date: {date}")

#  Play News
if st.button("Play News"):
    if st.session_state.headlines:
        threading.Thread(
            target=speak_news,
            args=(st.session_state.headlines,)
        ).start()
    else:
        st.warning("Please fetch news first!")