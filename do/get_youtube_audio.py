#!./env/bin/python
"""
Pass in a youtube url and it will downlaod the 128k m4a if possible
"""
import pafy
import sys
import re
import os

def clean_title(title):
    title = re.sub(r'\s+', '_', title)
    title = re.sub(r'\"', '', title)
    return title

if len(sys.argv) == 2:
    url = sys.argv[1]
    auto = False
elif len(sys.argv) == 3 and sys.argv[2] == "--auto":
    url = sys.argv[1]
    auto = True
else:
    print("Usage:\nget_youtube_audio.py <youtube-url> --auto")
    sys.exit(1)


video = pafy.new(url)

print("Title: ", video.title)

streams = video.streams
print("\nAvailable Streams: ", streams)

audiostreams = video.audiostreams
print("\nAudiostreams available: ")
m4a_128k_idx = None
for idx, astream in enumerate(audiostreams):
    if astream.bitrate == "128k" and astream.extension == "m4a":
        m4a_128k_idx = idx
    print(idx,
            astream.bitrate,
            astream.extension,
            astream.get_filesize(),
            )

if auto == True:    
    audio_idx = m4a_128k_idx
else:
    idx = input("Select which stream to download: ")
    if idx == "q" or idx == "Q":
        print("Quitting.")
        sys.exit(0)
    audio_idx = int(idx)


print("\ndownloading item {}".format(audio_idx))

audiostreams[audio_idx].download(
        "yt_music_shelf/"+clean_title(video.title)+"."+audiostreams[audio_idx].extension)
print("===== All Done! =====")

os.system("echo {} >> log_songs".format(url))
