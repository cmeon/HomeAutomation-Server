#!/usr/bin/python
import xmpp
import handlers
import new_handler

user="foe.capstone.15@gmail.com"
password="nfcandroidpi"

# the player
player = None

options = {
   "play_movie": new_handler.play_media,
   "torch": handlers.toggle_on_off_lights,
   "toggle": new_handler.toggle_action
}

media = {
	#movies
   'tt0120903': '/home/pi/tutv.avi',
   'tt0311429': '/home/pi/gush.mp3',
   'tt0903747': '/home/pi/file1.mp4',
   'tt1403865': '/home/pi/file1.mp4',
   'tt1826590': '/home/pi/file1.mp4',
   'tt2239832': '/home/pi/file1.mp4',
   'tt1621045': '/home/pi/file1.mp4'

	#music
}

def message_handler(conn_object, message_node):
   print message_node.getBody()
   command = message_node.getBody().split()
   player = options[command[0]](media[command[1]])

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


