# Download YouTube videos

`download_youtube.py` includes three functions: `download_youtube()`, `download_video_playlist()`, `download_music_playlist()`.

You have to specify the URL of the YouTube video or playlist you will download.

You can download one video by `download_youtube()` and one playlist by `download_video_playlist()`, `download_music_playlist()`.

By using `download_music_playlist()`, `mp4` files are converted to `mp3`.

*All three functions try to skip downloading videos when they are already downloaded but note that it sometimes fails.