from youtube_dl import YoutubeDL

def download(ytquery, songs, metadata):
    ydl_opts = {
        'outtmpl': f'temp/{ytquery}.mp3',
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    songs[f"{ytquery}.mp3"] = metadata

    with YoutubeDL(ydl_opts) as ydl:
        print(f"- Downloading {ytquery}")
        ydl.extract_info(f"ytsearch:{ytquery}", download=True)[
            'entries'][0]
        print(f"- Finished downloading {ytquery}")
