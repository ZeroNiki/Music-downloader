import eyed3
from eyed3.id3.frames import ImageFrame

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3

import os

def change_cover(audio, cover_path):
    audio_file = eyed3.load(f'{audio}')

    audio_file.tag.images.set(ImageFrame.FRONT_COVER, open(f'{cover_path}','rb').read(), 'image/jpeg')

    audio_file.tag.save()

    try:
        os.remove(cover_path)
    except OSError as e:
        print(f"Error deleting file '{cover_path}': {e}")


def change_metadata(file_path, author, track_name):
    # Load the MP3 file
    audio = EasyID3(file_path)
    
    # Change metadata
    audio['artist'] = author
    audio['title'] = track_name
    
    # Save metadata changes
    audio.save()
