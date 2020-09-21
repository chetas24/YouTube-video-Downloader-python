# Audio Downloader from Youtube videos
# Get Highest Bitrate audio

from pytube import YouTube

link = input("Please Enter Your Youtube Link for downloading Audio : ")

try:
    yt_getaudio = YouTube(link)

    # get_audio_only() gives highest bitrate audio stream
    yt_getaudio.streams.get_audio_only().download(output_path='/home/user/Downloads', filename='audio')
    print('YouTube video audio downloaded successfully')
except Exception as e:
    print(e)
