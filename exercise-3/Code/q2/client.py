import time
from thought import *
from connection import *
import socket

from cli import CommandLineInterface

cli = CommandLineInterface()
      
@cli.command
def upload(address, user, thought):
    # Parse server address
    server_ip_str, server_port_str  = address.split(":")
    server_port_int                 = int(server_port_str)
    
    thought_object                  = Thought(user, datetime.fromtimestamp(int(time.time())), thought)
    
    # Pack thought
    packed_thought = thought_object.serialize()
    
    # Connect and sent to server
    sock = socket.socket()
    sock.connect((server_ip_str, server_port_int))
    conn = Connection(sock)
    conn.send(packed_thought)
    
    # Print done
    print('done')

if __name__ == '__main__':
    import sys    
    sys.exit(cli.main())

