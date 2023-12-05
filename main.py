from utils import *
from pytube import YouTube

# TODO: Use metadata to sort the files in destination (or give option to). Sort by author name, retain as much as possible.

# Accept URL as input.
file_url = input("Please enter the URL to the YouTube video: \n>> ")

# Parse the URL into an object.
video_obj = YouTube(str(file_url))

# Instantiate an audio streaming object.
audio_obj = video_obj.streams.filter(only_audio=True).first()
  
# Download the file.
in_file = audio_obj.download(output_path = './downloads')

convert_to_mp3(in_file, video_obj.title)

# Delete the temporary '.mp4' file.
os.remove(in_file)

# Display results.
print("'" + video_obj.title + " by " + video_obj.author + "' has been successfully downloaded.")