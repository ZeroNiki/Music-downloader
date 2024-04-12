import requests
import subprocess
import yt_dlp
import os

from src.config import FULL_DIR, TOKEN

def download_music(link, author, track_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(FULL_DIR, f'{author} {track_name}'),
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


def downlad_cover(author, track_name, full_path_to_music):
    # Search for album on Discogs
    search_url = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&artist={author}&album={track_name}&api_key={TOKEN}&format=json"

    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()

        cover_img_link = data['album']['image'][4]["#text"]

        command = f'wget -O "{full_path_to_music}{author} {track_name}.jpg" {cover_img_link}' 

        subprocess.run(command, shell=True)

    return None

