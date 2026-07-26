from flask import Flask, render_template, request, session
import requests
import pyttsx3
import threading

app = Flask(__name__)
app.secret_key = "news_reader_secret"

API_KEY = "b61505ca88c943769025ebf5c8687ec0"

latest_headlines = []


# Text to Speech
def speak_news(headlines):

    for title in headlines:

        if title:

            print("Speaking:", title)

            engine = pyttsx3.init('sapi5')
            engine.setProperty('rate', 140)
            engine.setProperty('volume', 1.0)

            engine.say(title)
            engine.runAndWait()

            engine.stop()


# Home page
@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():

    articles = []

    if request.method == "POST":

        category = request.form["category"]
        number = int(request.form["num_news"])

        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={category}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
        )

        response = requests.get(url)

        data = response.json()

        articles = data.get("articles", [])[:number]


        session["headlines"] = [
            article["title"].replace("...", "").strip()
            for article in articles
            if article.get("title")
        ]


    return render_template(
        "index.html",
        headlines=articles
    )




# Play News
@app.route("/play")
def play():

    headlines = session.get("headlines", [])

    if headlines:

        threading.Thread(
            target=speak_news,
            args=(headlines,)
        ).start()

    return render_template(
        "index.html",
        headlines=[
            {
                "title": title,
                "source": {"name": ""},
                "publishedAt": ""
            }
            for title in headlines
        ]
    )


if __name__ == "__main__":
    app.run(debug=True)
