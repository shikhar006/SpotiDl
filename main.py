"""
Run "pip install spotipy pydub youtube_dl" when running for the first time
https://developer.spotify.com/dashboard/
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import threading
import shutil
import os
from pydub import AudioSegment

from creds import *
from modules.download import download

try:
    os.mkdir("exports/")
except:
    pass


client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

continue_ = "y"

while continue_ == "y":

    try:
        os.remove(".cache")
        shutil.rmtree("temp")
    except:
        pass

    id = input("Enter the playlist id: ")
    try:
        playlist = sp.user_playlist_tracks(
            "spotify", id)["items"]
        start_time = time.time()
        print(f"- Proccessing {len(playlist)} song(s)")

    except:
        os.system("cls")
        print("Playlist not found")
        continue

    os.remove(".cache")

    songs = {}
    queries = 0

    threads = []

    for song in playlist:
        # print(song)
        # break
        songName = song['track']['name']
        for i in '*."/\[]:;|,#':
            songName = songName.replace(i, "")
        artist = song['track']['artists'][0]['name']
        album = song['track']['album']['name']
        query = songName + " by " + artist

        x = threading.Thread(target=download, args=(
            query, songs,
            {
                "artist": artist,
                "album": album,
                "#": song["track"]["track_number"],
                "title": song["track"]["name"]
            }
        )
        )
        threads.append(x)
        queries += 1
        x.start()

    for thread in (threads):
        thread.join()

    threads.clear()
    songs_ = list(songs.items())

    for key, item in songs_:
        if "?" in key:
            del songs[key]
            songs[key.replace("?", "")] = item

    def convert(metadata, music_file):
        print(f"- Adding metadata to {music_file}")
        song = AudioSegment.from_file(os.path.join("temp", music_file))
        song.export(os.path.join('exports', music_file),
                    format="mp3", tags=metadata)
        print(f'- Finished adding metadata to {music_file}')

    for music_file in os.listdir("temp/"):
        if '#' in music_file:
            os.rename(os.path.join("temp/", music_file),
                      os.path.join("temp/", music_file.replace("#", "")))
            music_file = os.path.join(music_file.replace("#", ""))

        music_file_ = music_file.replace("#", "?")
        x = threading.Thread(target=convert, args=(
            songs[music_file_], music_file))
        threads.append(x)
        x.start()

    for thread in (threads):
        thread.join()
    shutil.rmtree("temp")
    end_time = time.time()
    time_taken = end_time - start_time

    print("- Finished downloading {} song(s) in {} minute(s).".format(
        queries, round(time_taken, 1) / 60))

    continue_ = input("Do you want to continue?\ny/n:\n")
