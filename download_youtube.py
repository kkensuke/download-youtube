import os
import re

from pytube import YouTube, Playlist
import moviepy.editor as mp

def download_youtube(url, path):
    try:
        yt = YouTube(url)
        yt_title = yt.title.replace("/", "").replace(".", "").replace('"', "").replace("'", "").replace(":", "").replace("*", "").replace(",", "").replace("|", "").replace("?", "")
        if not os.path.exists(path + yt_title+ '.mp4'):
            print(f'Downloading video: {yt.title}: {url}')
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download(path)
        else:
            print(f'Video {yt.title} already exists, skipping.') # sometimes fails
    except:
        print(f'Video {yt.title} is unavaialable, skipping.')
    print('Downloaded: ' + yt.title)


def download_video_playlist(url, path):
    playlist = Playlist(url)
    for url in playlist.video_urls:
        try:
            yt = YouTube(url)
            yt_title = yt.title.replace("/", "").replace(".", "").replace('"', "").replace("'", "").replace(":", "").replace("*", "").replace(",", "").replace("|", "").replace("?", "")
            if not os.path.exists(path + yt_title+ '.mp4'):
                print(f'Downloading video: {yt.title}: {url}')
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download(path)
            else:
                print(f'Video [{yt.title}] already downloaded, skipping.') # sometimes fails
        except:
            print(f'Video [{yt.title}] is unavaialable, skipping.')
    print('Playlist Downloaded: ' + playlist.title)


def download_music_playlist(url, path):
    playlist = Playlist(url)
    for url in playlist.video_urls:
        try:
            yt = YouTube(url)
            yt_title = yt.title.replace("/", "").replace(".", "").replace('"', "").replace("'", "").replace(":", "").replace("*", "").replace(",", "").replace("|", "").replace("?", "")
            if not os.path.exists(path + yt_title+ '.mp3'):
                print(f'Downloading video: {yt.title}: {url}')
                yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').first().download(path)
            else:
                print(f'Video [{yt.title}] already downloaded, skipping.') # sometimes fails
        except:
            print(f'Video {url} is unavaialable, skipping.')
    print('Playlist Downloaded: ' + playlist.title)

    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path,file)
            mp3_path = os.path.join(path,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)