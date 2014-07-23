#!/usr/bin/python
import xmpp
import handlers

user="foe.capstone.15@gmail.com"
password="nfcandroidpi"

options = {
   "play_video": handlers.media_player,
   "torch": handlers.toggle_on_off_lights
}

movie = {
   "break": '/home/cmeon/Downloads/Veep.S03E06.HDTV.x264-2HD.mp4'
}

a = 1
def message_handler(conn_object, message_node):
   print message_node.getBody()
   command = message_node.getBody().split()
   options[command[0]](movie[command[1]])

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


