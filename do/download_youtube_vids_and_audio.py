#!./env/bin/python
import pafy
import sys
import re

if len(sys.argv) != 2:
    print("Please enter a youtube url")
    sys.exit(1)

url = sys.argv[1]

video = pafy.new(url)

print("Title: ", video.title)

streams = video.streams
print("\nAvailable Streams: ", streams)

audiostreams = video.audiostreams
print("\nAudiostreams: ")
for idx, astream in enumerate(audiostreams):
    print(idx,
            astream.bitrate,
            astream.extension,
            astream.get_filesize(),
            )

    

which = input("Select which stream to download: ")

print("\ndownloading item {}".format(which))

# usually the stream with m4a is the preferred, as opposed to webm.
# typical rate is 128
audiostreams[int(which)].download("yt_music_shelf/"+re.sub(r'\s+', '_', video.title+"."+audiostreams[int(which)].extension))
print("===== All Done! =====")
