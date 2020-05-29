# https://pypi.org/project/youtube-transcript-api/
# Il faut d'abord installer youtube_transcript_api avec un simple pip install

from youtube_transcript_api import YouTubeTranscriptApi
import os
import requests
from bs4 import BeautifulSoup

video_urls = ['https://www.youtube.com/watch?v=yvsIywjglA4','https://www.youtube.com/watch?v=Bd0eULaVwNQ','https://www.youtube.com/watch?v=vQKOcB8K4fk']

t = ''
for url in video_urls:
    try:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "lxml")
        for div in soup.find_all("h1"):
            name = div.text.replace("Cette vidéo n'est pas disponible.","").replace("  ","").replace("\n","")
        id = url.lstrip('https://www.youtube.com/watch?v=')
        transcript = YouTubeTranscriptApi.get_transcript(id, languages=['fr'])
        s = ''
        for object in transcript:
            text = object['text']+' '
            time = object['start']
            phrase = '(' + str(time) + ') ' + str(text)
            s += phrase
        t += '\n' + url + " ; " + name + " ; " + s
    except:
        print('error')

file = open('transcript.txt','w', encoding='utf-8')
file.write(t)
file.close()
