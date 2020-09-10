################
Links: https://github.com/anujbansal16/Jarvis-Assistant
https://pythonspot.com/personal-assistant-jarvis-in-python/
https://www.activestate.com/blog/how-to-build-a-digital-virtual-assistant-in-python/
https://www.geeksforgeeks.org/personal-voice-assistant-in-python/
https://towardsdatascience.com/how-to-build-your-own-ai-personal-assistant-using-python-f57247b4494b
https://github.com/anujbansal16/Jarvis-Assistant/blob/49a945484182af2939ed5c0801ce149c4c1e0c6c/main.py

#Pre_requists:
pip install SpeechRecognition
pip install gtts
pip install pipwin
pipwin install pyaudio
pip install pyttsx3
pip install webbrowser
pip install wikipedia
pip install youtube_search
##################

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pyttsx3
import webbrowser
import wikipedia
from youtube_search import YoutubeSearch
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speakaudio(text):
 #engine.setProperty('volume',1.0) # setting up volume level from 0 to 1
   #changing index, changes voices. 1 for female 
 engine.say(text)
 engine.runAndWait()    
   
def speak(audioString):
    print(audioString)
    #tts = gTTS(text=audioString, lang='en')
    #tts.save("audio.mp3")
    #os.system("mpg321 audio.mp3")

def greet():
 msg="Good morning, Suzeet. This is Seno, your virtual assistant. How I can help you today"
 speak(msg)
 speakaudio(msg)
 
    
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
     print("I am listening!")
     #speakaudio("Say something!")
     audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
        #speakaudio(data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speakaudio('I could not understand, Can you please repeat')
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

def googleSearch(query):
 query=query.replace("google","",1)
 url="https://www.google.com.tr/search?q={}".format(query)
 webbrowser.open_new_tab(url)
 time.sleep(3)

def wikiData(query,sentences=1):
  speakaudio("Searcing Wikipedia")
  try:
       wikiData=wikipedia.summary(query,sentences=sentences,auto_suggest=True)
       print(wikiData)
       speakaudio(wikiData)
       return 1
  except Exception as e:
       speakaudio("Sorry Suzeet, I cant find anything related to that on wikipedia")
       return None

def playMusic(query):
 results = YoutubeSearch(query, max_results=1).to_dict()
 speakaudio("Playing: {}".format(results[0]["title"]))
 url = "https://www.youtube.com/{}".format(results[0]["url_suffix"])
 webbrowser.open_new_tab(url)

def speakNews():
    #speakaudio("News category {}".format(category))
    speakaudio("Geting news from TIMES now")
    #news_url=self.newsCategories[category]
    #Client=urlopen(news_url)
    #Client=urlopen("https://www.hindustantimes.com/india-news/")
    Client = requests.get("https://timesofindia.indiatimes.com/home/headlines")
   
    xml_page=Client.read()
    print(xml_page)
    Client.close()
    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    news=[]
    count=1
    for news in news_list:
        title=news.title.text
        desc=remove_html_tags(news.description.text)
        print(title)
        print(desc)
        speak("News: {}".format(count))
        speak(title)
        speak(desc)
        print("-"*60)
        count+=1
        if count>5:
           break
                
def jarvis(data):
    wordarr=data.split(" ")
    resQuery=' '.join(wordarr[1:])
    print(wordarr[0])
    if "how are you" in data:
        speak("I am fine")
        speakaudio('I am fine')
    elif "who are you" in data:
        speak("I am Senorita, You can call me Seno")
        speakaudio('I am Senorita, You can call me Seno')
    elif "what do you eat" in data:
        speak("I am a robot, I use CPU and GPU")
        speakaudio('I am a robot, I use CPU and GPU')
    elif "who created you" in data:
        speak("Sujeet created me")
        speakaudio('Sujeet created me')
    elif "can you eat" in data:
        speak("No, I am a robot , I can not eat")
        speakaudio('No, I am a robot , I can not eat')
    elif "can you walk" in data:
        speak("No, I am a robot , I can not walk")
        speakaudio('No, I am a robot , I can not walk') 
    elif "can you" in data:
        speak("No, I am a robot , I can not")
        speakaudio('No, I am a robot , I can not walk')    
    elif "can you work" in data:
        speak("No, I am a robot , I can not work")
        speakaudio('No, I am a robot , I can not work')     
    elif "what time is it" in data:
        speak(ctime())
        speakaudio(ctime())
    elif wordarr[0]=="google" or wordarr[0]=="Google":
      #query=query.replace("google","",1)
      googleSearch(resQuery)
    elif wordarr[0]=="wikipedia" or wordarr[0]=="Wikipedia":
      #query=query.replace("google","",1)
      googleSearch(resQuery)
  
    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Sujeet, I will show you where " + location + " is.")
        speakaudio("Hold on Sujeet, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
    elif wordarr[0]=="YouTube":
        #query=query.replace("youtube","",1)
        url="https://www.youtube.com/results?search_query={}".format(resQuery)
        webbrowser.open_new_tab(url)
        time.sleep(3)
    elif wordarr[0]=="play":
        playMusic(resQuery)
        time.sleep(30)
    elif wordarr[0]=="news" or (wordarr[0]=="open" and wordarr[1]=="news"):
        speakNews()
        time.sleep(90)
    else:
     if not wikiData(data):
       #speakaudio("Let me try to search it in google for you ")
       #googleSearch(resQuery)    
       speakaudio('I could not find option, Can you please repeat')
       speak('I could not find option, Can you please repeat')
    
# initialization
#time.sleep(0.30)
greet()
while 1:
    data = recordAudio()
    if "bye" in data:
        speak('Thank You Suzeet, See you Soon again')
        speakaudio('Thank You Suzeet, See you Soon again')
        break
    else:
     jarvis(data)    
    
    
    
    
    