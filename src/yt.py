from bs4 import BeautifulSoup
import requests

from src.config import YT_LINK 
import yt_dlp

import re


def yt_search(keyword: str):
    link = f"{YT_LINK}{keyword}"

    r = requests.get(link)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")

        get_div = soup.find("div", class_="pure-u-1 pure-u-md-1-4")
        get_href = get_div.find("a")['href']

        return f"https://www.youtube.com{get_href}"

    else:
        print("Error")
        return None


def yt_search_by_id(url: str):
    word_black_list = ["Official", "Music", "Video", "Vevo"]
    symbols_black_list = ["(", ")"]
    escaped_symbols = [re.escape(symbol) for symbol in symbols_black_list]

    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)

        video_id = info.get('id', None)

    p_url = f"https://yt.artemislena.eu/watch?v={video_id}"
    
    r = requests.get(p_url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html.parser")

        pattern = r'\b(?:{})\b|{}'.format('|'.join(map(re.escape, word_black_list)), '|'.join(escaped_symbols))

        channel_profile = soup.find("div", class_="channel-profile")
        author = channel_profile.find("span").text
        cleaned_author = re.sub(pattern, '', author)


        get_h_box = soup.find("div", class_="h-box")
        song_name = soup.find("h1").text
        song = re.sub(pattern, '', song_name)
        clean_song_name = re.sub(r'\s+', ' ', song)

        if cleaned_author in clean_song_name:
            pattern2 = r'\b{}\b'.format(re.escape(cleaned_author))
            cleaned_song2 = re.sub(pattern2, '', clean_song_name)
            return [cleaned_author, cleaned_song2]
        else:
            return [cleaned_author, clean_song_name]



        




