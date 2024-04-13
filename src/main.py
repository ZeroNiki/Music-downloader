from src.dw import downlad_cover, download_music 
from src.yt import yt_search
from src.spotify import get_spotify_track

from src.mtd_mp3 import change_cover, change_metadata

from src.config import FULL_DIR


def main():
    result = get_spotify_track()
    author = result[0]
    clear_author = author.replace('&', '')

    track_name = result[1]
    cover_url = result[2]

    keyword = clear_author + " " + track_name
    file_name = f'{clear_author} {track_name}.mp3'
    cover_name = f'{clear_author} {track_name}.jpg'

    link = yt_search(keyword)

    download_music(link, clear_author, track_name)
    downlad_cover(clear_author, track_name, FULL_DIR, cover_url)

    change_metadata(f"{FULL_DIR}{file_name}", clear_author, track_name)
    change_cover(f"{FULL_DIR}{file_name}", f"{FULL_DIR}{cover_name}")

