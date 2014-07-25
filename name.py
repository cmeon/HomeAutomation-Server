#!/usr/bin/python
import xmpp
import handlers
import new_handler
from omxplayer import OMXPlayer

user="foe.capstone.15@gmail.com"
password="nfcandroidpi"


# the player
player = None

options = {
   "play_movie": new_handler.play_media,
   "play_video": new_handler.play_media,
   "torch": handlers.toggle_on_off_lights,
   "action": new_handler.toggle_action
}

media = {
	#movies
   'tt0120903': '/home/pi/XMen.mp4',
   'tt0311429': '/home/pi/LXG.mp4',
   'tt0903747': '/home/pi/break.avi',
   'tt1204975': '/home/pi/LAST\ VEGAS.mp4',
   'tt1403865': '/home/pi/True\ Grit.mp4',
   'tt1826590': '/home/pi/Langkawi.mp4',
   'tt2239832': '/home/pi/Think\ Like\ A\ Man.mp4',
   'tt1621045': '/home/pi/Think\ Like\ A\ Man.mp4',

        #actions
   'pause': 'pause',
   'stop' : 'stop'
	#music
}

def message_handler(conn_object, message_node):
   global player
   print message_node.getBody()
   command = message_node.getBody().split()
   if (player == None):
      player = options[command[0]](media[command[1]], player)
   else:
      if (command[0] == "play_media" or command[0] == "play_movie"):
         player.stop()
         player = options[command[0]](media[command[1]], player)
      else:
         options[command[0]](media[command[1]], player)


def presence_handler(conn_object, presence_node):
   print presence_node.getAttr("from")
   print presence_node.getShow()


jid=xmpp.JID(user)
connection = xmpp.Client(jid.getDomain())
connection.connect()
print "done connection"
result=connection.auth(jid.getNode(), password, "Some Client-Name")

connection.sendInitPresence()

connection.RegisterHandler('presence', presence_handler)
connection.RegisterHandler('message', message_handler)


while connection.Process(1):
    pass


