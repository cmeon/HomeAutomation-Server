#!/usr/bin/python

import subprocess
import threading, zipfile

def handle_msg(msg):
    return
    
#plays the media files
def media_player(media):
    background = AsyncTask('/usr/bin/vlc', media)
    background.setDaemon(True)
    background.start()
    print('The main program continues to run in foreground.')

#turns lights on or off
def toggle_on_off_lights():
    background = AsyncTask('/usr/bin/totem', media)
    background.start()
    print('The main program continues to run in foreground.')

# This class performs playing the player in the background and
# brings it to the foreground when it is already playing
class AsyncTask(threading.Thread):
    def __init__(self, player, media_file):
        threading.Thread.__init__(self)
        self.player = player
        self.media_file = media_file
    def run(self):
        subprocess.call([self.player, self.media_file])
        print('done with bg process')
