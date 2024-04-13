import requests
import subprocess
import yt_dlp
import os

from src.config import FULL_DIR

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


def downlad_cover(author, track_name, full_path_to_music, url):
    command = f'wget -O "{full_path_to_music}{author} {track_name}.jpg" {url}' 

    subprocess.run(command, shell=True)

    return None

