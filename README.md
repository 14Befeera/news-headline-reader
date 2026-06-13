# News Headline Reader (Text-to-Speech)

##  Overview

This project is a News Headline Reader application built using Python and Streamlit. It fetches real-time news using an API and converts the headlines into speech using text-to-speech functionality.

##  Features

* Fetches real-time news using API
* Category-based news filtering
* Select number of headlines dynamically
* Displays news with source and date
* Converts text to speech for audio playback
* Interactive and user-friendly UI

##  Technologies Used

* Python
* Streamlit
* Requests
* pyttsx3 (Text-to-Speech)

##  Workflow

1. User selects news category and number of headlines
2. Application sends request to News API
3. Receives data in JSON format
4. Extracts headlines, source, and date
5. Displays news on UI
6. Converts headlines to speech using text-to-speec

##  How to Run

1. Clone the repository
2. Install required libraries:

   ```
   pip install streamlit requests pyttsx3
   ```
3. Run the application:

   ```
   streamlit run app.py
   ```
4. Open in browser and use the app

##  Future Improvements

* Add multilingual support
* Deploy application online
* Integrate advanced NLP features
* Improve UI/UX

##  Project Type

Machine Learning / AI-based Application (with API integration and text-to-speech)

