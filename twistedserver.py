#! /usr/bin/env python3

# This is my version of a twisted IRC server
# I would like to implement:
# usernames, logging, automatic disconnect of client is innactive for x amount of time
 
from twisted.internet import reactor, protocol, endpoints
from twisted.internet.protocol import Factory
from twisted.protocols import basic
import time, sys


# messages on server side after startup
print("Status: UP")
print("Welcome, Jack.")

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

log = open("connection_log.txt", "a")
print("-------", file=log)
print("Server Status: UP ---", current_time, file=log)
log.close()


                
      
class PubProtocol(basic.LineReceiver):
 
    def __init__(self, factory): # create empty variables for users name and state
        self.factory = factory
        
 
    def connectionMade(self): # Welcome message on connect
        self.sendLine(b"Welcome to Jack's IRC. Please type your name.")
        self.factory.clients.add(self)
        log = open("connection_log.txt", "a")
        print("Client has connected ---", self.transport.getPeer(),"---", current_time, file=log)
        log.close()

 
    def connectionLost(self, reason): # on disconnect
        log = open("connection_log.txt", "a")
        print("Client has disconnected ---", self.transport.getPeer(), "---", current_time, file=log)
        log.close()
        self.factory.clients.remove(self)

 
    def lineReceived(self, line): # formatting for messages sent over the server
        for c in self.factory.clients:
            source = u"<{}> ".format(self.transport.getPeer()).encode("ascii")
            c.sendLine(source + line)

class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()
        
    def buildProtocol(self, addr):
        return PubProtocol(self)
 
endpoints.serverFromString(reactor, "tcp:1025").listen(PubFactory())
reactor.run()