# Video Downloader from Youtube videos
# Get Highest Resolution Youtube videos

from pytube import YouTube

link = input("Please Enter Your Youtube Link for downloading Video : ")

try:
    yt_getvideo = YouTube(link)

    filters = yt_getvideo.streams.filter(progressive=True, file_extension='mp4')

    # Download the Highest Quality Video
    filters.get_highest_resolution().download(output_path='/home/user/Downloads')
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)
