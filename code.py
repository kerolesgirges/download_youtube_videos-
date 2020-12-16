pip install pytube                                            # install liberary to serve our code 
# type python in cmd and (>>) will apper in start of line     #
import pytube 
url = '(your youtube video link )'                            # remove ()
youtube = pytube.YouTube(url)                                 #Load url in function Youtube 
video = youtube.streams.first()                               #to set resolution
# or replace first with get_highest_resolution   #
#Download Video : #
video.download()                                              # In Same Folder
# or #
video.download('/Downloads')                                  # In Other Folder replace with your distanation 
