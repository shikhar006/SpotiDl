<div align="center">
<img src="https://i.imgur.com/7qSZ9rC.png" />

# SpotiDl
Download your Spotify playlists along with the metadata without spotify premium
</div>

## How does SpotiDl work?
1. Uses the spotify api to get plalist data
2. Searches youtube for the song
3. Downloads the song if a match is found
4. Adds basic metadata like:
    - Track Name
    - Artist
    - Album

## Installation
Check the [releases](https://github.com/shikhar006/SpotiDl/releases) page and download the most recent version.

### Installing FFmpeg
FFmpeg is required to convert the videos into audio
- [Windows Tutorial](https://windowsloop.com/install-ffmpeg-windows-10/)

## Running it on your own

### Installing FFmpeg
FFmpeg is required to convert the videos into audio
- [Windows Tutorial](https://windowsloop.com/install-ffmpeg-windows-10/)

1. Run - `pip install -r requirements.txt`
2. Add `cid` (client id) and `secret` (client secret) to creds.py. To get the client id and client secret do the following:

    - Browse to https://developer.spotify.com/dashboard/applications.

    - Log in with your Spotify account.

    - Click on ‘Create an app’.

    - Pick an ‘App name’ and ‘App description’ of your choice and mark the checkboxes.

    - After creation, you see your ‘Client Id’ and you can click on ‘Show client secret` to unhide your ’Client secret’.
3. Run - `python main.py`


## Disclaimer:
1. I dont earn anything from this.