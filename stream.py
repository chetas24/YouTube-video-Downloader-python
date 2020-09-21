from pytube import YouTube

link = input("Enter Your Youtube Link : ")
myVideo = YouTube(link)

# To get all streams available
'''
stream = myVideo.streams.all()
for i in stream:
    print(i)
'''

print('\n')

# for ascending order of stream
# for descending order we can use streams.desc()
'''
ascending = myVideo.streams.asc()
for i in ascending:
    print(i)
'''

# To get the first and second format
print(myVideo.streams.first())
print(myVideo.streams.last())

print('\n')

# Get highest resolution stream that is a progressive video
print("Highest resolution :", myVideo.streams.get_highest_resolution())

# Get lowest resolution stream mp4
print("Lowest resolution :", myVideo.streams.get_lowest_resolution())

# Get By Resolution You can edit as per Your need
print("480p Resolution :", myVideo.streams.get_by_resolution(resolution="480p"))

# Get By itag
print("itag :", myVideo.streams.get_by_itag(itag=22))

# We can use for loop to get every stream in list