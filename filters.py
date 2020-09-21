# Filter is an StreamQuery Object

"""
     fps=None,
     res=None,
     resolution=None,
     mime_type=None,
     type=None,
     subtype=None,
     file_extension=None,
     abr=None,
     bitrate=None,
     video_codec=None,
     audio_codec=None,
     only_audio=None,
     only_video=None,
     progressive=None,
     adaptive=None,
     is_dash=None,
     custom_filter_functions=None
"""

from pytube import YouTube

link = input("Enter Your Youtube Link : ")
myVideo = YouTube(link)

fil = myVideo.streams

# To Get the FPS (frame per seconds)
print(fil.filter(fps=30))

# For Resolution
print(fil.filter(res="720p"))

# For Resolution
print(fil.filter(resolution="480p"))

# mime-type To get mp4/mp4/3gp file "specify as per your need"
print(fil.filter(subtype='mp4'))

# To get the type Video/Audio
print(fil.filter(type='audio'))

# Bitrate set as per need
# print(fil.filter(bitrate='6000kbps'))

# Video and Audio codec
print(fil.filter(video_codec='avc1.42001E'))
print(fil.filter(audio_codec='mp4a.40.2'))

# only Audio
print("Print All Audio Streams.........")
aud = fil.filter(only_audio=True)
for i in aud:
    print(i)

# only Video
print("Print All Video Streams.........")
vid = fil.filter(only_video=True)
for i in vid:
    print(i)

# Progressive adaptive Stream Audio/Video
print("Print all Progressive streams.........")
progressive = fil.filter(progressive=True)
for i in progressive:
    print(i)
