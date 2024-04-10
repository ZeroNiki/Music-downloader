from dw import downlad_cover, download_music 
from yt import yt_search 

from mtd_mp3 import change_cover, change_metadata

from config import FULL_DIR

def chooce():
    print("Welcome user\n1: search by name and track name\n2: by youtube link\n")
    
    ch = int(input())

    return ch

    pass

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
        print("Maybe soon") 



if __name__ == "__main__":
    main()
