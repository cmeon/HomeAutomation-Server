#!/usr/bin/python

from omxplayer import OMXPlayer

# Handles actions for home automation server

# play video
def play_media(media, player=None):
    print "playing movie"
    return OMXPlayer(media)

# pause video
def pause_media(player):
    print "pausing..."
    player.toggle_pause()

def stop_media(player):
    print "stopping..."
    player.stop()

def toggle_action(action, player):
    {"pause":pause_media, "stop": stop_media}[action](player)
