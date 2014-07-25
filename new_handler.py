#!/usr/bin/python

from omxplayer import OMXPlayer

# Handles actions for home automation server

# play video
def play_media(media):
    print "playing movie"
    return OMXPlayer(media)

# pause video
def pause_media(player, media):
    omx.toggle_pause()

def toggle_action(action, player):
    {"pause":pause_media }[action](player)
