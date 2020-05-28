import time
from struct import *
import socket

def pack_thought_details(user_id, thought):
    user_id_number                  = int(user_id)
        
    thought_size, thought_data      = len(thought), thought.encode('utf-8')
    
    timestamp                       = int(time.time())
    
    # user_id        :    uint64
    # timestamp      :    uint64
    # thought_size   :    uint32
    # thought_data   :    <thought size> bytes
    THOUGHT_HEADER_FORMAT           = '<QQI'
    THOUGHT_DATA_FORMAT             = '{0}s'.format(thought_size)
    THOUGHT_FORMAT                  = THOUGHT_HEADER_FORMAT + THOUGHT_DATA_FORMAT

    # Packing thought    
    packed_thought = \
        pack(THOUGHT_FORMAT, \
             user_id_number, \
             timestamp, \
             thought_size, \
             thought_data)
        
    return packed_thought

from cli import CommandLineInterface

cli = CommandLineInterface()
      
@cli.command
def upload(address, user, thought):
    # Parse server address
    server_ip_str, server_port_str  = address.split(":")
    server_port_int                 = int(server_port_str)
    
    # Pack thought
    packed_thought = pack_thought_details(user, thought) 
    
    # Connect and sent to server
    conn = socket.socket()
    conn.connect((server_ip_str, server_port_int))
    conn.sendall(packed_thought)
    
    # Print done
    print('done')

if __name__ == '__main__':
    import sys    
    sys.exit(cli.main())

