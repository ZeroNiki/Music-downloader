from src.dw import downlad_cover, download_music 
from src.yt import yt_search, yt_search_by_id
from src.spotify import get_spotify_track

from src.mtd_mp3 import change_cover, change_metadata

from src.config import FULL_DIR

def chooce():
    print("Welcome user\n1: search by name and track name\n2: by youtube link (doesn't work correctly)\n3: by spotify track link")
    
    ch = int(input())

    return ch


def main():
    ch = chooce()

    if ch == 1:
        author = input("Artist (or artists) name:\n")
        track_name = input("Song name:\n")

        file_name = f'{author} {track_name}.mp3'

        keyword = author + " " + track_name

        link = yt_search(keyword)

        download_music(link, author, track_name)
        downlad_cover(author, track_name, FULL_DIR)

        change_metadata(f"{FULL_DIR}{file_name}", author, track_name)
        change_cover(f"{FULL_DIR}{file_name}", f"{FULL_DIR}{author} {track_name}.jpg")

    elif ch == 2:
        print("Someday I'll finish this (Just choose the first option)")
        url = input("Youtube link:\n")

        author_name = yt_search_by_id(url)[0]
        song_name = yt_search_by_id(url)[1]
        file_name = f'{author_name} {song_name}.mp3'

        download_music(url, author_name, song_name)
        downlad_cover(author_name, song_name, FULL_DIR)

        change_metadata(f"{FULL_DIR}{file_name}", author_name, song_name)
        change_cover(f"{FULL_DIR}{file_name}", f"{FULL_DIR}{author_name} {song_name}.jpg")

    elif ch == 3:
        result = get_spotify_track()
        author = result[0]
        track_name = result[1]

        keyword = author + "" + track_name
        file_name = f'{author} {track_name}.mp3'

        link = yt_search(keyword)

        download_music(link, author, track_name)
        downlad_cover(author, track_name, FULL_DIR)

        change_metadata(f"{FULL_DIR}{file_name}", author, track_name)
        change_cover(f"{FULL_DIR}{file_name}", f"{FULL_DIR}{author} {track_name}.jpg")


    else:

        print("Error")

