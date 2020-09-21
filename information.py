#  We have Youtube Object in pytube module
#  Ro get the information about the video we can use this Properties
"""
    Title
    Author
    Captions
    Length
    Thumbnail_URL
    Description
    Views*
    Rating*
    Age Restricted
    Video Id
"""
from pytube import YouTube

# We have created an instance with the YouTube URL, now we can retrieve information
link = input("Enter Youtube Video Link : ")
yt = YouTube(link)

# Title of Video
print("Title of Video :", yt.title)

# Author of Video
print("Author of Video :", yt.author)

# Captions of Video
print("Caption of Video :", yt.captions)

# Length of Video in seconds
print("Length of Video :", yt.length)

# To get the Thumbnail Url to see the Thumbnail of Video
print("Thumbnail URL of Video :", yt.thumbnail_url)

# Description of Video
print("Description  of Video :", yt.description)

# Views of Video
print("Total Views of Video :", yt.views)

# Ratings of Video
print("Ratings of Video :", yt.rating)  # Its return type is float

# Age Restriction
# if FALSE then the video is not age restricted and if its TRUE then it is age restricted
print("Age Restrictions of Video :", yt.age_restricted)

# Video ID
print("Video ID :", yt.video_id)


