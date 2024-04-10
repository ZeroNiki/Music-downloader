import requests
from config import TOKEN
import subprocess
import yt_dlp
import os

from config import FULL_DIR

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
    search_url = f"https://api.discogs.com/database/search?q={track_name}&artist={author}&token={TOKEN}"

    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()

        if data['results']:
            cover_img_link =data['results'][0]['cover_image'] 

            command = f'wget -O "{full_path_to_music}{author} {track_name}.jpg" {cover_img_link}' 

            subprocess.run(command, shell=True)

    return None

