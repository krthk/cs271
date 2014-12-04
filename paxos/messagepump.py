'''
    Created on Dec 3, 2014
    @author: karthik
    '''
import threading
import Queue
import sys
import socket
import time

class MessagePump(threading.Thread):
    '''
        This class listens to a port on a node and passes the messages it receives to
        the main thread.
        '''
    
    def __init__(self, owner, port, queue):
        '''
            The MessagePump binds itself to port and appends all the messages it receives
            to a queue
            '''
        threading.Thread.__init__(self)
        self.owner = owner
        self.port = port
        self.queue = queue
        self.socket = None
        self.isRunning = True
    
    def run(self):
	print "Starting message pump"

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.bind(("localhost", self.port))
            self.isRunning = True
        
            #self.socket.settimeout( timeout )
        
        except Exception as e:
            if self.socket:
                self.socket.close()
            
            print "Could not open/bind to socket."
            print "Exception message:", e
            sys.exit(1)
        
        # Listen forever on the port and add received messages to the queue
        while True:
            if self.isRunning:
                data, addr = self.socket.recvfrom(2048)                
                self.queue.put(data)